import unittest

from studylog.model import StudyEntry, create_entry, parse_minutes


class StudyEntryModelTest(unittest.TestCase):
    def test_create_entry_strips_topic_and_note(self):
        entry = create_entry(1, "  Git branch  ", "30", "  GitHub Flow  ")

        self.assertEqual(entry.id, 1)
        self.assertEqual(entry.topic, "Git branch")
        self.assertEqual(entry.minutes, 30)
        self.assertEqual(entry.note, "GitHub Flow")
        self.assertEqual(entry.status, "todo")

    def test_mark_done_changes_status(self):
        entry = StudyEntry(id=1, topic="PR review", minutes=20)

        entry.mark_done()

        self.assertEqual(entry.status, "done")

    def test_parse_minutes_rejects_invalid_values(self):
        for value in ["0", "-1", "abc"]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_minutes(value)

    def test_round_trip_dict(self):
        entry = StudyEntry(id=2, topic="Conflict", minutes=15, note="practice")

        restored = StudyEntry.from_dict(entry.to_dict())

        self.assertEqual(restored, entry)


if __name__ == "__main__":
    unittest.main()
