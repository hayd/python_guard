import unittest

from python_guard.a import bar


class TestBar(unittest.TestCase):

    def test_letter(self):
        self.assertEqual(bar("a"), "aa")
        self.assertEqual(bar("a", 3), "aaa")
