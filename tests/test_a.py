import unittest

from ..a import bar


class TestBar(unittest.TestCase):

    def test_letter(self):
        self.assertEqual(bar("a"), "aa")

    def test_letter2(self):
        self.assertEqual(bar("a", 3), "aaa")
