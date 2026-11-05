---
version: 2.0.0
---

# JSON Output Procedure

This procedure governs how a canonical JSON work product is built, validated, rendered, returned, and — only on explicit approval — persisted.

Every step is mandatory unless it states that it may be skipped. Execute required scripts as actual tool calls. Never infer or simulate a script's output, and never claim that a script or validator ran when it did not.

## 0. Work Products and Conventions

The invoking skill names one or more **work products**. A work product's name is also its filename: if it is ever persisted, it is persisted as `<name>.json` and under no other name.

Output tooling sits at fixed paths, resolved against the directory of the skill that produced the work product:

- schema — `schema/output_schema.json`
- validator — `scripts/validate_output.py`
- renderer — `scripts/render_output.py`

Use exactly these. Never substitute or guess a path, a script name, or a filename, never derive one from the input document, and never fall back to a similarly named file found nearby. If the expected tooling is absent, treat it as the unavailable-script case in steps 3 and 4, not as an invitation to find a replacement.

A work product's name is a name, not a location, and naming it is not authorization to create it. No file bearing that name may exist anywhere until step 6 is satisfied.

Reading is not writing. Loading an existing document that the invoking skill instructs you to extend is permitted at any point, and does not authorize writing it back.

Run steps 1–5 for each work product, and run step 6 once per work product, since the user may authorize one and not another.

## 1. Build the Canonical JSON

Create exactly one JSON document per work product, conforming strictly to the schema. Do not add properties the schema prohibits.

If the invoking skill hands this procedure a document produced elsewhere, adopt it unchanged as the canonical document and skip this step. Do not re-author, normalize, reorder, or otherwise improve a document handed in this way.

The canonical document is the canonical result. Every rendered output must be derived from it, and nothing may be added during rendering that is not in it.

## 2. Write the Working File

Validation and rendering operate on a file. That file is a **working file**: a transient implementation detail of this procedure, never a deliverable.

Resolve the temporary directory at runtime rather than hardcoding one — for example by reading the value of `tempfile.gettempdir()`. Write the canonical JSON there as UTF-8 without a BOM, under a name that cannot be mistaken for a deliverable (for example `working-<work-product>-<random>.json`). Never give the working file the work product's name.

The following locations are never acceptable for a working file, regardless of whether they are writable:

- the current working directory, or any directory the user has connected, selected, mounted, or designated for outputs;
- any project, repository, or document tree belonging to the user;
- any skill directory.

If no writable temporary location outside those locations can be resolved, **do not create a working file**. Validate by inspection under step 3 and render directly under step 4. Missing a temporary directory is never a reason to fall back to the working directory.

Serializing the canonical JSON into the working file is the one serialization this procedure authorizes; from here on the working file, not the document in context, is the artifact. Retain it until the persist-or-discard decision in step 6 is resolved: it is the only byte-exact record of what was validated and rendered. Do not present it to the user, do not name it in the response, and do not treat its creation as permission to create any further file.

## 3. Validate the Canonical JSON

Run the validator against the absolute working file path. If validation fails, correct the canonical JSON and rerun until it succeeds. Do not include validator output in the final response.

If the validator cannot be executed, use any other available JSON Schema validator. If none is available, validate by inspection against the schema and confirm that:

- the result is exactly one syntactically valid JSON document;
- all required properties are present;
- every value has the type declared by its schema;
- all object, array, string, number, and value constraints are satisfied;
- every array item conforms to its item schema;
- every enumeration value is permitted;
- every local `$ref` resolves;
- no property prohibited by `additionalProperties: false` is present;
- no Markdown fences, comments, validator output, or other text is part of the document.

Correct every detected error before rendering or returning a result.

## 4. Render When Required

If the user did not specify an output format, render Markdown by running the renderer against the absolute working file path. If the user requested another format the renderer supports, pass the corresponding option. Pass only options the renderer supports.

**Invoke the renderer for standard output only.** Never pass `-o`, `--output`, or any other option that makes the renderer write a file. A renderer is not a route to the filesystem; step 6 is the only route.

Skip rendering only when another skill, tool, or pipeline will consume the canonical JSON and no human will read the result. A user asking for JSON does not by itself remove the need for a review artifact under step 6.

If the renderer cannot be executed, render directly from the validated canonical JSON, preserving its meaning, wording, values, and ordering. Add no interpretation, correction, assumption, or unstated detail.

## 5. Return the Result

Return the renderer's standard output verbatim. Do not reformat, rewrite, reorder its contents, or summarize it. The invoking skill may place that output in a prescribed order among other results and add sections of its own around it; what must not change is the rendered output itself.

If the user asked for JSON in chat, return the validated canonical JSON in a fenced `json` block. If another skill, tool, or pipeline will consume it, return only the validated canonical JSON, unfenced and without surrounding text.

If the user asked for both, return the rendered result followed by the JSON. Include no validation logs, comments, or explanatory text unless the user asked for them.

A request to generate, create, produce, render, show, or return content is not a request to save it. When the user does ask for a file, go to step 6 rather than writing a newly generated document.

## 6. Persist Only After Review

Persisting into a user-visible location is a separate, explicitly authorized action. It is not part of producing a result.

All of the following must hold before anything is written:

1. The user has seen the result returned in step 5 — the rendered output where one was produced, otherwise the returned canonical JSON. That is the review artifact.
2. The user has, after seeing it, explicitly approved saving **this** work product. Approval of another work product in the same run does not carry over.
3. The approval occurred in the session that produced the canonical JSON. If the JSON changed after the user reviewed it, repeat steps 3 and 4 and obtain approval again.
4. The destination directory was named by the user in this session, or is the location the user designated for output. The filename is `<work-product-name>.json` unless the user named a different one.

When these hold, copy the validated working file byte for byte to the destination. Never re-serialize, reformat, regenerate, or reproduce the document from context: the stored file must be the exact artifact that was validated and rendered. If no working file was created, write the validated canonical JSON to the destination at this point and no earlier.

## 7. Remove Temporary Files

Once the persist-or-discard decision is resolved for every work product, remove the working files this procedure created. Remove nothing supplied by the user, and nothing the user requested as a deliverable.