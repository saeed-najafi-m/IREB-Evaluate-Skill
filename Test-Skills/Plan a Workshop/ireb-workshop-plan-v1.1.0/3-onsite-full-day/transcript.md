# Transcript: 3-onsite-full-day

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

**Duration:** 6 hours. **Setting:** on-site (meeting room at the company). **Documents provided:**
results of the user survey (5 pain points), current remote's button layout, sales requirement
"must work with all TV brands we sell".

**Known constraint:** the hardware budget allows at most 12 physical buttons.

## Turn 1: Skill agent

I've written the workshop plan to `<workspace>\workshop-plan.md`. It runs from 09:00 to 15:00 on-site and covers all three goals in the time; I didn't have to drop anything.

**How the day runs**
- **Morning (goal 1, collecting requirements):** a review of the survey's pain points with the current remote in hand, then usage scenarios in mixed groups. After that, everyone writes requirements silently on sticky notes and the group sorts them into categories. The engineer and designer then check each one for feasibility and against the constraints.
- **After lunch (goal 2, prioritizing):** dot voting and MoSCoW, with end users voting first. The top 5 come out of a "12-button budget" exercise, where groups place the Must requirements on a cardboard remote with only 12 button stickers. A quick show of fingers checks agreement.
- **Last block (goal 3, issues and risks):** participants imagine the remote has failed in the market and write down why. The facilitator adds these to issues collected during the morning, rates them, and gives the important ones an owner. A 15-minute wrap-up closes the day.

**Timing checks**
- Durations add up to exactly 360 minutes.
- No work block is longer than 90 minutes.
- Lunch is 12:15–13:00, inside the 11:30–13:30 window.
- Every goal is covered by at least one agenda item.

**Assumptions and decisions I made without guidance from you**
1. **Start time:** 09:00, so the end is 15:00.
2. **Decision rule:** the group decides by consensus; if it can't agree, the product owner decides. This fits the product owner's listed role ("prioritization decision").
3. **Breaks:** 15-minute breaks at 10:30 and 14:30, and a 45-minute lunch in place of the regular midday break.
4. **Buffer:** 30 minutes in total, the maximum (10 % of the day would be 36). It's spread across the working items rather than shown as its own item:
   - 5 minutes in the usage scenarios (AGD 3)
   - 10 minutes in requirement writing and sorting (AGD 5)
   - 5 minutes each in the feasibility check, prioritization and top-5 items (AGD 6, 8, 9)
5. **Brand scope:** the brief mentions both "major other brands" (the system description) and "all TV brands we sell" (the sales requirement). I read the sales list as the binding minimum and the "major other brands" scope as something the product owner and sales need to settle before the workshop (preparation task PT 3). If it isn't settled, it stays an open issue.
6. **The 12-button limit:** treated as fixed. The workshop decides which functions get a physical button and which use other means such as a long press, an on-screen menu or an app.
7. **Groups:** two mixed groups of 2 end users plus either the designer or the engineer, so that end users aren't outweighed by experts.
8. **Lead times and deadlines:** all preparation lead times, follow-up deadlines and the issue-list format are my estimates and are marked "(assumed)" in the document.
9. **Mixed household profiles:** I suggested a mix including someone with accessibility needs, a family, a tech-savvy single person and a household with a soundbar. The brief only said "diverse".
10. **Pain points:** the brief doesn't list the 5 survey pain points, so the plan refers to them generically. Once the survey results are in, you could tailor the scenarios in AGD 3 to them.

I can also turn the plan into a shareable page if you want to send it to the participants.
