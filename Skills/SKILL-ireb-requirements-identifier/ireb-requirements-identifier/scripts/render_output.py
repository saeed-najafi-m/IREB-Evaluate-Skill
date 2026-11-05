#!/usr/bin/env python3
"""Render requirements-identifier JSON as a deterministic Markdown table.

The renderer preserves requirement content verbatim and only adds Markdown
structure. It does not extract, translate, summarize, or validate requirements.
Validate inputs with ``validate_output.py`` before rendering them.

Usage:
    python render_output.py <file1.json> [<file2.json> ...] \
        [--format markdown] [--language en|de] [-o output.md]

If ``-o`` is omitted, the result is printed to stdout. Markdown is the only
supported format.
"""

import argparse
import json
import sys
from pathlib import Path


def escape_inline(value):
    """Escape Markdown syntax used in generated table cells."""
    text = str(value).replace("\ufffd", "-").replace("�", "-")
    text = text.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
    for character in "\\`*_{}[]<>#|":
        text = text.replace(character, "\\" + character)
    return text


def render_statements(statements, source_label):
    """Pair every statement with its source in one table cell."""
    blocks = []

    for statement in statements:
        statement_text = escape_inline(statement.get("statement", ""))
        source = escape_inline(statement.get("source", ""))
        blocks.append(f'"{statement_text}"<br>**{source_label}:** {source}')

    return "<br><br>".join(blocks)


def render(instances, language):
    requirements = []
    for instance in instances:
        requirements.extend(instance["original_requirements"])

    if not requirements:
        return "No requirements identified.\n"
    else:
        source_label = "Quelle" if language == "de" else "Source"
        title_label = "Titel" if language == "de" else "Title"
        statements_label = "Aussage" if language == "de" else "Statements"
        blocks = [f"| ID | {title_label} | {statements_label} |", "|---|---|---|"]
        for requirement in requirements:
            requirement_id = escape_inline(requirement.get("id", ""))
            title = escape_inline(requirement.get("title", ""))
            statements = render_statements(requirement.get("statements", []), source_label)
            blocks.append(f"| {requirement_id} | {title} | {statements} |")

    return "\n".join(blocks).rstrip() + "\n"


def load_input(path):
    try:
        instance = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"cannot read file: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON: {exc}") from exc

    if not isinstance(instance, dict) or not isinstance(
        instance.get("original_requirements"), list
    ):
        raise ValueError("expected a top-level 'original_requirements' array")
    return instance


def parse_args():
    parser = argparse.ArgumentParser(
        description="Render requirements-identifier JSON as Markdown."
    )
    parser.add_argument("inputs", type=Path, nargs="+", help="Input JSON file(s)")
    parser.add_argument(
        "-f",
        "--format",
        choices=["markdown"],
        default="markdown",
        help="Output format (default: markdown)",
    )
    parser.add_argument(
        "--language",
        choices=["en", "de"],
        default="en",
        help="Language for renderer labels (default: en)",
    )
    parser.add_argument("-o", "--output", type=Path, help="Output file (default: stdout)")
    return parser.parse_args()


def main():
    args = parse_args()
    instances = []
    for path in args.inputs:
        try:
            instances.append(load_input(path))
        except ValueError as exc:
            print(f"ERROR: {path}: {exc}", file=sys.stderr)
            return 1

    result = render(instances, args.language)
    if args.output:
        try:
            args.output.write_text(result, encoding="utf-8")
        except OSError as exc:
            print(f"ERROR: cannot write {args.output}: {exc}", file=sys.stderr)
            return 1
        print(f"Written to {args.output}")
    else:
        sys.stdout.write(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
