"""Markdown export for StudyLog."""

from __future__ import annotations

from studylog.formatting import format_entry
from studylog.model import StudyEntry
from studylog.stats import calculate_stats, format_stats


def render_markdown_report(entries: list[StudyEntry]) -> str:
    """Render a Markdown report for study entries."""
    stats = calculate_stats(entries)
    lines = [
        "# StudyLog Report",
        "",
        "## Summary",
        "",
    ]
    lines.extend(f"- {line}" for line in format_stats(stats).splitlines())
    lines.extend(["", "## Entries", ""])
    if not entries:
        lines.append("No study entries yet.")
    else:
        for entry in entries:
            lines.append(f"- {format_entry(entry)}")
    lines.append("")
    return "\n".join(lines)
