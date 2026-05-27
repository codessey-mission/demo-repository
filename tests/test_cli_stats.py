import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from studylog.cli import main


class CliStatsTest(unittest.TestCase):
    def test_stats_command_prints_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_path = Path(tmp) / "studylog.json"
            main(["--data", str(data_path), "add", "Merge", "--minutes", "30"])
            main(["--data", str(data_path), "complete", "1"])
            output = io.StringIO()

            with redirect_stdout(output):
                exit_code = main(["--data", str(data_path), "stats"])

            self.assertEqual(exit_code, 0)
            self.assertIn("Total entries: 1", output.getvalue())
            self.assertIn("Done minutes: 30", output.getvalue())


if __name__ == "__main__":
    unittest.main()
