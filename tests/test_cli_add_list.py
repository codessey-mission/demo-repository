import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from studylog.cli import main


class CliAddListTest(unittest.TestCase):
    def run_cli(self, data_path: Path, *args: str) -> str:
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(["--data", str(data_path), *args])
        self.assertEqual(exit_code, 0)
        return output.getvalue()

    def test_add_and_list_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_path = Path(tmp) / "studylog.json"

            add_output = self.run_cli(data_path, "add", "GitHub Flow", "--minutes", "40", "--note", "Issue PR")
            list_output = self.run_cli(data_path, "list")

            self.assertIn("Added #1", add_output)
            self.assertIn("#1 GitHub Flow (40m) - Issue PR", list_output)

    def test_list_empty_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_path = Path(tmp) / "studylog.json"

            output = self.run_cli(data_path, "list")

            self.assertIn("No study entries yet.", output)


if __name__ == "__main__":
    unittest.main()
