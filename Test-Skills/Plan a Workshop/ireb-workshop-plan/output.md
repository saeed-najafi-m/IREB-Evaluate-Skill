# Workshop Plan: Universal TV Remote Control (successor model)

A 90-minute remote workshop (video conference) from 10:00 to 11:30 (start time assumed) with 9 participants. If a conflict cannot be resolved by consensus within the timebox, the product owner decides (decision rule assumed, based on the product owner's role "prioritization decision").

## Workshop Goals

| ID | Goal | Expected result |
|---|---|---|
| WG 1 | Elicit the requirements for the new remote from all stakeholder groups | A list of candidate requirements on the shared whiteboard, each linked to its source (stakeholder group, survey pain point, sales requirement or current button layout) |
| WG 2 | Prioritize the requirements (MoSCoW) and agree the top 5 for the first release | Every candidate requirement classified as Must/Should/Could/Won't; the top 5 for the first release agreed, and checked against the 12-button limit |
| WG 3 | Identify open issues and risks (e.g. battery life vs. features) | A list of open issues and risks, each rated for impact (high/medium/low, assumed scale) and given an owner; mitigation is not worked out in the workshop (scope reduced, see AGD 6) |

## Participants

| ID | Role | Number | Expected contribution |
|---|---|---|---|
| WP 1 | Product owner | 1 | Business goals, scope, prioritization decision; final decision under the decision rule |
| WP 2 | Industrial designer | 1 | Usability, look & feel, hardware constraints (incl. the 12-button limit) |
| WP 3 | End users (diverse households) | 4 | Real usage scenarios, pain points with the current remote |
| WP 4 | Software/firmware engineer | 1 | Technical feasibility, interfaces to TV/soundbar, multi-brand compatibility, power consumption |
| WP 5 | Facilitator (requirements engineer) | 1 | Moderation, techniques, agenda, timekeeping |
| WP 6 | Scribe | 1 | Documentation of decisions, requirements, open issues and risks |

## Preparation

| ID | Task | Timing |
|---|---|---|
| PT 1 | Send the invitation with goals, agenda, decision rule and video-conference/whiteboard links to all participants | 7 working days before (assumed) |
| PT 2 | Prepare the digital whiteboard: one area each for context (5 survey pain points, current button layout, sales requirement, 12-button limit), brainwriting, MoSCoW board with a "Top 5" lane and a 12-button counter, risks/open issues list | 5 working days before (assumed) |
| PT 3 | Send a 1-page pre-read: the 5 survey pain points, a picture of the current remote's button layout and the sales requirement "must work with all TV brands we sell"; ask participants to note their 3 most important wishes or problems | 5 working days before (assumed) |
| PT 4 | Run a 10-minute tech check with the 4 end users (camera, audio, whiteboard access); offer an alternative input channel (chat or scribe) if the whiteboard does not work | 2–3 working days before (assumed) |
| PT 5 | Agree with the product owner on the decision rule, the release scope, and the criteria for the top 5 | 2 working days before (assumed) |
| PT 6 | Agree with the scribe on the documentation template (requirement, source, MoSCoW, decision, risk, owner) | 1 working day before (assumed) |

### Materials

* Video-conference tool with screen sharing, chat and a timer
* Digital whiteboard (prepared areas per PT 2), with digital sticky notes and voting dots
* Pre-read: user survey results (5 pain points), current remote's button layout, sales requirement "must work with all TV brands we sell"
* Visible note of the known constraint: at most 12 physical buttons
* Documentation template for the scribe (PT 6)

## Agenda

| ID | Start | Duration (min) | Title | Technique | Activity | Workshop goals |
|---|---|---|---|---|---|---|
| AGD 1 | 10:00 | 5 | Welcome and frame | – | Facilitator presents goals, agenda, video rules (camera on, raise hand, chat for side remarks) and the decision rule; short round of names and roles | WG 1, WG 2, WG 3 |
| AGD 2 | 10:05 | 10 | Context: what we already know | Document analysis (short presentation of existing documents, so that all start from the same facts) | Facilitator presents the 5 survey pain points, the current button layout, the sales requirement and the 12-button limit; participants ask clarifying questions only | WG 1 |
| AGD 3 | 10:15 | 20 | Elicit requirements | Brainwriting (each person writes ideas silently on own sticky notes, so quiet participants are not drowned out), then round robin (each person presents in turn, 1 minute each) | 8 min silent writing on the whiteboard (one requirement or usage scenario per note, from own pain points and wishes); 12 min round robin, facilitator clusters notes and removes duplicates; scribe records the source of each note | WG 1 |
| AGD 4 | 10:35 | 5 | Break | – | Screen break; facilitator and scribe finish clustering | – |
| AGD 5 | 10:40 | 20 | Prioritize and agree top 5 | MoSCoW (sort each requirement into Must have, Should have, Could have, Won't have this time), supported by dot voting (each person gets 5 digital dots to mark the most important requirements) | 5 min dot voting; 10 min sort clusters into MoSCoW, starting with the most-voted; designer and engineer check each Must against the 12-button limit and feasibility; 5 min agree top 5 for the first release – if no consensus, the product owner decides | WG 2 |
| AGD 6 | 11:00 | 15 | Open issues and risks | Round robin, then impact rating on the whiteboard | Each person names the biggest risk or open question for the top 5 (e.g. battery life vs. features, button count vs. functions, compatibility with all brands sold); group rates impact high/medium/low; each item gets an owner. Mitigation is postponed to follow-up because of time | WG 3 |
| AGD 7 | 11:15 | 5 | Buffer | – | Used for overruns in AGD 3–6, otherwise for remaining open questions | WG 1, WG 2, WG 3 |
| AGD 8 | 11:20 | 10 | Summary and close | – | Scribe reads back the top 5, MoSCoW result, decisions and risks; facilitator explains next steps and the validation; short feedback round (one word each) | WG 1, WG 2, WG 3 |

## Facilitation Tips

| ID | Situation | Recommended action |
|---|---|---|
| FT 1 | Conflict between participants (e.g. designer wants fewer buttons, end users want more direct functions; battery life vs. features) | Make both positions visible on the whiteboard with their reasons and link them to the survey pain points and the 12-button limit; look for a combination (e.g. long-press, app or voice for rare functions); if no agreement within 3 minutes, the product owner decides under the decision rule; scribe records the decision and the rationale |
| FT 2 | Dominant participant (e.g. product owner or engineer steers the discussion, or one end user talks for long) | Refer to the timebox and the round robin; thank them and explicitly hand over to the next person; ask the product owner to give their view last during prioritization so they do not anchor the others |
| FT 3 | Silent participant (often end users, who may feel less expert in a video call) | Rely on silent writing and the round robin; address them by name with a concrete question ("How do you use the remote on a typical evening?"); allow input via chat, which the facilitator reads out |
| FT 4 | Discussion drifts into technical solutions (protocols, chip, app design) | Note the topic in a "parking lot" area of the whiteboard and come back to the requirement ("what should the user be able to do?"); the engineer explains solutions in the follow-up |
| FT 5 | Technical problems in the video call (dropout, whiteboard not working) | Scribe or facilitator writes on the whiteboard for the affected person; catch up on missed content in one sentence after reconnection; use the buffer (AGD 7) if necessary |
| FT 6 | Too many requirements become "Must" | Remind the group of the 12-button limit and the top 5 for the first release; ask "would the release fail without it?"; the product owner decides if needed |

## Follow-up

| ID | Step | Timing |
|---|---|---|
| FS 1 | Scribe completes the minutes: requirements with source, MoSCoW classification, top 5, decisions with rationale, open issues and risks with owner, parking lot | Within 1 working day (assumed) |
| FS 2 | Send the minutes to all participants for validation, asking them to confirm or correct their requirements and the documented decisions | Within 2 working days (assumed) |
| FS 3 | Incorporate the feedback and resolve deviations; conflicts are resolved according to the decision rule (product owner decides) | Within 5 working days (assumed) |
| FS 4 | Risk owners analyze the top risks (e.g. battery life vs. features, compatibility with all brands sold) and propose mitigations | Within 10 working days (assumed) |
| FS 5 | Document the top 5 as requirements in the requirements specification/backlog and check them against the 12-button limit and the sales requirement | Within 10 working days (assumed) |
| FS 6 | Plan a follow-up session for the Should/Could requirements and for risk mitigation, if needed | After FS 4 (assumed) |
