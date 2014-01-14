import unittest

from ..c import fib


class TestFib(unittest.TestCase):

    def test_fib0(self):
        self.assertEqual(fib(0), 1)

    def test_fib1(self):
        self.assertEqual(fib(1), 1)

    def test_fib2(self):
        self.assertEqual(fib(2), 2)

    def test_fib3(self):
        self.assertEqual(fib(3), 3)

    # Note: I'm making this up to 8 tests,
    # so I can count which tests are being run

    def test_fib4(self):
        self.assertEqual(fib(0), 1)

    def test_fib5(self):
        self.assertEqual(fib(1), 1)

    def test_fib6(self):
        self.assertEqual(fib(2), 2)

    def test_fib7(self):
        self.assertEqual(fib(3), 3)
