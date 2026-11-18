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
Prompts for Prepare Interview Script: [exploratory interview](Prepare-Interview-Script/ireb-exploratory-interview/prompt.md), [goal confirmation](Prepare-Interview-Script/ireb-goal-confirmation-interview/prompt.md).
Prompt for Identify Requirements (original and improved skill): [Identify-Requirements/ireb-requirements-identifier/prompt.md](Identify-Requirements/ireb-requirements-identifier/prompt.md).
Prompts for the Plan a Workshop retest (skill v1.1.0): [1 complete brief, remote 90 min](Plan%20a%20Workshop/ireb-workshop-plan-v1.1.0/1-ami-remote-90min/prompt.md), [2 without duration and setting](Plan%20a%20Workshop/ireb-workshop-plan-v1.1.0/2-missing-duration-setting/prompt.md), [3 on-site, 6 hours](Plan%20a%20Workshop/ireb-workshop-plan-v1.1.0/3-onsite-full-day/prompt.md).

| Use case | Skill | Example | Model / harness | Date | Verdict |
|---|---|---|---|---|---|
| Summarize Domain | [ireb-actors](Summarize-Domain/ireb-actors) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
| Summarize Domain | [ireb-domain-glossary](Summarize-Domain/ireb-domain-glossary) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
| Summarize Domain | [ireb-domain-overview](Summarize-Domain/ireb-domain-overview) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
| Summarize Domain | [ireb-regulations-and-standards](Summarize-Domain/ireb-regulations-and-standards) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
| Summarize Domain | [ireb-system-context](Summarize-Domain/ireb-system-context) | GOV.UK Notify (web search, no documents) | Opus 5.5, Claude Code CLI | 2026-11-08 | to review |
| Prepare Interview Script | [ireb-exploratory-interview](Prepare-Interview-Script/ireb-exploratory-interview) | NIHR loneliness support, frontline staff, 45 min | Opus 5.5, Claude Code CLI | 2026-11-12 | to review |
| Prepare Interview Script | [ireb-goal-confirmation-interview](Prepare-Interview-Script/ireb-goal-confirmation-interview) | GOV.UK Verify, 3 business-case goals, 60 min | Opus 5.5, Claude Code CLI | 2026-11-12 | to review |
| Identify Requirements | [ireb-requirements-identifier](Identify-Requirements/ireb-requirements-identifier/output.md) (original) | AI4RE interview on lists and tables | Opus 5.5, Claude Code CLI | 2026-11-16 | to review |
| Identify Requirements | [ireb-requirements-identifier-improved](Identify-Requirements/ireb-requirements-identifier/output-improved.md) | AI4RE interview on lists and tables | Opus 5.5, Claude Code CLI | 2026-11-16 | to review |
| Plan a Workshop | [ireb-workshop-plan v1.1.0](Plan%20a%20Workshop/ireb-workshop-plan-v1.1.0/1-ami-remote-90min) | AMI remote control, complete brief, remote, 90 min | Opus 5.5, Claude Code CLI, multi-turn (simulated user: Opus 5.5) | 2026-11-18 | to review |
| Plan a Workshop | [ireb-workshop-plan v1.1.0](Plan%20a%20Workshop/ireb-workshop-plan-v1.1.0/2-missing-duration-setting) | AMI remote control, brief without duration and setting | Opus 5.5, Claude Code CLI, multi-turn (simulated user: Opus 5.5) | 2026-11-18 | to review |
| Plan a Workshop | [ireb-workshop-plan v1.1.0](Plan%20a%20Workshop/ireb-workshop-plan-v1.1.0/3-onsite-full-day) | AMI remote control, complete brief, on-site, 6 hours | Opus 5.5, Claude Code CLI, multi-turn (simulated user: Opus 5.5) | 2026-11-18 | to review |
