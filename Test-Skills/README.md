# Test-Skills

Quick tests of the IREB skills: one example per skill, to share with the team before the full evaluation.
These are not scored evaluations. The scored evaluation of `ireb-requirements-identifier` is in [`../eval/`](../eval).

## Layout

The folders follow the use cases in [`../Skills/`](../Skills): one folder per use case, one subfolder per skill.

```
Test-Skills/
  <Use-Case>/
    <skill>/
      input.md     the exact prompt, the domain and system, and any attached documents
      output.md    the skill's answer, unedited
      notes.md     model, harness, skill version, date, observations
```

## Rules

- Keep `output.md` exactly as the skill produced it. Put comments in `notes.md`.
- If you test a revised skill, add `output-v<version>.md` next to the earlier output instead of overwriting it.
- Only use inputs that may be published: no personal data, and only sources whose licence allows it.

## Tests

Prompt and run setup for Summarize Domain: [Summarize-Domain/prompt.md](Summarize-Domain/prompt.md).

| Use case | Skill | Example | Model / harness | Date | Verdict |
|---|---|---|---|---|---|
| Summarize Domain | [ireb-actors](Summarize-Domain/ireb-actors) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
| Summarize Domain | [ireb-domain-glossary](Summarize-Domain/ireb-domain-glossary) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
| Summarize Domain | [ireb-domain-overview](Summarize-Domain/ireb-domain-overview) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
| Summarize Domain | [ireb-regulations-and-standards](Summarize-Domain/ireb-regulations-and-standards) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
| Summarize Domain | [ireb-system-context](Summarize-Domain/ireb-system-context) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
