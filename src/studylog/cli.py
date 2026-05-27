"""Command line interface for StudyLog."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from studylog.formatting import format_entry
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

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
