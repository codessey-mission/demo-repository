import unittest

import studylog


class BootstrapTest(unittest.TestCase):
    def test_package_has_version(self):
        self.assertEqual(studylog.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
