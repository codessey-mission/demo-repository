import tempfile
import unittest
from pathlib import Path

from studylog.storage import StudyLogStore


class StudyLogStoreTest(unittest.TestCase):
    def test_add_persists_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StudyLogStore(Path(tmp) / "studylog.json")

            entry = store.add("Git issue", 25, "Closes syntax")
            loaded = store.load()

            self.assertEqual(entry.id, 1)
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0].topic, "Git issue")

    def test_complete_marks_existing_entry_done(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StudyLogStore(Path(tmp) / "studylog.json")
            entry = store.add("PR review", 20)

            completed = store.complete(entry.id)

            self.assertIsNotNone(completed)
            self.assertEqual(store.load()[0].status, "done")

    def test_delete_removes_existing_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StudyLogStore(Path(tmp) / "studylog.json")
            entry = store.add("stash", 10)

            deleted = store.delete(entry.id)

            self.assertTrue(deleted)
            self.assertEqual(store.load(), [])

    def test_missing_complete_returns_none(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StudyLogStore(Path(tmp) / "studylog.json")

            self.assertIsNone(store.complete(999))


if __name__ == "__main__":
    unittest.main()
