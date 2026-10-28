# IREB Evaluate Skills

Tests the `ireb-requirements-identifier` skill across agent harnesses and models, and scores the results against a reference answer.

## Input

- `Inputs/Interview_Listen en-US.md`: a transcribed stakeholder interview about lists and tables in a software application, converted unchanged from the original Word file.
- `Inputs/expected-requirement.json`: the reference answer from the IREB AI4RE example. It contains 9 expected requirements, 9 topics the reference explicitly excludes, and a validation summary. The requirements part follows the skill's output schema.

## Test method

1. **Run.** `eval/run_eval.py` starts each harness headless with the same prompt (`eval/prompts/default.txt`). Each run gets a fresh workspace outside the repo containing only the skill and the input. Harnesses, models and effort are set in `eval/config.json`.

   | Harness | Models | Effort |
   |---|---|---|
   | Claude Code | Sonnet 5.5, Opus 5.5, Haiku 5.5 | medium |
   | Cursor | Grok 4.6 | medium |
   | Mistral Vibe | Mistral Medium 3.5, Mistral Large 4 | high (Mistral accepts only high or none) |

   Results from web apps (Claude, Gemini) were added manually as exported answers.

2. **Score.** `eval/score.py` checks each answer and writes a report.
   - Process (CLI runs only, from the transcript): skill loaded, validator run, renderer run.
   - Output: JSON valid against the skill's schema, number of extracted requirements, quotes stitched from fragments.
   - Content: an LLM judge (Claude Opus 5.5, tools disabled) maps each extracted requirement to the expected requirements and excluded topics. The report gives recall over the 9 expected requirements, a comment for each missed one, and counts of extracted items that match an expected requirement, match an excluded topic, or are not in the reference.

## Usage

```
python eval/run_eval.py                                   # all harnesses and models in config.json
python eval/run_eval.py --harness claude --model claude-opus-5-5
python eval/score.py eval/results                         # score all results
python eval/score.py --no-judge eval/results              # without the LLM judge
```

Requires Python 3 and the CLIs being tested (`claude`, `cursor-agent`, `vibe`). The judge uses `claude`.

## Repository map

```
Inputs/
  Interview_Listen en-US.md      interview used as input
  expected-requirement.json      reference answer
Skills/
  ireb-requirements-identifier/  skill under test (SKILL.md, references, schema, scripts)
  ireb-requirements-identifier.zip
.claude/skills/                  copy of the skill for use with Claude Code in this repo
eval/
  config.json                    harnesses, models, effort, repeats
  prompts/default.txt            prompt used for every run
  run_eval.py                    runs the skill in each harness
  score.py                       checks, LLM judge and report
  reference_issues.md            observations on the reference, included in the report
  results/<batch>/<run>/         answer.md per CLI run
  results/WebBased/              answers exported from web apps
  scores/<timestamp>/            report.md, scores.csv, judge details per run
```

Transcripts, run metadata and the original Word file are excluded from the repository because they contain local paths and personal data.

## Latest report

`eval/scores/20261029-094637/report.md`
