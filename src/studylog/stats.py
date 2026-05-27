"""Statistics helpers for StudyLog entries."""

from __future__ import annotations

from dataclasses import dataclass

from studylog.model import StudyEntry


@dataclass(frozen=True)
class StudyStats:
    total_entries: int
    done_entries: int
    todo_entries: int
    total_minutes: int
    done_minutes: int

    @property
    def completion_rate(self) -> float:
        if self.total_entries == 0:
            return 0.0
        return self.done_entries / self.total_entries


def calculate_stats(entries: list[StudyEntry]) -> StudyStats:
    total_entries = len(entries)
    done_entries = sum(1 for entry in entries if entry.status == "done")
    total_minutes = sum(entry.minutes for entry in entries)
    done_minutes = sum(entry.minutes for entry in entries if entry.status == "done")
    return StudyStats(
        total_entries=total_entries,
        done_entries=done_entries,
        todo_entries=total_entries - done_entries,
        total_minutes=total_minutes,
        done_minutes=done_minutes,
    )


def format_stats(stats: StudyStats) -> str:
    percent = stats.completion_rate * 100
    return "\n".join(
        [
            f"Total entries: {stats.total_entries}",
            f"Done entries: {stats.done_entries}",
            f"Todo entries: {stats.todo_entries}",
            f"Total minutes: {stats.total_minutes}",
            f"Done minutes: {stats.done_minutes}",
            f"Completion rate: {percent:.1f}%",
        ]
    )
