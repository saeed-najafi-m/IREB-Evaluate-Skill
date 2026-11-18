# Workshop Plan: Universal TV Remote Control (Successor Model)

90-minute remote requirements workshop (video conference) from 09:00 to 10:30 (start time assumed) with 9 participants. Decision rule (assumed): consensus; if no consensus is reached, the product owner decides.

## Workshop Goals

| ID | Goal | Expected result |
|---|---|---|
| WG 1 | Elicit the requirements for the new remote from all stakeholder groups | Consolidated list of requirements, clustered by usage scenario and traced to the 5 survey pain points, with source stakeholder noted |
| WG 2 | Prioritize the requirements (MoSCoW) and agree the top 5 for the first release | Every requirement classified as Must / Should / Could / Won't (this release); agreed top 5 for release 1, checked against the limit of 12 physical buttons |
| WG 3 | Identify open issues and risks (e.g. battery life vs. features) | Risk and open-issue list, each item with a short description, an owner, and a due date for clarification |

## Participants

| ID | Role | Number | Expected contribution |
|---|---|---|---|
| WP 1 | Product owner | 1 | Business goals, scope, prioritization decision; decides if no consensus is reached; represents the sales requirement "must work with all TV brands we sell" (assumed, as sales is not present) |
| WP 2 | Industrial designer | 1 | Usability, look & feel, hardware constraints (incl. the 12-button limit, battery, form factor) |
| WP 3 | End users (diverse households) | 4 | Real usage scenarios, pain points with the current remote; mix assumed to cover e.g. an older user, a family with children, a multi-device household (TV + soundbar + streaming), and a user with limited vision or dexterity |
| WP 4 | Software/firmware engineer | 1 | Technical feasibility, interfaces to TV/soundbar, multi-brand compatibility (IR/CEC/Bluetooth), power consumption |
| WP 5 | Facilitator (requirements engineer) | 1 | Moderation, techniques, agenda, timekeeping, whiteboard preparation |
| WP 6 | Scribe | 1 | Documentation of decisions, requirements, risks, and open issues directly on the whiteboard and in the minutes; monitors the chat |

## Preparation

| ID | Task | Timing |
|---|---|---|
| PT 1 | Send the invitation with the goals, agenda, video-conference link, whiteboard link, decision rule, and the request to keep cameras on where possible | 10 working days before (assumed) |
| PT 2 | Recruit and confirm the 4 end users so that the households are diverse (age, household size, devices, accessibility needs); clarify incentives and consent to recording/notes | 10 working days before |
| PT 3 | Send a pre-read (max. 2 pages): the 5 survey pain points, the current remote's button layout, the sales requirement, and the 12-button constraint, written in plain language for end users | 5 working days before |
| PT 4 | Prepare the digital whiteboard with one frame per agenda item: AGD 1 welcome/goals/rules; AGD 2 pain points, current layout, constraints; AGD 3 brainwriting columns per usage scenario (e.g. watching TV, switching sources/streaming, sound via soundbar, setup and pairing, finding the remote/at night) with one colour of sticky notes per participant; AGD 4 clustering area; AGD 5 MoSCoW board with four columns and a "12-button counter"; AGD 7 dot-voting area; AGD 8 risk/open-issue board (permanent "parking lot" visible throughout) | 3 working days before |
| PT 5 | Clarify with the PO and the firmware engineer beforehand which "major other brands" and which "TV brands we sell" are meant, so the compatibility requirement can be stated precisely in the workshop | 3 working days before |
| PT 6 | Run a 15-minute tech check with each end user (audio, camera, whiteboard access, adding a sticky note, placing a voting dot); offer a phone dial-in as fallback | 1–2 working days before |
| PT 7 | Agree roles with the scribe (template for requirements, decisions, risks; who watches the chat) and do a dry run of the whiteboard with the scribe | 1 working day before |
| PT 8 | Open the meeting and whiteboard, check screen sharing, set up a timer visible to everyone | 15 minutes before start |

### Materials

* Video-conference link (with dial-in number as fallback) and chat as fallback channel
* Digital whiteboard, prepared with one frame per agenda item (see PT 4) and a permanent risk/parking-lot area
* Pre-read: survey results (5 pain points), current remote's button layout, sales requirement "must work with all TV brands we sell", 12-button constraint
* Requirement template for the scribe (ID, requirement, source stakeholder, related pain point, MoSCoW, notes)
* Risk/open-issue template (ID, description, owner, due date)
* Visible timer and agenda on the first whiteboard frame
* Optional: physical current remote at each end user's home to show on camera

## Agenda

| ID | Start | Duration (min) | Title | Technique | Activity | Workshop goals |
|---|---|---|---|---|---|---|
| AGD 1 | 09:00 | 5 | Welcome and rules | Round of introductions | Facilitator presents goals, agenda, decision rule, and meeting rules (mute when not speaking, raise hand, chat as fallback, parking lot); each participant introduces themselves in one sentence incl. their TV setup at home | – |
| AGD 2 | 09:05 | 7 | Context and constraints | Short input + energizer | Energizer (1 min): everyone holds their current remote up to the camera and names the button they use most. Facilitator summarizes the 5 survey pain points, the current button layout, the sales requirement, and the 12-button limit; participants may ask clarifying questions only | WG 1 |
| AGD 3 | 09:12 | 20 | Elicitation by usage scenario | Brainwriting (first use: each participant silently writes requirements or wishes as sticky notes in the scenario columns, one idea per note, for 8 minutes, and may build on others' notes; then each reads out their top note) | Silent writing (8 min), round where every participant presents 1–2 notes, end users first (9 min); designer and engineer add constraints. Includes 3 min buffer | WG 1 |
| AGD 4 | 09:32 | 10 | Cluster and clarify | Affinity clustering (first use: group similar notes into clusters and name each cluster as a requirement) | Facilitator and participants merge duplicates, scribe phrases each cluster as a requirement and links it to a pain point; conflicts and feasibility doubts (e.g. battery life vs. backlight/voice/display) go to the risk board | WG 1, WG 3 |
| AGD 5 | 09:42 | 18 | MoSCoW prioritization | MoSCoW (first use: each requirement is classified as Must have, Should have, Could have, or Won't have this release) | Each participant places requirements in the MoSCoW columns (5 min, silently); group discusses deviations; designer checks the "12-button counter" for all requirements needing a physical button; scribe records classification and rationale. Includes 3 min buffer | WG 2 |
| AGD 6 | 10:00 | 10 | Break | – | Cameras off, away from the screen | – |
| AGD 7 | 10:10 | 10 | Agree top 5 for the first release | Dot voting (first use: each participant places 3 dots on the Must/Should requirements they consider most important) | Dot voting (3 min), facilitator shows the ranking, group checks feasibility (engineer) and the 12-button limit (designer); consensus on the top 5, otherwise the PO decides. Includes 3 min buffer | WG 2 |
| AGD 8 | 10:20 | 7 | Open issues and risks | Risk round (first use: each participant names the one biggest risk or open question from their perspective) | Complete the risk board collected during the session; each item gets an owner and a due date | WG 3 |
| AGD 9 | 10:27 | 3 | Wrap-up | One-word flash feedback | Facilitator recaps the top 5, key decisions, and next steps; each participant gives one word of feedback | WG 1, WG 2, WG 3 |

## Facilitation Tips

| ID | Situation | Recommended action |
|---|---|---|
| FT 1 | Conflict between stakeholders, e.g. end users want more direct-access buttons but the 12-button limit is fixed, or the designer wants a slim device while the engineer needs a larger battery | Make the conflict visible on the whiteboard, ask each side for the underlying need (e.g. "fast access to Netflix" may be solved by a configurable button), seek consensus; if none is reached within 3 minutes, the product owner decides and the scribe records the decision and rationale |
| FT 2 | A dominant participant (e.g. the product owner or the engineer) talks for long or pre-empts the end users | Use silent techniques first (brainwriting, silent MoSCoW, dot voting), let end users speak first in rounds, enforce a 1-minute speaking limit, and point to the agenda and timer |
| FT 3 | Silent participants, typically end users who feel less expert | Address them by name with an easy, scenario-based question ("How do you switch to the soundbar today?"), invite contributions via chat or sticky notes, and value every contribution explicitly |
| FT 4 | Technical problems (audio drops, a user cannot access the whiteboard) | Switch to the chat as fallback; the scribe transfers chat contributions to the whiteboard; offer dial-in by phone; do not wait more than 2 minutes, continue and catch the participant up after the break |
| FT 5 | Attention drops in the video session | Keep inputs short (max. 5 minutes), alternate silent work and discussion, use the camera energizer in AGD 2 and a camera-off break at 10:00, and keep the timer visible |
| FT 6 | Technical jargon (IR, HDMI-CEC, Bluetooth LE) excludes end users | Ask the engineer to translate into user impact ("the remote also controls the soundbar volume without pointing") and have the scribe phrase requirements in plain language |
| FT 7 | Discussion drifts into solution design or topics outside scope (e.g. app control, pricing) | Park the topic on the risk/parking-lot board with an owner and return to the agenda |
| FT 8 | The scope of "all TV brands we sell" vs. "major other brands" is unclear | Record it as an open issue, do not resolve it in the workshop unless the PO can decide on the spot |

## Follow-up

| ID | Step | Timing |
|---|---|---|
| FS 1 | Scribe finalizes the minutes: requirements list with MoSCoW, top 5 with rationale, decisions, risks and open issues with owners; export of the whiteboard | Within 1 working day |
| FS 2 | Send the minutes to all participants for validation, asking them to confirm or correct the phrasing of the requirements and the top 5 within a set deadline | Within 2 working days; feedback within 5 working days |
| FS 3 | Clarify open issues and risks with their owners (e.g. battery life budget vs. features, brand compatibility list, button mapping within 12 buttons) | By the due dates set in AGD 8 |
| FS 4 | Specify the top 5 requirements in detail with acceptance criteria and review them with the designer and the engineer | Within 2 weeks |
| FS 5 | Validate the button layout concept for the top 5 with the end users (e.g. paper or clickable prototype) | Within 4 weeks |
| FS 6 | Share the agreed prioritization and the sales requirement interpretation with sales | Within 1 week |
