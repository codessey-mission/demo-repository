import unittest

from studylog.export import render_markdown_report
from studylog.model import StudyEntry


class MarkdownExportTest(unittest.TestCase):
    def test_render_markdown_report(self):
        entries = [StudyEntry(id=1, topic="Conflict", minutes=25, status="done", note="same hunk")]

        report = render_markdown_report(entries)

        self.assertIn("# StudyLog Report", report)
        self.assertIn("Total entries: 1", report)
        self.assertIn("[✓] #1 Conflict (25m) - same hunk", report)

    def test_empty_report(self):
        report = render_markdown_report([])

        self.assertIn("No study entries yet.", report)


if __name__ == "__main__":
    unittest.main()
