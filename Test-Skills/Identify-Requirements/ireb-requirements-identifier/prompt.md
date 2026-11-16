# Prompt for the ireb-requirements-identifier quick test — interview on lists and tables

Source: stakeholder interview about lists and tables in a software application, from the IREB AI4RE
working group page "Identify Requirements" (retrieved 2026-10-28). It is used unchanged as
[`Inputs/Interview_Listen en-US.md`](../../../Inputs/Interview_Listen%20en-US.md) and given to the
skill as `interview.md`.

## Exact prompt

```
Identify the requirements in interview.md. Return both the rendered result and the JSON.
```

## Run setup

- Harness: Claude Code CLI, headless (`claude -p`), model `claude-opus-5-5`, effort `medium`.
- Each version runs in a fresh, empty folder containing only `interview.md` and the skill under
  `.claude/skills/`, with `--setting-sources project,local --strict-mcp-config`.
- Original skill: `Skills/SKILL-ireb-requirements-identifier/ireb-requirements-identifier/`.
  Improved skill: `Skills/SKILL-ireb-requirements-identifier/Improved_Version/ireb-requirements-identifier-improved/`.
- The skill creates no files; its chat reply (rendered table and JSON) is saved unedited as
  `output.md` (original) and `output-improved.md` (improved).
