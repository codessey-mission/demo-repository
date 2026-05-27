"""Domain model for StudyLog entries."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Literal

EntryStatus = Literal["todo", "done"]


@dataclass
class StudyEntry:
    """A single study task or study session plan."""

    id: int
    topic: str
    minutes: int
    status: EntryStatus = "todo"
    note: str = ""
    created_on: str = field(default_factory=lambda: date.today().isoformat())

    def __post_init__(self) -> None:
        self.topic = self.topic.strip()
        self.note = self.note.strip()
        if self.id < 1:
            raise ValueError("id must be a positive integer")
        if not self.topic:
            raise ValueError("topic must not be empty")
        if self.minutes <= 0:
            raise ValueError("minutes must be greater than zero")
        if self.status not in {"todo", "done"}:
            raise ValueError("status must be either 'todo' or 'done'")

    def mark_done(self) -> "StudyEntry":
        """Mark this entry as completed and return itself for convenience."""
        self.status = "done"
        return self

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-serializable representation."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "StudyEntry":
        """Build an entry from persisted JSON data."""
        return cls(
            id=int(data["id"]),
            topic=str(data["topic"]),
            minutes=int(data["minutes"]),
            status=str(data.get("status", "todo")),  # type: ignore[arg-type]
            note=str(data.get("note", "")),
            created_on=str(data.get("created_on", date.today().isoformat())),
        )


def parse_minutes(value: str | int) -> int:
    """Parse a positive minute value from CLI/user input."""
    try:
        minutes = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("minutes must be an integer") from exc
    if minutes <= 0:
        raise ValueError("minutes must be greater than zero")
    return minutes


def create_entry(next_id: int, topic: str, minutes: str | int, note: str = "") -> StudyEntry:
    """Create a validated StudyEntry from user input."""
    return StudyEntry(id=next_id, topic=topic, minutes=parse_minutes(minutes), note=note)
