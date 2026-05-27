import unittest

from studylog.model import StudyEntry
from studylog.stats import calculate_stats, format_stats


class StudyStatsTest(unittest.TestCase):
    def test_calculate_stats(self):
        entries = [
            StudyEntry(id=1, topic="Issue", minutes=10, status="done"),
            StudyEntry(id=2, topic="PR", minutes=20, status="todo"),
        ]

        stats = calculate_stats(entries)

        self.assertEqual(stats.total_entries, 2)
        self.assertEqual(stats.done_entries, 1)
        self.assertEqual(stats.todo_entries, 1)
        self.assertEqual(stats.total_minutes, 30)
        self.assertEqual(stats.done_minutes, 10)
        self.assertEqual(stats.completion_rate, 0.5)

    def test_format_stats(self):
        stats = calculate_stats([StudyEntry(id=1, topic="Review", minutes=30, status="done")])

        output = format_stats(stats)

        self.assertIn("Total entries: 1", output)
        self.assertIn("Completion rate: 100.0%", output)


if __name__ == "__main__":
    unittest.main()
