import unittest
from gitconfig.shell import shell


class TestCase(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(shell("echo 1"), "1")

    def test_error(self):
        self.assertRaises(SystemError, shell, "error")


if __name__ == "__main__":
    unittest.main()