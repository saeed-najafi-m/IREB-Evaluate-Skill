#!/usr/bin/env python3
"""Score skill runs against Inputs/expected-requirement.json.

Accepts run folders produced by run_eval.py (anything containing answer.md),
batch folders, or standalone .md answers exported from web apps.

Per run it reports
  * process checks (CLI runs only, from the transcript): skill loaded,
    validator run, renderer run;
  * output checks: schema valid, number of extracted requirements, quotes
    stitched from fragments;
  * judge-based matching: an LLM judge (Opus, called through `claude -p` with all
    tools disabled) maps every extracted requirement to the expected requirements
    (REQ n) and to the topics the reference explicitly excluded (EX n), and
    comments on every expected requirement no extracted item covers.

Output goes to eval/scores/<timestamp>/: report.md, scores.csv and one
<run>.json per run with every judge decision. Judge answers are cached in
eval/scores/cache/ so re-scoring the same answer does not call the judge again.

Usage:
    python eval/score.py eval/results
    python eval/score.py --no-judge eval/results          # process and output checks only
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVAL = REPO / "eval"
SKILL_DIR = REPO / "Skills/ireb-requirements-identifier"
VALIDATOR = SKILL_DIR / "scripts/validate_output.py"
EXPECTED = REPO / "Inputs/expected-requirement.json"
INPUT = REPO / "Inputs/Interview_Listen en-US.md"
REFERENCE_ISSUES = EVAL / "reference_issues.md"

JUDGE_MODEL = "claude-opus-5-5"
JUDGE_EFFORT = "medium"
JUDGE_SYSTEM = """You are a strict, impartial evaluator for requirements engineering.
You compare requirements extracted by a system under test (CANDIDATES) with a reference
list (REFERENCE). The reference has expected requirements (ids "REQ n") and topics that
the reference author deliberately excluded (ids "EX n"). The original interview (SOURCE)
is given for context.

Task 1 - matches. For every candidate decide which reference items it covers:
- A candidate covers a reference item when it expresses the same obligation or topic,
  even with different wording, a different title, or different supporting quotes.
- A candidate may cover several reference items, and several candidates may cover the
  same reference item.
- Partial overlap counts only if the core of the reference item is present.
- List every covered reference item in "covers", REQ ids and EX ids alike. A candidate that
  covers an excluded topic must list that EX id; do not leave it out because it was excluded.
- Return an empty list only if the candidate covers no REQ item and no EX item.
Judge content only. Ignore ids, ordering, formatting, source labels and writing style.
Give a short reason (max 25 words) for each decision.

Task 2 - not covered. For every REQ item that no candidate covers, explain in max 40 words
what the candidates did instead or why the item is absent. Then state whether the reference
item itself may be the cause (for example: not explicitly stated in the SOURCE, describes
an existing feature rather than a new need, or relies on weaker wording than items the
reference excluded) and set possible_reference_issue accordingly."""

JUDGE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["matches", "not_covered"],
    "properties": {
        "matches": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["candidate_id", "covers", "reason"],
                "properties": {
                    "candidate_id": {"type": "string"},
                    "covers": {"type": "array", "items": {"type": "string"}},
                    "reason": {"type": "string"},
                },
            },
        },
        "not_covered": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["reference_id", "comment", "possible_reference_issue"],
                "properties": {
                    "reference_id": {"type": "string"},
                    "comment": {"type": "string"},
                    "possible_reference_issue": {"type": "boolean"},
                },
            },
        },
    },
}

HARNESS_NAMES = {"claude": "Claude Code", "cursor": "Cursor", "vibe": "Mistral Vibe"}
WEB_NOTE = "n/a (web app export, no tool log)"

LEGEND = """\
| Column | Meaning |
|---|---|
| Run | Harness and model that produced the answer. Web app exports are named as stated by the user. |
| Effort | Reasoning effort / thinking level the model ran with. Mistral models accept only `high` or `none`, so Vibe runs use `high`. |
| Skill loaded | The transcript shows the agent loaded the skill (skill tool or a read of `SKILL.md`). |
| Validator run | The transcript shows `scripts/validate_output.py` executed as a shell command. |
| Renderer run | The transcript shows `scripts/render_output.py` executed as a shell command. |
| Schema valid | The JSON in the answer passes the skill's own validator. |
| Extracted | Number of requirements the run extracted. |
| Recall | Expected requirements (of the reference's 9) covered by at least one extracted requirement, divided by 9. |
| Missed | Expected requirements no extracted requirement covers. Each is explained under *Comments per run*. |
| Matches expected | Extracted requirements that cover at least one expected requirement. |
| Matches excluded topic | Extracted requirements that cover none of the expected requirements but a topic the reference explicitly excluded. |
| Not in reference | Extracted requirements that cover neither. Matches expected + Matches excluded topic + Not in reference = Extracted. |
| Stitched quotes | Supporting quotes built from several interview fragments joined with "[...]" or "...". Every fragment was found in the interview. |
"""


# ---------------------------------------------------------------- discovery

def find_runs(paths):
    runs = []
    for p in map(Path, paths):
        if p.is_file() and p.suffix == ".md":
            runs.append((p.parent.name + "__" + p.stem, p, None))
        elif (p / "answer.md").exists():
            runs.append((p.name, p / "answer.md", p))
        elif p.is_dir():
            for ans in sorted(p.rglob("answer.md")):
                runs.append((ans.parent.name, ans, ans.parent))
            for md in sorted(p.rglob("*.md")):
                if md.name != "answer.md" and not (md.parent / "transcript.jsonl").exists():
                    runs.append((md.parent.name + "__" + md.stem, md, None))
    return runs


# ---------------------------------------------------------------- display names

def model_display(model):
    if model.startswith("claude-"):
        parts = model.split("-")[1:]
        return f"{parts[0].title()} {'.'.join(parts[1:])}"
    model = re.sub(r"^cursor-", "", model)
    model = re.sub(r"-(none|low|medium|high|xhigh|max)$", "", model)
    return " ".join(w.title() if w.isalpha() else w for w in model.split("-"))


def run_identity(answer_path, meta):
    if meta:
        harness = HARNESS_NAMES.get(meta["harness"], meta["harness"])
        model = model_display(meta["model_requested"])
        effort = str(meta.get("effort", "")).split()[0] if meta.get("effort") else ""
        if meta["harness"] == "cursor":
            m = re.search(r"-(none|low|medium|high|xhigh|max)$", meta["model_requested"])
            effort = m.group(1) if m else effort
        return f"{harness} · {model}", effort
    stem = re.sub(r"^result_", "", answer_path.stem)
    return f"Web app export · {' '.join(w.capitalize() for w in stem.split('_'))}", "not reported"


# ---------------------------------------------------------------- deterministic checks

def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def extract_json(answer):
    for block in reversed(re.findall(r"```json\s*(\{.*?\})\s*```", answer, re.S)):
        try:
            return json.loads(block)
        except ValueError:
            continue
    return None


def schema_valid(doc, tmp_dir):
    tmp = tmp_dir / "_candidate.json"
    tmp.write_text(json.dumps(doc), encoding="utf-8")
    proc = subprocess.run([sys.executable, "-I", str(VALIDATOR), str(tmp)],
                          capture_output=True, text=True)
    tmp.unlink()
    return proc.returncode == 0


def is_stitched(statement, source_norm):
    if norm(statement) in source_norm:
        return False
    parts = [p for p in re.split(r"\[\s*(?:\.\.\.|…)\s*\]|\.\.\.|…", statement) if norm(p)]
    return len(parts) > 1 and all(norm(p) in source_norm for p in parts)


def tool_calls(run_dir):
    """List of (tool, text) from a run_eval transcript, any harness."""
    if run_dir is None or not (run_dir / "transcript.jsonl").exists():
        return None
    calls = []
    for line in (run_dir / "transcript.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        # claude: assistant messages with tool_use parts
        message = e.get("message")
        for part in message.get("content", []) if isinstance(message, dict) else []:
            if isinstance(part, dict) and part.get("type") == "tool_use":
                calls.append((part.get("name", ""), json.dumps(part.get("input", {}))))
        # cursor: tool_call started events
        if e.get("type") == "tool_call" and e.get("subtype") == "started":
            for name, body in (e.get("tool_call") or {}).items():
                if name.endswith("ToolCall") and isinstance(body, dict):
                    calls.append((name, json.dumps(body.get("args", {}))))
        # vibe: effect entries
        if e.get("type") == "effect":
            detail = e.get("detail") or {}
            calls.append((e.get("title", ""), json.dumps(detail.get("input", {})) + " " +
                          json.dumps(detail.get("display", {}))))
    return calls


def process_checks(run_dir):
    calls = tool_calls(run_dir)
    if calls is None:
        return {"skill_loaded": WEB_NOTE, "validator_run": WEB_NOTE, "renderer_run": WEB_NOTE}
    shell = [t for n, t in calls if re.search(r"bash|shell|powershell", n, re.I)]
    skill = any(("ireb-requirements-identifier" in t and re.search(r"skill", n, re.I))
                or "SKILL.md" in t for n, t in calls)
    yes_no = lambda b: "Yes" if b else "No"
    return {
        "skill_loaded": yes_no(skill),
        "validator_run": yes_no(any("validate_output.py" in t for t in shell)),
        "renderer_run": yes_no(any("render_output.py" in t for t in shell)),
    }


# ---------------------------------------------------------------- judge

def reference_items(expected):
    items = [{"id": r["id"], "title": r["title"], "statements": [s["statement"] for s in r["statements"]]}
             for r in expected["reference_output"]["original_requirements"]]
    items += [{"id": f"EX {i}", "title": ex["topic"], "statements": [ex["source_modality"]]}
              for i, ex in enumerate(expected["excluded_statements"]["items"], 1)]
    return items


def judge(candidates, references, source_text, cache_dir):
    payload = {
        "SOURCE": source_text,
        "REFERENCE": references,
        "CANDIDATES": [{"candidate_id": c["id"], "title": c["title"],
                        "statements": [s["statement"] for s in c["statements"]]}
                       for c in candidates],
    }
    prompt = ("Do task 1 and task 2.\n\n" + json.dumps(payload, indent=1, ensure_ascii=False))
    key = hashlib.sha256((JUDGE_MODEL + JUDGE_EFFORT + JUDGE_SYSTEM + prompt).encode()).hexdigest()[:16]
    cache = cache_dir / f"{key}.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))

    argv = [shutil.which("claude"), "-p", "--model", JUDGE_MODEL, "--effort", JUDGE_EFFORT,
            "--system-prompt", JUDGE_SYSTEM, "--tools", "", "--setting-sources", "",
            "--strict-mcp-config", "--no-session-persistence", "--no-chrome",
            "--output-format", "json", "--json-schema", json.dumps(JUDGE_SCHEMA)]
    proc = subprocess.run(argv, input=prompt, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=900)
    if proc.returncode != 0:
        raise RuntimeError(f"judge failed ({proc.returncode}): {proc.stderr[:500] or proc.stdout[:500]}")
    envelope = json.loads(proc.stdout)
    result = envelope.get("structured_output")
    if result is None:
        text = envelope.get("result", "")
        result = json.loads(text[text.find("{"):text.rfind("}") + 1])
    # Claude Code may also use a small model for background tasks, so keep the
    # full per-model usage to confirm the judge model did the work.
    usage = {m: {"input": u.get("inputTokens"), "output": u.get("outputTokens")}
             for m, u in (envelope.get("modelUsage") or {}).items()}
    result["_judge"] = {"model": JUDGE_MODEL, "effort": JUDGE_EFFORT, "model_usage": usage}
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(result, indent=1), encoding="utf-8")
    return result


def match_metrics(result, candidates, references):
    expected_ids = [r["id"] for r in references if r["id"].startswith("REQ")]
    titles = {r["id"]: r["title"] for r in references}
    covers = {m["candidate_id"]: [c for c in m["covers"] if c in titles] for m in result["matches"]}
    reasons = {m["candidate_id"]: m["reason"] for m in result["matches"]}
    covered = {ref for refs in covers.values() for ref in refs}
    comments = {n["reference_id"]: n for n in result.get("not_covered", [])}

    matches_expected, matches_excluded, not_in_reference = [], [], []
    for c in candidates:
        refs = covers.get(c["id"], [])
        if any(r.startswith("REQ") for r in refs):
            matches_expected.append(c)
        elif refs:
            matches_excluded.append((c, refs))
        else:
            not_in_reference.append(c)

    missed = []
    for ref in expected_ids:
        if ref not in covered:
            note = comments.get(ref, {})
            missed.append({"id": ref, "title": titles[ref],
                           "comment": note.get("comment", "The judge gave no comment."),
                           "possible_reference_issue": note.get("possible_reference_issue")})
    return {
        "recall": f"{len(expected_ids) - len(missed)}/{len(expected_ids)}",
        "recall_value": round((len(expected_ids) - len(missed)) / len(expected_ids), 3),
        "missed": missed,
        "matches_expected": len(matches_expected),
        "matches_excluded_topic": len(matches_excluded),
        "not_in_reference": len(not_in_reference),
        "excluded_details": [{"id": c["id"], "title": c["title"],
                              "topics": [f"{r} {titles[r]}" for r in refs]} for c, refs in matches_excluded],
        "not_in_reference_details": [{"id": c["id"], "title": c["title"], "reason": reasons.get(c["id"], "")}
                                     for c in not_in_reference],
    }


# ---------------------------------------------------------------- per run

def score_run(name, answer_path, run_dir, references, source_text, out_dir, use_judge):
    meta = {}
    if run_dir and (run_dir / "meta.json").exists():
        meta = json.loads((run_dir / "meta.json").read_text(encoding="utf-8"))
    label, effort = run_identity(answer_path, meta)
    row = {"run": label, "effort": effort}
    row.update(process_checks(run_dir))
    detail = {"run": label, "answer": answer_path.resolve().relative_to(REPO).as_posix()}

    doc = extract_json(answer_path.read_text(encoding="utf-8"))
    if doc is None:
        row["schema_valid"] = "No JSON found"
        return row, detail
    row["schema_valid"] = "Yes" if schema_valid(doc, out_dir) else "No"
    candidates = doc.get("original_requirements", [])
    source_norm = norm(source_text)
    row["extracted"] = len(candidates)
    row["stitched_quotes"] = sum(is_stitched(s.get("statement", ""), source_norm)
                                 for c in candidates for s in c.get("statements", []))

    if use_judge:
        result = judge(candidates, references, source_text, EVAL / "scores" / "cache")
        metrics = match_metrics(result, candidates, references)
        row.update({k: metrics[k] for k in ("recall", "recall_value", "matches_expected",
                                            "matches_excluded_topic", "not_in_reference")})
        row["missed"] = " ".join(m["id"] for m in metrics["missed"]) or "none"
        detail.update(metrics)
        detail["judge"] = result
    detail["row"] = row
    return row, detail


# ---------------------------------------------------------------- report

def skill_version():
    match = re.search(r"^version:\s*(\S+)", (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"), re.M)
    return match.group(1) if match else "unknown"


def write_report(rows, details, expected, path, use_judge):
    meta = expected["meta"]
    lines = [
        "# Skill test report: ireb-requirements-identifier", "",
        f"- **Skill:** `{SKILL_DIR.relative_to(REPO).as_posix()}`, version {skill_version()}",
        f"- **Input:** `{INPUT.relative_to(REPO).as_posix()}`",
        f"- **Reference:** `{EXPECTED.relative_to(REPO).as_posix()}`: 9 expected requirements and "
        f"9 explicitly excluded topics, generated by {meta['generated_by']}, "
        f"retrieved {meta['retrieved']}.",
        f"- **Judge:** {JUDGE_MODEL}, effort {JUDGE_EFFORT}, tools disabled. Each answer is judged once."
        if use_judge else "- **Judge:** not used (process and output checks only).",
        f"- **Date:** {dt.date.today().isoformat()}", "",
        "## Results", "",
    ]
    cols = [("Run", "run"), ("Effort", "effort"), ("Skill loaded", "skill_loaded"),
            ("Validator run", "validator_run"), ("Renderer run", "renderer_run"),
            ("Schema valid", "schema_valid"), ("Extracted", "extracted")]
    if use_judge:
        cols += [("Recall", "recall"), ("Missed", "missed"), ("Matches expected", "matches_expected"),
                 ("Matches excluded topic", "matches_excluded_topic"), ("Not in reference", "not_in_reference")]
    cols += [("Stitched quotes", "stitched_quotes")]
    lines += ["| " + " | ".join(c for c, _ in cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        lines.append("| " + " | ".join(str(r.get(k, "")) for _, k in cols) + " |")

    lines += ["", "## Legend", "", LEGEND]
    if use_judge:
        lines += ["Judge decisions vary slightly between calls. In a repeat judgment of the same answer, "
                  "one of 19 decisions changed, so treat differences of one item as noise.", ""]

        lines += ["## Comments per run", ""]
        for d in details:
            if "missed" not in d:
                continue
            lines += [f"### {d['run']}", ""]
            if d["missed"]:
                lines.append("**Missed expected requirements**")
                for m in d["missed"]:
                    flag = {True: "yes", False: "no", None: "not stated"}[m["possible_reference_issue"]]
                    lines.append(f"- {m['id']} ({m['title']}): {m['comment']} "
                                 f"*Possible reference issue: {flag}.*")
                lines.append("")
            else:
                lines += ["All 9 expected requirements covered.", ""]
            if d["excluded_details"]:
                lines.append("**Extracted topics the reference excluded**")
                for x in d["excluded_details"]:
                    lines.append(f"- {x['id']} ({x['title']}) → {', '.join(x['topics'])}")
                lines.append("")
            if d["not_in_reference_details"]:
                lines.append("**Extracted requirements not in the reference**")
                for x in d["not_in_reference_details"]:
                    lines.append(f"- {x['id']} ({x['title']}): {x['reason']}")
                lines.append("")

    if REFERENCE_ISSUES.exists():
        lines += [REFERENCE_ISSUES.read_text(encoding="utf-8").strip(), ""]
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="run folders, batch folders or .md answers")
    ap.add_argument("--no-judge", action="store_true", help="process and output checks only")
    args = ap.parse_args()

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    references = reference_items(expected)
    source_text = INPUT.read_text(encoding="utf-8")
    out_dir = EVAL / "scores" / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir.mkdir(parents=True)

    rows, details = [], []
    for name, answer_path, run_dir in find_runs(args.paths):
        print(f"[score] {name}", flush=True)
        try:
            row, detail = score_run(name, answer_path, run_dir, references, source_text,
                                    out_dir, not args.no_judge)
        except Exception as exc:  # noqa: BLE001 - keep scoring the other runs
            print(f"      error: {exc}")
            row, detail = {"run": name, "error": str(exc)}, {"run": name, "error": str(exc)}
        rows.append(row)
        details.append(detail)
        (out_dir / f"{name}.json").write_text(json.dumps(detail, indent=1, ensure_ascii=False),
                                              encoding="utf-8")

    fields = []
    for r in rows:
        fields += [k for k in r if k not in fields]
    with open(out_dir / "scores.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    write_report(rows, details, expected, out_dir / "report.md", not args.no_judge)
    print(f"scores: {out_dir}")


if __name__ == "__main__":
    main()
