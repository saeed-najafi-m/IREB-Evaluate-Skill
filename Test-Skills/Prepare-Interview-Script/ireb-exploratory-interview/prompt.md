# Prompt for the ireb-exploratory-interview quick test — NIHR loneliness discovery

The skill asks the user for input before proceeding. The run is headless, so the prompt says
"Do not ask questions" and contains the whole brief as text.

Source: NIHR project 128616 "Understanding and using people's experiences of social care to guide
service improvements" (University of Oxford, study protocol V2.0, 14 Dec 2021,
https://njl-admin.nihr.ac.uk/document/download/2038447). The brief paraphrases the protocol's lay
summary and staff-interview section; the protocol text is not copied. The 45 minutes are our choice
within the protocol's 30–60 minute range.

## Exact prompt

```
Use the ireb-exploratory-interview skill. Do not ask questions; everything known is in the brief below.

--- Brief ---

**System:** loneliness support provided by English local-authority, private and voluntary-sector
social care services.

**Domain:** adult social care, service improvement.

**Stakeholder group:** staff who provide or manage support services with a remit to tackle loneliness.

**Interviewee:** one frontline staff member who provides this support (name and employer unknown).

**Organization conducting the interviews:** a university-led research project (name not needed).

**Available time:** 45 minutes, remote (video or telephone), audio recorded with consent.

**Documents provided (summary):**
- Project: local authorities need better ways to collect and use people's experiences of social care
  to improve services. The project adapts a healthcare improvement method: interviews with service
  users and staff are analysed for "touch points" (good care moments and points where services could
  improve); a short film of interview extracts then drives co-design workshops where staff and service
  users agree improvement priorities. Loneliness is the focus.
- Staff interviews: about 20 staff from different regions and backgrounds. The interviews should
  explore how staff understand the way service users experience loneliness, what staff see as
  priorities for improving services, and what gets in the way of providing the best possible support.

Focus on work, people, problems and improvement opportunities, and report your assumptions.
```

## Run setup

- Harness: Claude Code CLI, headless (`claude -p`), model `claude-opus-5-5`, effort `medium`.
- The skill runs in a fresh, empty folder containing only the skill under
  `.claude/skills/ireb-exploratory-interview/`, with `--setting-sources project,local --strict-mcp-config`.
- Save the skill's document unedited as `output.md` in this folder.
