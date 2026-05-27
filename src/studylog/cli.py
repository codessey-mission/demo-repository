"""Command line interface for StudyLog."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from studylog.export import render_markdown_report
from studylog.formatting import format_entry
from studylog.stats import calculate_stats, format_stats
from studylog.storage import StudyLogStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="studylog", description="Record and review study tasks.")
    parser.add_argument("--data", default="studylog.json", help="Path to the StudyLog JSON data file.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a study entry.")
    add_parser.add_argument("topic", help="Study topic or task name.")
    add_parser.add_argument("--minutes", required=True, help="Planned or spent study minutes.")
    add_parser.add_argument("--note", default="", help="Optional note.")

    subparsers.add_parser("list", help="List study entries.")

    complete_parser = subparsers.add_parser("complete", help="Mark a study entry as done.")
    complete_parser.add_argument("id", type=int, help="Entry id to complete.")

    delete_parser = subparsers.add_parser("delete", help="Delete a study entry.")
    delete_parser.add_argument("id", type=int, help="Entry id to delete.")

    subparsers.add_parser("stats", help="Show study statistics.")

    export_parser = subparsers.add_parser("export-md", help="Export a Markdown study report.")
    export_parser.add_argument("output", help="Output Markdown file path.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    store = StudyLogStore(Path(args.data))

    if args.command == "add":
        entry = store.add(args.topic, args.minutes, args.note)
        print(f"Added #{entry.id}: {entry.topic} ({entry.minutes}m)")
        return 0

    if args.command == "list":
        entries = store.load()
        if not entries:
            print("No study entries yet.")
            return 0
        for entry in entries:
            print(format_entry(entry))
        return 0

    if args.command == "complete":
        entry = store.complete(args.id)
        if entry is None:
            print(f"Entry #{args.id} was not found.")
            return 1
        print(f"Completed #{entry.id}: {entry.topic}")
        return 0

    if args.command == "delete":
        if not store.delete(args.id):
            print(f"Entry #{args.id} was not found.")
            return 1
        print(f"Deleted #{args.id}.")
        return 0

    if args.command == "stats":
        print(format_stats(calculate_stats(store.load())))
        return 0

    if args.command == "export-md":
        output_path = Path(args.output)
        output_path.write_text(render_markdown_report(store.load()), encoding="utf-8")
        print(f"Exported Markdown report to {output_path}")
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
