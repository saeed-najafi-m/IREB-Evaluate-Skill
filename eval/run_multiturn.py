#!/usr/bin/env python3
"""Run a skill as a multi-turn conversation with a simulated user (Claude Code only).

For each scenario, the skill agent gets the scenario's opening message in a fresh
workspace outside the repo that contains only the skill (as in run_eval.py). If the
agent asks something instead of delivering its result, a second Claude session plays
the user: it sees only the scenario's user card and the visible conversation, and
answers only what was asked. Its answer goes back into the same agent session
(--resume). This repeats until the result is delivered or max_turns is reached.

Layout of a skill's eval folder:

    eval/<skill>/config.json                  skill path, models, effort, stop rule
    eval/<skill>/scenarios/<name>/opening.md  first user message, sent verbatim
    eval/<skill>/scenarios/<name>/user.md     the simulated user's card: facts, behaviour
    eval/<skill>/results/<batch>/<name>/      written by this script:
        transcript.md       the visible conversation, unedited except the workspace
                            path, which is replaced by <workspace>
        <done_file>         the agent's result file, if it wrote one
        turn-<n>-agent.jsonl, turn-<n>-user.jsonl   raw harness output
        meta.json           models, commands, timing, stop reason

Usage:
    python eval/run_multiturn.py eval/ireb-workshop-plan
    python eval/run_multiturn.py eval/ireb-workshop-plan --scenario 2-missing-duration-setting
    python eval/run_multiturn.py eval/ireb-workshop-plan --dry-run
"""
import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import tempfile
import time
import uuid
from pathlib import Path

from run_eval import REPO, SKILL_DIRS, cleanup, cli_version, final_answer, resolved_model, snapshot

SIMULATOR_PROMPT = """You play the user in a test conversation. You asked an AI assistant for help, and it has replied. Write your next message to the assistant.

Rules:
- Answer only what the assistant asked in its last message. Do not volunteer other information.
- Use only the facts on your card and in your first message. For anything else, follow the behaviour on your card.
- Keep it short, as a requirements engineer would write in a chat.
- Write in the language of the conversation.
- Do not mention the card, the test, or these rules.
- Output only the message text, nothing else.

Your card:
{card}

Conversation so far:
{conversation}"""


def agent_argv(exe, cfg, message, session_id, first_turn):
    # Same flags as run_eval.py, except that the session is kept so it can be resumed.
    session = ["--session-id", session_id] if first_turn else ["--resume", session_id]
    return [exe, "-p", message, "--model", cfg["model"], "--effort", cfg["effort"],
            "--output-format", "stream-json", "--verbose",
            "--setting-sources", "project,local", "--strict-mcp-config",
            "--permission-mode", "bypassPermissions", "--no-chrome", *session]


def simulator_argv(exe, cfg, prompt):
    # No tools, no skills, no settings, no saved session: it only writes the reply.
    return [exe, "-p", prompt, "--model", cfg["simulator_model"], "--effort", cfg["simulator_effort"],
            "--output-format", "stream-json", "--verbose",
            "--setting-sources", "project,local", "--strict-mcp-config",
            "--tools", "", "--disable-slash-commands",
            "--no-session-persistence", "--no-chrome"]


def run(argv, cwd, timeout):
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDECODE")}
    start = time.time()
    try:
        proc = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True,
                              encoding="utf-8", errors="replace",
                              stdin=subprocess.DEVNULL, timeout=timeout)
        stdout, stderr, code = proc.stdout, proc.stderr, proc.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr, code = "TIMEOUT", "timeout"
    return stdout, stderr, code, round(time.time() - start, 1)


def conversation_text(turns):
    return "\n\n".join(f"{'USER' if role == 'user' else 'ASSISTANT'}:\n{text}" for role, text in turns)


def transcript_md(name, turns):
    lines = [f"# Transcript: {name}", ""]
    n = 0
    for role, text in turns:
        if role == "user":
            n += 1
            label = "User (opening message)" if n == 1 else "User (simulated)"
        else:
            label = "Skill agent"
        lines += [f"## Turn {n}: {label}", "", text.strip(), ""]
    return "\n".join(lines)


def run_scenario(cfg, scen_dir, out_dir, exe, dry_run):
    name = scen_dir.name
    opening = (scen_dir / "opening.md").read_text(encoding="utf-8").strip()
    card = (scen_dir / "user.md").read_text(encoding="utf-8").strip()
    session_id = str(uuid.uuid4())

    ws = Path(tempfile.mkdtemp(prefix="skill-eval-mt-"))
    sim_ws = Path(tempfile.mkdtemp(prefix="skill-eval-mt-user-"))
    skill_src = REPO / cfg["skill"]
    shutil.copytree(skill_src, ws / SKILL_DIRS["claude"] / skill_src.name,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    if dry_run:
        argv = agent_argv(exe, cfg, "<opening.md>", session_id, True)
        print(f"[dry] {name}\n      skill={skill_src}\n      cwd={ws}\n      agent: {' '.join(argv)}")
        argv = simulator_argv(exe, cfg, "<simulator prompt>")
        print(f"      user:  cwd={sim_ws}\n             {' '.join(argv)}")
        cleanup(ws)
        cleanup(sim_ws)
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    before = snapshot(ws)
    turns = [("user", opening)]
    turn_meta, stop_reason, done_path = [], None, None
    message = opening
    print(f"[run] {name} ...", flush=True)

    for n in range(1, cfg["max_turns"] + 1):
        argv = agent_argv(exe, cfg, message, session_id, n == 1)
        stdout, stderr, code, secs = run(argv, ws, cfg["timeout_s"])
        (out_dir / f"turn-{n}-agent.jsonl").write_text(stdout, encoding="utf-8")
        answer = final_answer("claude", stdout)
        turns.append(("agent", answer))
        found = sorted(ws.rglob(cfg["done_file"]))
        done_path = found[0] if found else None
        turn_meta.append({"turn": n, "agent_exit_code": code, "agent_duration_s": secs,
                          "agent_model_reported": resolved_model(stdout),
                          "agent_stderr": (stderr or "")[-2000:]})
        print(f"      turn {n}: agent exit={code} {secs}s", flush=True)

        if code != 0:
            stop_reason = f"agent exit code {code}"
            break
        if done_path or cfg["done_marker"] in answer:
            stop_reason = "result delivered"
            break
        if n == cfg["max_turns"]:
            stop_reason = "max_turns reached"
            break

        prompt = SIMULATOR_PROMPT.format(card=card, conversation=conversation_text(turns))
        stdout, stderr, code, secs = run(simulator_argv(exe, cfg, prompt), sim_ws, cfg["timeout_s"])
        (out_dir / f"turn-{n}-user.jsonl").write_text(stdout, encoding="utf-8")
        message = final_answer("claude", stdout).strip()
        turn_meta[-1].update({"user_exit_code": code, "user_duration_s": secs,
                              "user_stderr": (stderr or "")[-2000:]})
        print(f"      turn {n}: user exit={code} {secs}s", flush=True)
        if code != 0 or not message:
            stop_reason = f"simulated user failed (exit code {code})"
            break
        turns.append(("user", message))

    # The agent may name its temporary workspace (which contains the local user name); mask it.
    transcript = transcript_md(name, turns).replace(str(ws), "<workspace>")
    (out_dir / "transcript.md").write_text(transcript, encoding="utf-8")
    if done_path:
        shutil.copyfile(done_path, out_dir / cfg["done_file"])
    meta = {
        "scenario": name,
        "cli_version": cli_version(exe),
        "skill": cfg["skill"],
        "model": cfg["model"], "effort": cfg["effort"],
        "simulator_model": cfg["simulator_model"], "simulator_effort": cfg["simulator_effort"],
        "max_turns": cfg["max_turns"],
        "session_id": session_id,
        "workspace": str(ws),
        "agent_command": agent_argv(exe, cfg, "<message>", session_id, True),
        "simulator_command": simulator_argv(exe, cfg, "<simulator prompt>"),
        "simulator_prompt_template": SIMULATOR_PROMPT,
        "turns": turn_meta,
        "agent_turns": len(turn_meta),
        "stop_reason": stop_reason,
        "result_file": str(done_path.relative_to(ws)).replace("\\", "/") if done_path else None,
        "new_files_in_workspace": sorted(snapshot(ws) - before),
        "finished": dt.datetime.now().isoformat(timespec="seconds"),
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    cleanup(ws)
    cleanup(sim_ws)
    print(f"      stop: {stop_reason}; result file: {meta['result_file']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skill_eval_dir", help="e.g. eval/ireb-workshop-plan")
    ap.add_argument("--scenario", action="append", help="only this scenario (repeatable)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    base = Path(args.skill_eval_dir).resolve()
    cfg = json.loads((base / "config.json").read_text(encoding="utf-8"))
    scenarios = sorted(p for p in (base / "scenarios").iterdir() if p.is_dir())
    if args.scenario:
        scenarios = [p for p in scenarios if p.name in args.scenario]
        missing = set(args.scenario) - {p.name for p in scenarios}
        if missing:
            raise SystemExit(f"unknown scenario(s): {', '.join(sorted(missing))}")

    exe = shutil.which("claude")
    if exe is None:
        raise SystemExit("claude CLI not found on PATH")
    batch_dir = base / "results" / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    for scen_dir in scenarios:
        run_scenario(cfg, scen_dir, batch_dir / scen_dir.name, exe, args.dry_run)
    if not args.dry_run:
        print(f"results: {batch_dir}")


if __name__ == "__main__":
    main()
