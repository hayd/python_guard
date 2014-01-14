import unittest

from python_guard.b.c import fib


class TestFib(unittest.TestCase):

    def test_fib0(self):
        self.assertEqual(fib(0), 1)

    def test_fib1(self):
        self.assertEqual(fib(1), 1)

    def test_fib2(self):
        self.assertEqual(fib(2), 2)

    def test_fib3(self):
        self.assertEqual(fib(3), 3)
