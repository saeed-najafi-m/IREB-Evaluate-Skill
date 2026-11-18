# Workshop Plan: Universal TV Remote Control (successor model)

On-site requirements workshop in a company meeting room, 6 hours from 09:00 to 15:00 (start time assumed), with 9 participants including facilitator and scribe. Decision rule (assumed): consensus, and the product owner decides if no consensus is reached.

## Workshop Goals

| ID | Goal | Expected result |
|---|---|---|
| WG 1 | Elicit the requirements for the new remote from all stakeholder groups | A consolidated, categorized list of requirements (functions, usability/ergonomics, compatibility, power/battery, look & feel). Each requirement records its source stakeholder and the survey pain point it addresses, if any. |
| WG 2 | Prioritize the requirements (MoSCoW) and agree the top 5 for the first release | Every requirement has a MoSCoW category. The top 5 for the first release are agreed (by consensus or a PO decision) and checked against the 12-physical-button limit. |
| WG 3 | Identify open issues and risks (e.g. battery life vs. features) | A list of open issues and risks, each with a description, affected requirements, an owner, and a due date (assumed format). |

## Participants

| ID | Role | Number | Expected contribution |
|---|---|---|---|
| WP 1 | Product owner | 1 | Business goals and scope. Makes the prioritization decision when no consensus is reached. |
| WP 2 | Industrial designer | 1 | Usability, look & feel, and hardware constraints (12-button limit, form factor) |
| WP 3 | End users (diverse households) | 4 | Real usage scenarios and pain points with the current remote |
| WP 4 | Software/firmware engineer | 1 | Technical feasibility, interfaces to TV/soundbar, multi-brand compatibility, power consumption |
| WP 5 | Facilitator (requirements engineer) | 1 | Moderation, techniques, agenda, time-keeping |
| WP 6 | Scribe | 1 | Documents decisions, requirements, open issues, and photos of the boards |

## Preparation

| ID | Task | Timing |
|---|---|---|
| PT 1 | Recruit the 4 end users so that the households are diverse (e.g. older person or person with visual/motor impairment, family with children, tech-savvy single, multi-device household with soundbar/streaming). Arrange compensation, consent/NDA, and travel. | 3 weeks before (assumed) |
| PT 2 | Book the meeting room (wall space, group tables, accessible) and catering. Send invitations with goals, agenda, decision rule, and the start/end time. | 2 weeks before (assumed) |
| PT 3 | Ask sales to supply the concrete list behind "must work with all TV brands we sell". Agree with the PO which "major other brands" are in scope. | 2 weeks before (assumed) |
| PT 4 | With the firmware engineer, prepare a one-page fact sheet: supported control protocols (e.g. IR code libraries, HDMI-CEC, Bluetooth/RF), rough power consumption per feature, and known compatibility limits | 1 week before (assumed) |
| PT 5 | Send a pre-read to all participants: a one-page summary of the 5 survey pain points and the current remote's button layout. Ask end users to bring their own remote(s) or a photo of their TV setup. | 1 week before (assumed) |
| PT 6 | Prepare posters: the 5 pain points, the current button layout enlarged, a category wall for clustering, a MoSCoW board, an issue & risk board, a parking lot, and a "12-button budget" template (outline of a remote with 12 empty slots) | 2 days before (assumed) |
| PT 7 | Prepare props: several current remotes, 2–3 competitor universal remotes, cardboard/foam remote blanks, and 12 button stickers per group | 2 days before (assumed) |
| PT 8 | Brief the scribe on the requirements template (ID, statement, source, pain point, category, MoSCoW, notes), the issue template (ID, description, affected requirements, owner, due date), and photo documentation | 1 day before (assumed) |
| PT 9 | Set up the room: group tables, hang the posters, lay out the props, test the projector, put the agenda and ground rules on display | 45 min before start (assumed) |

### Materials

* Posters: 5 survey pain points, current button layout (enlarged), category wall, MoSCoW board, issue & risk board, parking lot, agenda, ground rules
* "12-button budget" templates (one per group, plus one large version for the plenary)
* Current remote (several units), 2–3 competitor universal remotes, cardboard/foam remote blanks, button stickers (12 per set)
* Sticky notes in 3 colors (requirements, issues/risks, questions), markers, dot stickers (5 per person for dot voting), masking tape
* Printed handouts: pre-read (pain points, button layout), firmware fact sheet, sales compatibility list
* Requirements and issue templates (laptop for the scribe), camera/phone for board photos
* Projector/screen, timer, bell or chime for time signals
* Name tags, water, snacks, catering for lunch

## Agenda

| ID | Start | Duration (min) | Title | Technique | Activity | Workshop goals |
|---|---|---|---|---|---|---|
| AGD 1 | 09:00 | 15 | Welcome and kick-off | Round robin: each person speaks in turn, briefly, without interruption | The PO presents the business goal and scope (successor model, brand TVs plus major other brands). The facilitator presents the goals, agenda, ground rules, decision rule, and known constraints (max. 12 physical buttons, sales compatibility requirement). Round robin introductions: name, role, "the TV setup I use at home". | WG 1, WG 2, WG 3 |
| AGD 2 | 09:15 | 30 | Pain points and current remote | Document review plus show and tell: participants handle the real artifact and explain what they do with it | The facilitator presents the 5 survey pain points and the current button layout. End users demonstrate on the current remote how they use it and where it fails. Everyone adds their own pain points and wishes on sticky notes next to the pain-point poster. | WG 1 |
| AGD 3 | 09:45 | 45 | Usage scenarios | Scenario walk-through in mixed groups: a group plays through a concrete situation step by step (e.g. "Saturday evening: switch from TV to streaming with soundbar volume", "grandparent finds the subtitles", "remote lost under the sofa") | Two mixed groups, each with 2 end users and the designer or the engineer. Each group walks through 3–4 scenarios with the current remote and writes down needed functions, problems, and conditions as requirement sticky notes. Short presentation per group. (Includes 5 min buffer.) | WG 1 |
| AGD 4 | 10:30 | 15 | Break | – | – | – |
| AGD 5 | 10:45 | 50 | Generate and cluster requirements | Brainwriting: everyone writes ideas silently on sticky notes first, then reads the others' notes and builds on them. Affinity clustering: the group sorts the notes by similarity into categories. | 10 min silent brainwriting by everyone, including the PO, designer, and engineer, based on pain points and scenarios. Notes are read aloud and placed on the category wall (functions, usability/ergonomics, compatibility, power/battery, look & feel, other). Merge duplicates and name the clusters. The scribe records each requirement with its source. (Includes 10 min buffer.) | WG 1 |
| AGD 6 | 11:35 | 40 | Consolidate and check feasibility | Requirements walk-through with traffic-light marking (green = feasible, yellow = unclear, red = conflicts with a constraint) | Walk through the clusters together. The engineer and the designer mark feasibility and conflicts with the 12-button limit and the multi-brand requirement. Reformulate vague notes as testable requirements. Unclear points and conflicts (e.g. battery life vs. backlight/voice/Bluetooth) go to the issue & risk board. (Includes 5 min buffer.) | WG 1, WG 3 |
| AGD 7 | 12:15 | 45 | Lunch break | – | – | – |
| AGD 8 | 13:00 | 45 | MoSCoW prioritization | MoSCoW: each requirement is classified as Must have, Should have, Could have, or Won't have (this release). Dot voting first: each participant places 5 dots on the requirements most important to them, to make preferences visible before discussing. | Brief standing recap of the morning (energizer after lunch). Dot voting, with end users voting first so they are not influenced. Then go through the requirements cluster by cluster, starting with those with the most dots, and assign MoSCoW categories on the board. Guideline: at most about 60 % of the effort in Must. Unresolved disagreements follow the decision rule. (Includes 5 min buffer.) | WG 2 |
| AGD 9 | 13:45 | 25 | Top 5 for the first release | 12-button budget: groups place the Must requirements on a remote blank with only 12 button stickers and decide which functions need a physical button and which can use other means (long press, on-screen menu, app). Fist of five: everyone shows 0–5 fingers to show agreement, and anyone showing ≤ 2 explains their concern. | Two groups build a button-budget mock-up each and present it. Derive the top 5 candidates from the Must list together. Check consensus with fist of five. If there is no consensus after one round of discussion, the PO decides and the rationale is recorded. (Includes 5 min buffer.) | WG 2, WG 3 |
| AGD 10 | 14:10 | 20 | Open issues and risks | Pre-mortem: participants imagine the new remote has failed in the market one year after launch and write down why | 5 min silent writing of failure reasons, then add them to the issue & risk board alongside the items from AGD 6. Rate each issue/risk roughly by impact and likelihood (high/medium/low). Assign an owner and due date to each high-rated item (e.g. a battery life feasibility check, the compatibility list for "all TV brands we sell"). | WG 3 |
| AGD 11 | 14:30 | 15 | Break | – | – | – |
| AGD 12 | 14:45 | 15 | Wrap-up and next steps | Round robin | The scribe reads back the top 5, the MoSCoW results, PO decisions, and open issues with owners. Review the parking lot. The facilitator explains the follow-up and the validation process. Feedback round: one sentence per person ("What I take away…"). Thank the participants. | WG 1, WG 2, WG 3 |

## Facilitation Tips

| ID | Situation | Recommended action |
|---|---|---|
| FT 1 | Conflict between stakeholders, e.g. end users want more direct buttons, but the designer insists on the 12-button limit, or the engineer warns that features drain the battery | Make the conflict visible on the board and focus on the underlying needs instead of positions ("What problem does this button solve?"). Look for alternatives (long press, on-screen menu, app). If there is no consensus after one timeboxed discussion, apply the decision rule: the PO decides, and the scribe records the decision and its rationale. |
| FT 2 | Dominant participant, e.g. the PO or the engineer steers the discussion or dismisses end user input as "not feasible" | Use the silent techniques (brainwriting, dot voting with end users first) and round robin. Remind everyone of the ground rule "first collect, then evaluate". Ask the PO to share their view last in prioritization. Address the person directly and politely: "Thanks, let's hear the others first." |
| FT 3 | Silent participants, especially end users who feel intimidated by experts or the brand | Put them in small mixed groups. Use silent writing before discussion. Ask them directly by name with open, scenario-based questions ("How does it work at your place on a Saturday evening?"). Point out that their everyday experience is the key input. |
| FT 4 | Participants jump to solutions or technology ("we need voice control", "use Bluetooth") | Ask "Why?" and "What should be possible then?" to capture the underlying need as the requirement. Record the solution idea as a note attached to it. |
| FT 5 | Technical jargon from the engineer or designer (e.g. "CEC", "IR learning", "mAh") | Ask for a one-sentence explanation in everyday terms. Add terms to a small glossary poster. |
| FT 6 | Off-topic or out-of-scope discussion (e.g. TV menu design, pricing, the app ecosystem) | Acknowledge it and put it on the parking lot. Review the parking lot in the wrap-up and assign owners where needed. |
| FT 7 | Criticism of the current remote makes the designer or PO defensive | Frame it at the start: criticism of the product is the most valuable input, not criticism of people. Thank people for specific pain points. |
| FT 8 | An agenda item runs over time | Use the buffer built into that item first. If it is used up, timebox the discussion, record the remaining points as open issues, and resolve them in the follow-up rather than cutting the prioritization or the risk session. |
| FT 9 | Energy dip after lunch | Start AGD 8 standing at the boards, use physical activities (dot voting, button stickers), and keep the room ventilated. |

## Follow-up

| ID | Step | Timing |
|---|---|---|
| FS 1 | The scribe writes the protocol: the requirements list with source, category, and MoSCoW; the top 5 with rationale; PO decisions; the issue & risk list; the parking lot; and photos of all boards and mock-ups | Within 2 working days (assumed) |
| FS 2 | Send the protocol to all participants for validation, with a feedback deadline. Ask specifically whether each person's requirements are captured correctly. | Within 3 working days; feedback within 1 week (assumed) |
| FS 3 | Incorporate the corrections. Resolve any remaining disagreements with the decision rule (the PO decides) and send the final version to all participants. | Within 2 weeks (assumed) |
| FS 4 | Track the open issues and risks with their owners, e.g. a battery life vs. feature feasibility check, the confirmed compatibility list of TV brands, and the 12-button layout draft | According to the due dates set in AGD 10 |
| FS 5 | Validate the top 5 and the button layout with additional end users, e.g. in a short prototype or paper mock-up test | Before release planning (assumed) |
| FS 6 | Thank the end users, arrange compensation, and tell them how their input was used | Within 2 weeks (assumed) |
