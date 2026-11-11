# Prompt for the Plan-a-Workshop quick test

The skill's Input section says to ask the user for the system, participants, workshop goals, and optionally duration, setting and documents before proceeding. The prompt is written for a headless run: there is nobody to answer, so "Do not ask questions" is stated and the whole brief is pasted into the prompt as a text snippet.

Reference: the brief below is a synthetic composite modeled on the remote-control design scenario of the AMI Meeting Corpus (https://huggingface.co/datasets/knkarthick/AMI)

## Exact prompt (single message, brief included as text)

The prompt starts with a one-sentence reference to the brief's source.

```


Use the ireb-workshop-plan skill. Do not ask questions; the system, participants, goals,
duration, setting and documents are all given in the brief below.

--- Brief ---

**System:** a new universal TV remote control for a consumer electronics brand (successor of the
current model; must work with the brand's TVs and the major other brands).

**Workshop goals:**
1. Elicit the requirements for the new remote from all stakeholder groups.
2. Prioritize the requirements (MoSCoW) and agree the top 5 for the first release.
3. Identify open issues and risks (e.g. battery life vs. features).

**Participants (stakeholder list):**
| Role | Number | Expected contribution |
|---|---|---|
| Product owner | 1 | Business goals, scope, prioritization decision |
| Industrial designer | 1 | Usability, look & feel, hardware constraints |
| End users (diverse households) | 4 | Real usage scenarios, pain points with current remote |
| Software/firmware engineer | 1 | Technical feasibility, interfaces to TV/soundbar |
| Facilitator (requirements engineer) | 1 | Moderation, techniques, agenda |
| Scribe | 1 | Documentation of decisions and requirements |

**Duration:** 90 minutes. **Setting:** remote (video conference). **Documents provided:** results of
the user survey (5 pain points), current remote's button layout, sales requirement "must work with
all TV brands we sell".

**Known constraint:** the hardware budget allows at most 12 physical buttons.
```



## Run setup

- Harness: Claude Code CLI, headless (`claude -p`), model `claude-opus-5-5`, effort `medium`.
- The skill ran in a fresh, empty folder outside this repository, containing only the skill under
  `.claude/skills/ireb-workshop-plan/` (copied from
  `Skills/SKILLS-Plan a Workshop/ireb-workshop-plan/ireb-workshop-plan/`). User settings, hooks,
  plugins and MCP servers were not loaded (`--setting-sources project,local --strict-mcp-config`),
  so nothing from this repository or the user's setup could influence the result.
- No documents were attached; the brief above was part of the prompt text.
- The skill's document is saved unedited as `ireb-workshop-plan/output.md`.

