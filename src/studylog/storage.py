"""JSON persistence for StudyLog entries."""

from __future__ import annotations

import json
from pathlib import Path

from studylog.model import StudyEntry, create_entry


class StudyLogStore:
    """Small JSON-backed repository for StudyEntry objects."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self) -> list[StudyEntry]:
        if not self.path.exists():
            return []
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(raw, list):
            raise ValueError("StudyLog JSON file must contain a list")
        return [StudyEntry.from_dict(item) for item in raw]

    def save(self, entries: list[StudyEntry]) -> None:
        """학습 항목 목록을 제이슨 파일에 저장합니다.

        참고: 저장 실패 상황(디스크 공간 부족, 권한 오류 등)은 현재 구현 범위 밖으로 제외합니다.
        """
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = [entry.to_dict() for entry in entries]
        self.path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def next_id(self) -> int:
        entries = self.load()
        if not entries:
            return 1
        return max(entry.id for entry in entries) + 1

    def add(self, topic: str, minutes: str | int, note: str = "") -> StudyEntry:
        entries = self.load()
        entry = create_entry(self.next_id(), topic, minutes, note)
        entries.append(entry)
        self.save(entries)
        return entry

    def complete(self, entry_id: int) -> StudyEntry | None:
        entries = self.load()
        for entry in entries:
            if entry.id == entry_id:
                entry.mark_done()
                self.save(entries)
                return entry
        return None

    def delete(self, entry_id: int) -> bool:
        entries = self.load()
        remaining = [entry for entry in entries if entry.id != entry_id]
        if len(remaining) == len(entries):
            return False
        self.save(remaining)
        return True
