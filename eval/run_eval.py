#!/usr/bin/env python3
"""Run one skill against one input across agent harnesses and models.

Every run gets a fresh workspace outside the repo (so no repo CLAUDE.md,
AGENTS.md or settings leak in) containing only the skill, installed where the
harness looks for it, and the input file. The harness is then started headless
with the fixed prompt. Results are written to eval/results/<batch>/<run>/:

    meta.json        harness, model, CLI version, command, timing, exit code,
                     files the agent left behind in the workspace
    transcript.*     raw harness output (tool calls included where available)
    answer.md        the agent's final answer
    stderr.txt

Usage:
    python eval/run_eval.py                       # full matrix from config.json
    python eval/run_eval.py --harness claude --model sonnet --repeats 1
    python eval/run_eval.py --dry-run             # print commands only
"""
import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVAL = REPO / "eval"

# Where each harness discovers project-level skills.
SKILL_DIRS = {
    "claude": ".claude/skills",
    "vibe": ".vibe/skills",
    "cursor": ".cursor/skills",
}


def cli_version(exe):
    try:
        out = subprocess.run([exe, "--version"], capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=60)
        return (out.stdout or out.stderr).strip().splitlines()[-1]
    except Exception as exc:  # noqa: BLE001 - recorded, not fatal
        return f"unknown ({exc})"


def vibe_home(model, thinking, dest):
    """Copy ~/.vibe settings into dest with the active model and thinking level set.

    Vibe has no --model or thinking flag, and the user's global config must not
    be edited, so each run points VIBE_HOME at its own copy. Only top-level
    files are copied (config and login caches), not logs, history or skills.
    """
    src = Path.home() / ".vibe"
    dest.mkdir(parents=True)
    for f in src.iterdir():
        if f.is_file() and f.name not in ("vibehistory", "config.toml.bak"):
            shutil.copy2(f, dest / f.name)

    out, in_models = [], False

    def close_models_block():
        # Give the [[models]] block that just ended a thinking line if it had none.
        if in_models and not any(l.startswith("thinking =") for l in block):
            out.append(f'thinking = "{thinking}"')

    block = []
    for line in (src / "config.toml").read_text(encoding="utf-8").splitlines():
        if line.startswith("["):
            close_models_block()
            in_models, block = line.strip() == "[[models]]", []
        elif line.startswith("active_model ="):
            line = f'active_model = "{model}"'
        elif in_models and line.startswith("thinking ="):
            line = f'thinking = "{thinking}"'
        block.append(line)
        out.append(line)
    close_models_block()
    (dest / "config.toml").write_text("\n".join(out) + "\n", encoding="utf-8")


def build_command(harness, model, prompt, ws, out_dir, effort):
    """Return (exe, argv, extra_env, transcript_name)."""
    if harness == "claude":
        exe = shutil.which("claude")
        argv = [exe, "-p", prompt, "--model", model, "--effort", effort,
                "--output-format", "stream-json", "--verbose",
                # Skip user settings/hooks/skills and MCP servers; only the workspace counts.
                "--setting-sources", "project,local", "--strict-mcp-config",
                "--permission-mode", "bypassPermissions",
                "--no-session-persistence", "--no-chrome"]
        return exe, argv, {}, "transcript.jsonl"
    if harness == "cursor":
        # Effort and thinking are part of the Cursor model ID (e.g. "-medium").
        exe = shutil.which("cursor-agent")
        argv = [exe, "-p", prompt, "--model", model,
                "--output-format", "stream-json",
                "--force", "--trust", "--workspace", str(ws)]
        return exe, argv, {}, "transcript.jsonl"
    if harness == "vibe":
        exe = shutil.which("vibe")
        argv = [exe, "-p", prompt, "--output", "streaming",
                "--auto-approve", "--trust", "--workdir", str(ws),
                "--output-dir", str(out_dir / "vibe_export")]
        home = ws.parent / f"{ws.name}-vibehome"
        vibe_home(model, effort, home)
        return exe, argv, {"VIBE_HOME": str(home)}, "transcript.jsonl"
    raise ValueError(f"unknown harness: {harness}")


def final_answer(harness, stdout):
    """Pull the agent's final text out of the raw transcript."""
    lines = [l for l in stdout.splitlines() if l.strip()]
    for line in reversed(lines):
        try:
            event = json.loads(line)
        except ValueError:
            continue
        # claude and cursor stream-json both end with a "result" event.
        if event.get("type") == "result" and isinstance(event.get("result"), str):
            return event["result"]
        # vibe streaming: last assistant message, content is a list of parts.
        if event.get("role") == "assistant":
            content = event.get("content")
            if isinstance(content, list):
                content = "".join(p.get("text", "") for p in content if isinstance(p, dict))
            if isinstance(content, str) and content.strip():
                return content
    return stdout


def resolved_model(stdout):
    """Model actually used, if the harness reports it (claude init event)."""
    for line in stdout.splitlines()[:20]:
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") == "system" and event.get("model"):
            return event["model"]
    return None


def snapshot(root):
    return {str(p.relative_to(root)).replace("\\", "/")
            for p in root.rglob("*") if p.is_file()}


def cleanup(ws):
    # Vibe can still be flushing logs into its settings copy right after it
    # exits, so retry for a few seconds before giving up.
    for path in (ws, ws.parent / f"{ws.name}-vibehome"):
        for _ in range(10):
            shutil.rmtree(path, ignore_errors=True)
            if not path.exists():
                break
            time.sleep(1)
        else:
            print(f"      warning: could not remove {path}")


def run_one(cfg, harness, model, rep, batch_dir, prompt, dry_run):
    run_name = f"{harness}__{model.replace('/', '-')}__r{rep}"
    out_dir = batch_dir / run_name
    ws = Path(tempfile.mkdtemp(prefix=f"skill-eval-{harness}-"))

    skill_src = REPO / cfg["skill"]
    shutil.copytree(skill_src, ws / SKILL_DIRS[harness] / skill_src.name,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    shutil.copyfile(REPO / cfg["input"], ws / cfg["input_name"])

    exe, argv, extra_env, transcript_name = build_command(harness, model, prompt, ws, out_dir,
                                                          cfg["effort"][harness])
    if exe is None:
        print(f"[skip] {run_name}: {harness} CLI not found on PATH")
        cleanup(ws)
        return
    if dry_run:
        print(f"[dry] {run_name}\n      cwd={ws}\n      {' '.join(argv)}  env={extra_env}")
        cleanup(ws)
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    before = snapshot(ws)
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDECODE")}
    env.update(extra_env)

    print(f"[run] {run_name} ...", flush=True)
    start = time.time()
    try:
        proc = subprocess.run(argv, cwd=ws, env=env, capture_output=True, text=True,
                              encoding="utf-8", errors="replace",
                              stdin=subprocess.DEVNULL, timeout=cfg["timeout_s"])
        stdout, stderr, code = proc.stdout, proc.stderr, proc.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr, code = "TIMEOUT", "timeout"
    duration = round(time.time() - start, 1)

    (out_dir / transcript_name).write_text(stdout, encoding="utf-8")
    (out_dir / "stderr.txt").write_text(stderr or "", encoding="utf-8")
    (out_dir / "answer.md").write_text(final_answer(harness, stdout), encoding="utf-8")

    meta = {
        "harness": harness,
        "cli_version": cli_version(exe),
        "model_requested": model,
        "model_reported": resolved_model(stdout),
        "effort": cfg["effort"][harness],
        "repeat": rep,
        "prompt": prompt,
        "skill": cfg["skill"],
        "input": cfg["input"],
        "workspace": str(ws),
        "command": argv,
        "extra_env": extra_env,
        "started": dt.datetime.fromtimestamp(start).isoformat(timespec="seconds"),
        "duration_s": duration,
        "exit_code": code,
        "new_files_in_workspace": sorted(snapshot(ws) - before),
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    cleanup(ws)
    print(f"      exit={code} {duration}s new_files={meta['new_files_in_workspace']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=str(EVAL / "config.json"))
    ap.add_argument("--harness", choices=sorted(SKILL_DIRS), help="only this harness")
    ap.add_argument("--model", help="only this model (requires --harness)")
    ap.add_argument("--repeats", type=int, help="override repeats from config")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reextract", metavar="RESULTS_DIR",
                    help="rebuild answer.md from saved transcripts, no runs")
    args = ap.parse_args()

    if args.reextract:
        # Rebuild answer.md from saved transcripts without re-running anything.
        for meta_path in Path(args.reextract).glob("*/meta.json"):
            run_dir = meta_path.parent
            harness = json.loads(meta_path.read_text(encoding="utf-8"))["harness"]
            stdout = (run_dir / "transcript.jsonl").read_text(encoding="utf-8")
            (run_dir / "answer.md").write_text(final_answer(harness, stdout), encoding="utf-8")
            print(f"[re-extract] {run_dir}")
        return

    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    prompt = (REPO / cfg["prompt"]).read_text(encoding="utf-8").strip()
    repeats = args.repeats or cfg["repeats"]

    matrix = cfg["matrix"]
    if args.harness:
        matrix = {args.harness: [args.model] if args.model else matrix.get(args.harness, [])}
    elif args.model:
        sys.exit("--model requires --harness")

    batch_dir = EVAL / "results" / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    for harness, models in matrix.items():
        for model in models:
            for rep in range(1, repeats + 1):
                run_one(cfg, harness, model, rep, batch_dir, prompt, args.dry_run)
    if not args.dry_run:
        print(f"results: {batch_dir}")


if __name__ == "__main__":
    main()
