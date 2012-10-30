import unittest
import os
import gitconfig
from gitconfig.shell import shell


class test(unittest.TestCase):
    filename = None
    config = None

    @classmethod
    def setUpClass(cls):
        cls.filename = os.path.expanduser("~/.gitconfig_test")
        if os.path.exists(cls.filename):
            os.unlink(cls.filename)
        cls.config = gitconfig.config("~/.gitconfig_test")

    def test_filename(self):
        self.assertEqual(self.filename, self.config.filename)

    def test_exists(self):
        self.assertEqual(os.path.exists(self.filename), self.config.exists)

    def test_emptylist(self):
        self.assertEqual(self.config.list, [])

    def test_set(self):
        self.config.section.key = "value"
        self.assertEqual(self.config.section.key, "value")
        self.config.set("section", "key", "value")
        self.assertEqual(self.config.get("section", "key"), "value")
        command = "git config --file %s --list" % self.filename
        lines = shell(command).splitlines()
        self.assertEqual(self.config.list, lines)

    def test_get(self):
        self.assertEqual(self.config.not_exists.not_exists, None)
        self.assertEqual(self.config.get("not_exists", "not_exists"), None)

    def test_unset(self):
        self.config.section.key = "value"
        self.assertEqual(self.config.section.key, "value")
        self.config.unset("section", "key")
        self.assertEqual(self.config.section.key, None)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.filename):
            os.unlink(cls.filename)

if __name__ == "__main__":
    unittest.main()