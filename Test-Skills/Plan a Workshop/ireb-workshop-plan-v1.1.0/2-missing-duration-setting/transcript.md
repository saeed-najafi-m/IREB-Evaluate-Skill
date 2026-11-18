# Transcript: 2-missing-duration-setting

## Turn 1: User (opening message)

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

**Documents provided:** results of the user survey (5 pain points), current remote's button layout,
sales requirement "must work with all TV brands we sell".

**Known constraint:** the hardware budget allows at most 12 physical buttons.

## Turn 1: Skill agent

I can draft the plan once I know two things the brief doesn't cover:

1. **Duration:** how long is the workshop? For example half a day (4 h) or a full day. Eliciting, MoSCoW-prioritizing and picking a top 5 with 10 participants probably needs at least about 4 hours. If you give me less time than that, I'll cut the scope and tell you what I dropped.
2. **Setting:** will it be **on-site**, **remote** or **hybrid**? This changes the techniques, the materials and the breaks. Remote needs a video link, a digital whiteboard and a tech check. Hybrid also needs a co-facilitator for the people dialing in.

You can also set these, or I'll use the defaults:
- **Start time:** 09:00.
- **Break rhythm:**
  - On-site: 15 min after at most 90 min of work.
  - Remote: 10 min after at most 60 min.
  - Hybrid: 15 min after at most 60 min.
  - A 45-minute lunch between 11:30 and 13:30 if the workshop runs longer than 4 hours or over midday.

I'll use the rest of your brief as given: the goals, the 10 participants, the survey, the current button layout, the sales requirement and the 12-button limit. Unless you tell me otherwise, conflicts will be settled by consensus, and the product owner decides when there's no consensus.

## Turn 2: User (simulated)

Duration: 90 minutes. Setting: remote (video conference). Start time and breaks: no preference, the defaults are fine.

## Turn 2: Skill agent

I've written the workshop plan to `<workspace>\workshop-plan.md`. It runs remotely from 09:00 to 10:30 with 10 participants, and the agenda durations add up to exactly 90 minutes.

**90 minutes isn't enough to fully reach all three goals with 10 people, so I cut the scope:**
- **Goal 1 (elicit):** the workshop collects and clusters short candidate requirements. Writing them out as full requirements happens afterwards.
- **Goal 2 (prioritize):** the workshop sorts requirements into Must and Should and agrees the top 5. The split into Could and Won't is finished afterwards with the product owner and designer.
- **Goal 3 (risks):** risks and open issues are collected, quickly rated by impact and likelihood, and each gets an owner. Plans for handling them come later.

**Timing:**
- The 10-minute break is at 09:50, after 50 minutes of work. The second block is 30 minutes. Both stay under the 60-minute limit for remote sessions.
- The roughly 10% buffer (9 minutes) is built into the working items rather than added as its own slot: 3 minutes each in the elicitation item, the clustering and feasibility item, and the prioritization item.

**Assumptions:**
- If there's no consensus, the product owner decides. You didn't object when I proposed this, but you didn't confirm it either.
- Pre-meetings and tech checks are timed relative to the workshop date, because no date was given.
- End users get a phone dial-in, the chat counts as input, and the scribe moves their contributions onto the whiteboard. I added this because "diverse households" may include people who aren't comfortable with online whiteboards.
- I used examples like "find the remote", backlight, voice control, IR, HDMI-CEC and Bluetooth only as illustrations. They don't come from your survey.

**Decisions I made without clear guidance:**
- The opening (check-in) and the break aren't linked to any goal, so they show "–".
- The 12-button limit is used as the cap on Must-haves, so a requirement that needs a new physical button has to replace an existing one.
- In dot voting (everyone places a limited number of dots on the ideas they rate highest), each participant gets 5 dots, to match the top 5.
- The product owner speaks last when prioritizing so the others aren't anchored by their view, while still making the call if there's no consensus.
- There's no co-facilitator, because the workshop is fully remote rather than hybrid. The scribe helps anyone with technical problems.
