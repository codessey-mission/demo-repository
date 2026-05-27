import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from studylog.cli import main


class CliCompleteDeleteTest(unittest.TestCase):
    def run_cli(self, data_path: Path, *args: str) -> tuple[int, str]:
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(["--data", str(data_path), *args])
        return exit_code, output.getvalue()

    def test_complete_marks_entry_done(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_path = Path(tmp) / "studylog.json"
            self.run_cli(data_path, "add", "Review", "--minutes", "15")

            exit_code, complete_output = self.run_cli(data_path, "complete", "1")
            _, list_output = self.run_cli(data_path, "list")

            self.assertEqual(exit_code, 0)
            self.assertIn("Completed #1", complete_output)
            self.assertIn("[✓] #1 Review", list_output)

    def test_delete_removes_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_path = Path(tmp) / "studylog.json"
            self.run_cli(data_path, "add", "Reset soft", "--minutes", "10")

            exit_code, delete_output = self.run_cli(data_path, "delete", "1")
            _, list_output = self.run_cli(data_path, "list")

            self.assertEqual(exit_code, 0)
            self.assertIn("Deleted #1", delete_output)
            self.assertIn("No study entries yet.", list_output)

    def test_missing_id_returns_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_path = Path(tmp) / "studylog.json"

            exit_code, output = self.run_cli(data_path, "complete", "999")

            self.assertEqual(exit_code, 1)
            self.assertIn("was not found", output)


if __name__ == "__main__":
    unittest.main()
