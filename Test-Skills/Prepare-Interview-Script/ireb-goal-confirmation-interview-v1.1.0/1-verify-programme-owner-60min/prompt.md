# Prompt for the ireb-goal-confirmation-interview retest, skill v1.1.0: GOV.UK Verify, programme owner, 60 min

Source: National Audit Office, *Investigation into Verify*, HC 1926, 5 March 2019, paragraph 1.7
(https://www.nao.org.uk/wp-content/uploads/2019/03/Investigation-into-verify.pdf). NAO permits
non-commercial reproduction with attribution. The goals are the NAO's account of the 2015/2016
business-case targets, not the business cases themselves.
The interviewee, 60 minutes and two main goals are our choices.

## Exact prompt

```
Use the ireb-goal-confirmation-interview skill. Everything known is in the brief below.

--- Brief ---

**System:** GOV.UK Verify, the UK government's online identity verification service.

**Domain:** government online identity verification.

**Interviewee:** the Government Digital Service (GDS) programme owner responsible for Verify's
delivery and its adoption across government departments (name unknown).

**Organization:** Government Digital Service, Cabinet Office.

**Main goals to agree on:** 2.

**Available time:** 60 minutes.

**Document with the previously collected goals** (the business-case targets, as later reported):

> Verify's performance can be assessed against the expectations set out in the programme's
> business cases for service and user take-up:
> - Number of users who have signed up to use Verify: In both the 2015 and 2016 business cases,
>   GDS forecast that 25 million people would use Verify by 2020.
> - Number of government services that use Verify: The 2016 business case expected 46 services to
>   connect to Verify by March 2018.
> - Verification success rate: This measures the proportion of people who can sign up for a Verify
>   user account having had their identities successfully confirmed by a provider. The 2015 business
>   case states the verification success rate should be 90%.

Do not assume that the targets were achieved or are still appropriate, and report your assumptions.
```

## Simulated user's card

```
Facts you know: only what is in your first message (the brief). You have nothing to add.

Behaviour: cooperative. If asked about anything not in the brief, say you have no preference.
If asked to confirm before the assistant continues, confirm.
```

## Run setup

- Runner: `eval/run_multiturn.py`, scenario `eval/ireb-goal-confirmation-interview/scenarios/1-verify-programme-owner-60min/`, one run.
- Skill agent: Claude Code CLI, headless, model `claude-opus-5-5`, effort `medium`, in a fresh, empty
  folder outside this repository containing only the skill under `.claude/skills/ireb-goal-confirmation-interview/`
  (copied from `Skills/SKILLS-Prepare-Interview-Script/ireb-goal-confirmation-interview-v1.1.0/ireb-goal-confirmation-interview/`).
  `--setting-sources project,local --strict-mcp-config`.
- Simulated user: a second Claude Code session, model `claude-opus-5-5`, effort `medium`, no tools or
  skills. If the skill asks something, it answers only what was asked, from the card above; the
  answer goes back into the same skill session. At most 4 turns.
- `output.md`: the skill's document, unedited. `transcript.md`: the whole conversation, unedited except
  that the temporary workspace path is replaced by `<workspace>`.
