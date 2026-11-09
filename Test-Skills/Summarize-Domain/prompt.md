# Prompt for the Summarize-Domain quick tests

The same prompt was used for all five skills. Only the skill name changes.

```
Use the {skill} skill. Domain: UK public-sector service communications. System: GOV.UK Notify.
Do not ask questions; the domain and system are given above and there are no documents. Use web search.
```

`{skill}` is one of `ireb-actors`, `ireb-domain-glossary`, `ireb-domain-overview`, `ireb-regulations-and-standards`, `ireb-system-context`.

The second line is needed for a headless run: each skill's Input section says to ask the user before proceeding, and there is nobody to answer.

## Run setup

- Harness: Claude Code CLI, headless (`claude -p`), model `claude-opus-5-5`, effort `medium`.
- Each skill ran in its own fresh, empty folder outside this repository, containing only that skill under `.claude/skills/`. User settings, hooks, plugins and MCP servers were not loaded (`--setting-sources project,local --strict-mcp-config`), so nothing from this repository or the user's setup could influence the result.
- Example: GOV.UK Notify, the UK government service that public-sector teams use to send emails, text messages and letters (https://www.notifications.service.gov.uk). No documents were attached; the skills researched it with web search.
- Each skill's document was saved unedited as `output.md` in its folder.
