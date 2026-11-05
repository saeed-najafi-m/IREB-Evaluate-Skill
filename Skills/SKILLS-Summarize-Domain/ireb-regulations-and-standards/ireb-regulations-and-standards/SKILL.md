---
name: ireb-regulations-and-standards
description: Use this skill to list the most important laws, regulations, standards, and guidelines to consider when specifying a system in a domain that is new to the requirements engineer, for a given country or region. From a domain, a system name, and optionally a country or region and documents the user provides, it produces one Markdown document for human review, researched with web search in official sources. Use it whenever someone asks which rules apply to a system or prepares compliance requirements, e.g. "which regulations apply to", "relevant standards for", "regulatory requirements of", "welche Normen gelten für", "relevante Gesetze und Normen", "regulatorische Vorgaben für".
license: Apache-2.0
compatibility: Works without scripts or bundled files. Web search is needed unless the user provides documents that cover the applicable regulations and standards.
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

List the most important **Regulations and Standards** to consider when specifying the system in the given country or region. For each, give an **id** (`REG {{n}}`), its official short **designation** (e.g. "Commission Implementing Regulation (EU) 2017/373", "ISO 9001:2015"), one **type**, optionally its **jurisdiction** (International, Regional, National, or Organizational, naming the region or country), a **description** and its **relevance** (one sentence each), and at least one **source**.

Types:
* **Law**: issued by a legislator, or an international treaty (e.g. Chicago Convention).
* **Regulation**: binding rule issued by an authority on the basis of a law.
* **Standard**: issued by a standardization body or an international organization.
* **Guideline**: non-binding.

If the type is unclear, choose the most plausible one and say why in the description.

List the sources (`SRC {{n}}`) with title, url, edition or date (or "not stated"), and reading status: full (the complete text, without embedded media or linked pages), partial (which parts), or provided document.

## Instructions

1. **Prioritize sources**: Use provided documents first; they take precedence for the organization's own terms. Then use official web sources (legislators, standardization bodies, authorities) in their current edition. If one is not freely available or cannot be retrieved, use an authority's copy or another official publication, never an unofficial copy; if none can be read, leave the source out. No blogs, forums, or vendor marketing.
2. **Read and reference sources**: Use at least three sources you have read, not search snippets. Base each entry on its official text or on an official publication by its issuer. Reference the sources for each entry.
3. **Write accessibly**: Explain technical terms and abbreviations at first use. Do not invent sources, products, organizations, people, figures, or statistics.
4. **State limitations**: State limitations (no documents, no web search, unreadable sources, fewer than three sources, no rules found for the country or region, not an IT system) in one opening sentence. Add no other preamble.
5. **Include only confirmed entries**: Include only entries that a source confirms; never guess a designation, version, or issuer. Use the current version; treat amendments as part of the act they amend and mention relevant ones in its description; omit repealed acts.
6. **Classify international rules**: Classify standards of international organizations (e.g. ICAO Annexes) as Standard, and their procedures and manuals (e.g. ICAO PANS, ICAO Docs) as Guideline.

## Input

Ask the user for the domain, the system, the country or region, and optionally any relevant documents before proceeding. Without a country or region, cover international rules only.

---
## Output

* Write the result as one Markdown document, named `regulations-and-standards.md`, with exactly this structure:
  * `# Regulations and Standards: <system>, <country or region>` (omit the country or region if none was given), then the limitation sentence, if any.
  * A table with the columns ID, Designation, Type, Jurisdiction, Description, Relevance, Sources.
  * `## Sources`, as a table with the columns ID, Title, URL, Edition or date, Reading status. Show "–" for empty values.
  * Write the whole document, including the headings, column headers, type and jurisdiction values, and "not stated", in the language of the user's request.
* Report the cases you had to decide without clear guidance to the user alongside the result, outside the document.
* The document is a draft for human review. Do not add approval or review status.
