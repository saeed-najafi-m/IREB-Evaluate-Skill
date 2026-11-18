# Workshop Plan: Universal TV Remote Control (successor model)

Remote workshop via video conference, 90 minutes from 09:00 to 10:30, with 10 participants; decision rule: consensus, and if no consensus is reached, the product owner decides (assumed).

## Workshop Goals

| ID | Goal | Expected result |
|---|---|---|
| WG 1 | Elicit the requirements for the new remote from all stakeholder groups | Clustered list of candidate requirements on the whiteboard, each traced to a pain point from the survey, a usage scenario, or a business/technical need; contributions from every stakeholder group (reduced scope: candidate requirements as short statements, detailed formulation in follow-up) |
| WG 2 | Prioritize the requirements (MoSCoW) and agree the top 5 for the first release | Must/Should classification of all candidate-requirement clusters and an agreed, ranked top 5 for release 1 that fits the 12-button limit (reduced scope: the Could/Won't split is completed in follow-up) |
| WG 3 | Identify open issues and risks (e.g. battery life vs. features) | Risk and open-issue list with a quick impact/likelihood rating and an owner per item (reduced scope: mitigation planned in follow-up) |

## Participants

| ID | Role | Number | Expected contribution |
|---|---|---|---|
| WP 1 | Product owner | 1 | Business goals, scope, prioritization decision when there is no consensus |
| WP 2 | Industrial designer | 1 | Usability, look and feel, hardware constraints (12-button limit, form factor, battery) |
| WP 3 | End users (diverse households) | 4 | Real usage scenarios, pain points with the current remote |
| WP 4 | Software/firmware engineer | 1 | Technical feasibility, interfaces to TV and soundbar, compatibility with other brands |
| WP 5 | Facilitator (requirements engineer) | 1 | Moderation, techniques, agenda, timekeeping, whiteboard host |
| WP 6 | Scribe | 1 | Documents requirements, decisions, and risks; adds cards to the whiteboard for anyone with technical problems |

## Preparation

| ID | Task | Timing |
|---|---|---|
| PT 1 | Send the invitation with goals, agenda, decision rule, video-conference link, phone dial-in, and whiteboard link | 1 week before |
| PT 2 | Send the pre-read (survey results with the 5 pain points, current button layout, sales requirement, 12-button limit); ask each end user to note 2–3 everyday situations with the remote | 1 week before |
| PT 3 | Pre-meeting with the product owner: confirm scope, decision rule, criteria for the top 5, and their role of speaking last when prioritizing | 3 days before |
| PT 4 | Pre-meeting with the engineer: TV/soundbar brands and protocols to support (e.g. IR, HDMI-CEC, Bluetooth), known battery and cost constraints, as input for the feasibility check | 3 days before |
| PT 5 | Prepare the digital whiteboard with one frame per agenda item: check-in, brainwriting areas pre-filled with the 5 pain points, clustering area, a "12 buttons" panel with the current layout, a MoSCoW board with voting dots, a risk board (impact × likelihood), a parking lot | 3 days before |
| PT 6 | 15-minute tech check with each participant, especially the end users: audio, camera, whiteboard access, adding a sticky note, voting with a dot; explain the chat as the fallback channel | 2–3 days before |
| PT 7 | Brief the scribe: templates for requirements (ID, statement, source, priority), decisions, and risks; agree who records chat input | 1 day before |
| PT 8 | Facilitator test run: whiteboard frames, timers, voting function, screen sharing | 1 day before |

### Materials

- Video-conference link with a phone dial-in as a backup
- Digital whiteboard with one prepared frame per agenda item (see PT 5)
- Survey results (5 pain points), current button layout, sales requirement "must work with all TV brands we sell", 12-button limit, all placed on the whiteboard
- Visible timer (shared on screen or on the whiteboard)
- Chat in the video conference as a fallback channel
- Scribe templates for requirements, decisions, and risks
- Slide with goals, agenda, ground rules, and decision rule

## Agenda

| ID | Start | Duration (min) | Title | Technique | Activity | Workshop goals |
|---|---|---|---|---|---|---|
| AGD 1 | 09:00 | 8 | Opening and check-in | Check-in round (each person answers one question in a fixed order, at most 30 seconds each) | Welcome; goals, agenda, ground rules, and decision rule; check-in question "Which button on your current remote do you never use?" Every participant adds a sticky note to the board, which also tests the whiteboard | – |
| AGD 2 | 09:08 | 22 | Eliciting pain points and usage scenarios | Brainwriting (everyone writes ideas silently and in parallel on sticky notes, then builds on others' notes) + round robin (each person presents in turn) | 8 min silent writing on the 5 pain-point areas and an "other needs" area: end users add scenarios and problems, the designer adds usability and hardware needs, the engineer adds technical needs, the product owner adds business goals; 2 min of building on other people's notes; 12 min round robin starting with the end users, with the facilitator asking clarifying questions (includes 3 min buffer) | WG 1 |
| AGD 3 | 09:30 | 20 | Clustering and feasibility check | Affinity clustering (grouping related notes into named clusters) | Group the notes into candidate requirements, e.g. "find the remote", "switch input/soundbar", "backlight", "voice"; the engineer and the designer comment on each cluster's feasibility and button cost against the 12-button limit; risks and conflicts that come up (e.g. battery life vs. backlight/voice) go onto the risk board, and off-topic items go into the parking lot (includes 3 min buffer) | WG 1, WG 3 |
| AGD 4 | 09:50 | 10 | Break | – | Cameras off and away from the screen | – |
| AGD 5 | 10:00 | 15 | MoSCoW prioritization and top 5 | Dot voting (each person places a limited number of dots, here 5, on the clusters they think matter most) + MoSCoW (Must / Should / Could / Won't have for this release) | 3 min silent dot voting; the facilitator sorts clusters by votes; classify Must/Should with a cap (Musts must fit within the 12 buttons); discuss the top candidates, with the product owner speaking last; agree the top 5 by consensus, and if there is no consensus the product owner decides; the scribe records the rationale (includes 3 min buffer) | WG 2 |
| AGD 6 | 10:15 | 9 | Open issues and risks | Round robin + risk board (impact × likelihood grid) | Each person adds or confirms at most one risk or open issue in turn (e.g. battery life vs. features, compatibility with other brands, button count vs. functions); quick placement on the grid; an owner is named for each item | WG 3 |
| AGD 7 | 10:24 | 6 | Wrap-up | One-word round | Facilitator recaps the top 5, the Must/Should list, the risks, and the parking lot; explains the next steps and the validation; each participant gives one word of feedback on the workshop | WG 1, WG 2, WG 3 |

## Facilitation Tips

| ID | Situation | Recommended action |
|---|---|---|
| FT 1 | Conflict, e.g. designer vs. engineer on button count or features vs. battery life | Make the trade-off visible on the "12 buttons" panel ("if this becomes a button, which one goes?"); restate both positions neutrally; seek consensus within a time box of 3 min; if there is none, the product owner decides; the scribe records the decision and the rationale, and the open trade-off goes onto the risk board |
| FT 2 | Dominant participant (e.g. product owner or engineer steering the discussion) | Use silent writing and voting before any discussion; use round robin with a fixed order; ask the product owner to speak last when prioritizing; politely time-box ("let's hear two more voices first") |
| FT 3 | Silent participants (often end users unfamiliar with the vocabulary of product development) | Use brainwriting so everyone can contribute without speaking; invite people by name with open questions ("how does this work in your household?"); accept input via chat, with the scribe transferring it to the board |
| FT 4 | Technical problems (audio, connection, whiteboard access) | Switch to the chat as the fallback channel; the scribe adds cards for the person affected; use the phone dial-in for audio; do not stop the whole group for one person's problem, and recap for them when they rejoin |
| FT 5 | Dropping attention in the video session | Change the activity every 10–20 minutes (writing, presenting, voting); keep the break camera-off and away from the screen; use a 1-minute stand-up stretch energizer if energy drops before AGD 5 |
| FT 6 | Every requirement becomes a "Must" | Cap the Musts at what fits into the 12 buttons and release 1; ask "would we cancel the release without it?" |
| FT 7 | Technical jargon from the engineer or designer (e.g. "CEC", "IR learning") | Ask for an explanation in plain language with an everyday example for the end users |
| FT 8 | Discussion runs over the time box or drifts off-topic | Move the item into the parking lot with an owner; use the buffer in AGD 2, AGD 3, or AGD 5 first, then cut details rather than agenda items |

## Follow-up

| ID | Step | Timing |
|---|---|---|
| FS 1 | Scribe distributes the minutes: candidate requirements, MoSCoW classification, top 5 with rationale, risk list, parking lot, whiteboard export | Within 1 working day |
| FS 2 | Facilitator formulates the candidate requirements as complete requirements traced to their source (pain point, scenario, stakeholder) | Within 3 working days |
| FS 3 | Validate the results with all participants: comment period on the requirements, the top 5, and the risks; a short follow-up call with the end users if they have a lot of feedback | Comments within 1 week after FS 2 |
| FS 4 | Facilitator, product owner, and designer complete the Could/Won't classification and check the button allocation against the 12-button limit | Within 2 weeks |
| FS 5 | Risk owners propose mitigations (e.g. battery-life budget per feature, compatibility list for the TV brands sold, with the engineer and sales) | Within 2 weeks |
| FS 6 | Product owner confirms the validated top 5 for release 1; facilitator updates the requirements backlog and closes or reassigns the parking-lot items | After FS 3 to FS 5 |
