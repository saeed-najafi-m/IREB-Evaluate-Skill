# Prompt for the Plan-a-Workshop retest, skill v1.1.0, variant 1: complete brief (remote, 90 min)

Reference: the brief below is a synthetic composite modeled on the remote-control design scenario of the AMI Meeting Corpus (https://huggingface.co/datasets/knkarthick/AMI)

## Exact prompt (single message, brief included as text)

```
Use the ireb-workshop-plan skill to plan a workshop for the brief below.

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

## Simulated user's card

```
Facts you know: only what is in your first message (the brief). You have nothing to add.

Behaviour: cooperative. If asked about anything not in the brief, say you have no preference.
If asked to confirm before the assistant continues, confirm.
```

## Run setup

- Runner: `eval/run_multiturn.py`, scenario `eval/ireb-workshop-plan/scenarios/1-ami-remote-90min/`, one run.
- Skill agent: Claude Code CLI, headless, model `claude-opus-5-5`, effort `medium`, in a fresh, empty
  folder outside this repository containing only the skill under `.claude/skills/ireb-workshop-plan/`
  (copied from `Skills/SKILLS-Plan a Workshop/ireb-workshop-plan-v1.1.0/ireb-workshop-plan/`).
  `--setting-sources project,local --strict-mcp-config`.
- Simulated user: a second Claude Code session, model `claude-opus-5-5`, effort `medium`, no tools or
  skills. If the skill asks something, it answers only what was asked, from the card above; the
  answer goes back into the same skill session. At most 4 turns.
- `output.md`: the skill's document, unedited. `transcript.md`: the whole conversation, unedited except
  that the temporary workspace path is replaced by `<workspace>`.
