"""Human-readable formatting helpers for StudyLog CLI output."""

from __future__ import annotations

from studylog.model import StudyEntry


def format_entry(entry: StudyEntry) -> str:
    """Format one entry for the list command."""
    marker = "✓" if entry.status == "done" else " "
    note = f" - {entry.note}" if entry.note else ""
    return f"[{marker}] #{entry.id} {entry.topic} ({entry.minutes}m){note}"
