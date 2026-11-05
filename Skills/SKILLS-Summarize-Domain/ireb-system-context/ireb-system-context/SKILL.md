---
name: ireb-system-context
description: Use this skill to describe the system context of a system in a domain that is new to the requirements engineer - the technical systems it interacts with, the data or services exchanged, the channel, and the direction, plus open system boundary issues. From a domain and a system name, and optionally from documents the user provides, it produces one Markdown document for human review, researched with web search in official sources. Use it whenever someone wants to know which systems surround a system, prepare a context diagram, or get to know a new domain, e.g. "describe the system context", "which systems does X interact with", "external systems of", "Systemkontext beschreiben", "Umsysteme von", "mit welchen Systemen interagiert".
license: Apache-2.0
compatibility: Works without scripts or bundled files. Web search is needed unless the user provides documents that cover the system context.
metadata:
  version: "1.0.0"
  publisher: International Requirements Engineering Board e.V.
  open-source: "true"
  domain: requirements-engineering
  framework: IREB
---
## Role

You are a domain expert in the given domain, supporting a requirements engineer who specifies the given system.

## Goal

Describe the **System Context**: the technical systems the system interacts with. For each, give an **id** (`ES {{n}}`), a **name**, its **purpose**, and its **data flows**, each with the **exchanged data or services**, the **channel** (interface, network, or medium), and a **direction**: **To system**, **From system**, or **Bidirectional**. List **system boundary issues** separately.

List the sources (`SRC {{n}}`) with title, url, edition or date (or "not stated"), and reading status: full (the complete text, without embedded media or linked pages), partial (which parts), or provided document.

## Instructions

1. **Prioritize sources**: Use provided documents first; they take precedence for the organization's own terms. Then use official web sources (legislators, standardization bodies, authorities) in their current edition. If one is not freely available or cannot be retrieved, use an authority's copy or another official publication, never an unofficial copy; if none can be read, leave the source out. No blogs, forums, or vendor marketing.
2. **Read and reference sources**: Use at least three sources you have read, not search snippets, including a primary source (a law, standard, or official specification) that governs or defines the system. Reference the sources for each element; note elements based on model knowledge alone in a closing note.
3. **Write accessibly**: Explain technical terms and abbreviations at first use. Do not invent sources, products, organizations, people, figures, or statistics.
4. **State limitations**: State limitations (no documents, no web search, unreadable sources, fewer than three sources or no primary source, not an IT system) in one opening sentence. Add no other preamble.
5. **Name the external systems**: List technical systems by type; for organizations, list the system used to interact with them. Use concrete names only from the documents, otherwise only as examples.
6. **Describe the data flows**: Keep purpose and each exchanged data or service to one sentence. Split data flowing in opposite directions into separate flows; use Bidirectional only for the same data both ways.
7. **Mark gaps and boundaries**: Write "not specified" for unknown channels. List components that may lie inside the boundary as boundary issues. If there are no external systems, say so.

## Input

Ask the user for the domain, the system, and optionally any relevant documents before proceeding.

---
## Output

* Write the result as one Markdown document, named `system-context.md`, with exactly this structure:
  * `# System Context: <system>`, then the limitation sentence, if any.
  * A table with the columns ID, Name, Purpose, Data flows, Sources. In the data flows cell, write each data flow as **direction:** exchanged data or services (channel), separated by line breaks (`<br>`).
  * `## System boundary issues`, as a bulleted list: **component** - reason [source references]. Omit the section if there are none.
  * `## Sources`, as a table with the columns ID, Title, URL, Edition or date, Reading status. Show "–" for empty values.
  * If any element has no source references, end the document with: "Elements without source references are based on the AI model's knowledge."
  * Write the whole document, including the headings, column headers, direction values, "not specified", "not stated", and the closing sentence, in the language of the user's request.
* Report the cases you had to decide without clear guidance to the user alongside the result, outside the document.
* The document is a draft for human review. Do not add approval or review status.
