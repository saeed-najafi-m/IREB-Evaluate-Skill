#!/usr/bin/env python3
"""Standalone validator for requirements-identification output.

Validates a JSON document against the bundled ``schema/output_schema.json``
using only the Python standard library — no third-party packages and no
ReqWeaver imports — so it runs in any sandbox (e.g. Claude's code execution
environment).

Usage:
    python scripts/validate_output.py <output.json>

Exit codes: 0 = valid, 1 = invalid, 2 = usage/IO error.
"""
import json
import sys
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "output_schema.json"


def _resolve(schema, root):
    """Follow a local ``$ref`` (e.g. '#/$defs/OriginalRequirementModel') to its definition."""
    if "$ref" in schema:
        node = root
        for part in schema["$ref"].lstrip("#/").split("/"):
            node = node[part]
        return node
    return schema


def validate(data, schema, root, path="$"):
    """Return a list of human-readable validation errors (empty list = valid)."""
    schema = _resolve(schema, root)
    errors = []

    if "anyOf" in schema:
        if not any(not validate(data, sub, root, path) for sub in schema["anyOf"]):
            errors.append(f"{path}: does not match any allowed type")
        return errors

    if "enum" in schema:
        if data not in schema["enum"]:
            errors.append(f"{path}: {data!r} is not one of {schema['enum']}")
        return errors

    kind = schema.get("type")
    if kind == "object":
        if not isinstance(data, dict):
            return [f"{path}: expected object, got {type(data).__name__}"]
        for req in schema.get("required", []):
            if req not in data:
                errors.append(f"{path}: missing required field '{req}'")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in data:
                if key not in props:
                    errors.append(f"{path}: unexpected field '{key}'")
        for key, sub in props.items():
            if key in data:
                errors += validate(data[key], sub, root, f"{path}.{key}")
    elif kind == "array":
        if not isinstance(data, list):
            return [f"{path}: expected array, got {type(data).__name__}"]
        item_schema = schema.get("items", {})
        for i, item in enumerate(data):
            errors += validate(item, item_schema, root, f"{path}[{i}]")
    elif kind == "string":
        if not isinstance(data, str):
            errors.append(f"{path}: expected string, got {type(data).__name__}")
    elif kind == "null":
        if data is not None:
            errors.append(f"{path}: expected null")
    return errors


def main(argv):
    if len(argv) != 2:
        print("usage: validate_output.py <output.json>", file=sys.stderr)
        return 2
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        data = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    errors = validate(data, schema, schema)
    if errors:
        print("INVALID:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
