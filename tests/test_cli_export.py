import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from studylog.cli import main


class CliExportTest(unittest.TestCase):
    def test_export_md_writes_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_path = Path(tmp) / "studylog.json"
            output_path = Path(tmp) / "report.md"
            main(["--data", str(data_path), "add", "Export", "--minutes", "20"])
            output = io.StringIO()

            with redirect_stdout(output):
                exit_code = main(["--data", str(data_path), "export-md", str(output_path)])

            self.assertEqual(exit_code, 0)
            self.assertTrue(output_path.exists())
            self.assertIn("# StudyLog Report", output_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
