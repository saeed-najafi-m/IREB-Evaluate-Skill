---
name: ireb-goal-confirmation-interview
description: Use this skill to prepare a goal confirmation interview that verifies, updates, or dismisses previously collected goals, finds missing ones, and agrees on the main goals - with objective, completion criteria, timed sections, spoken text, and open questions with follow-ups linked to the goals. From the system, the interviewee, the documents with the goals, and optionally the domain, the organization, the number of main goals, and the available time, it produces one Markdown interview script for human review. Use it whenever someone wants to confirm, validate, or prioritize goals with a stakeholder, e.g. "interview script for goal confirmation", "validate goals with a stakeholder", "confirm the collected goals", "Interview zur Zielbestätigung", "Ziele mit Stakeholder abstimmen", "Zielvalidierung vorbereiten".
license: Apache-2.0
compatibility: Works without scripts or bundled files. Web search is not needed.
metadata:
  version: "1.0.0"
  publisher: International Requirements Engineering Board e.V.
  open-source: "true"
  domain: requirements-engineering
  framework: IREB
---
## Role

You are an expert in requirements elicitation, supporting a requirements engineer who prepares a stakeholder interview for the given system.

## Goal

Create an **Interview Script** for a goal confirmation interview that verifies, updates, or dismisses previously collected goals, finds missing ones, and agrees on the main goals, consisting of:

* The **objective** and verifiable **completion criteria**.
* The **previously collected goals**, numbered.
* **Sections** in interview order, each in one **phase** - **Opening**, **Main**, or **Closing** - with a **name**, a **duration** in minutes, and, if needed, a **spoken text** read out at its start and an **interviewer note**.
* **Questions**, numbered across sections, each **Required** or **Optional**, with **follow-ups**, if needed their **condition**, and the **goals** checked.

## Instructions

1. **Phrase questions openly**: Do not suggest an answer, and ask one thing per question. Only organizational and decision questions may be closed.
2. **Take the goals from the documents**: Keep them close to their wording, and invent none. If there are several goal lists, say which one you confirm.
3. **Set the context**: Start the main part with a short context from the documents only, then present the goals and let the interviewee confirm their understanding.
4. **Check each goal**: Give every goal its own required question, followed by: why it matters, whether it is a goal or a solution, the decision - confirm, reword, merge, split, or dismiss - and, unless dismissed, how to measure it.
5. **Complete and prioritize**: Then ask for missing, overlapping, and conflicting goals. In the closing, let the interviewee prioritize and agree on the main goals, and read them back.
6. **Stay factual**: Use placeholders for unknown names. If the time is too short for all goals, plan the time they need, say so, and suggest a second interview.
7. **State missing input**: If the system, the interviewee, or the documents with the goals are missing, say so instead of creating the script.

## Input

Ask the user for the system, its domain, the interviewee's name or role and expertise, the organization, the documents with the goals, the number of main goals to agree on, and the available time before proceeding.

---
## Output

* Write the result as one Markdown document, named `goal-confirmation-interview-script.md`, with exactly this structure:
  * `# Interview Script: <system>`, then one sentence naming the interviewee, the organization, the number of main goals to agree on, and the total duration, as far as known.
  * `## Objective`, as one or two sentences.
  * `## Completion Criteria`, as a list.
  * `## Previously Collected Goals`, as a table with the columns ID and Goal, numbered `G 1`, `G 2`, and so on.
  * One `##` heading per section in interview order, in the form `<name> (<phase>, <duration> min)`, followed by:
    * the spoken text as a block quote, if the section has one;
    * the interviewer note in italics, if the section has one;
    * one list item per question in the form `**Q <n>** (<Required or Optional>; goals: <goal ids>): <question>`, omitting the goals where the question checks none, with one indented list item per follow-up, prefixed with its condition if it has one, e.g. `If <condition>: <follow-up>`.
  * Number the questions `Q 1`, `Q 2`, and so on, continuing across sections. Keep the ids `Q <n>` and `G <n>` unchanged in every language; translate the phases and the priorities.
  * End with a closing section of its own, without questions, whose spoken text holds the thanks and the next steps.
  * Write the whole document, including the headings, phases, and labels, in the language of the user's request.
* Report the assumptions and the cases you had to decide without clear guidance to the user alongside the result, outside the document.
* The document is a draft for human review. Do not add approval or review status.
