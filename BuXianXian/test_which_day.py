from unittest import TestCase
import unittest
from buxianxian23 import which_day


class TestWhich_day(TestCase):
    def test_which_day1(self):
        self.assertEqual(1, which_day(2000, 1, 1))

    def test_which_day2(self):
        self.assertEqual(32, which_day(2000, 2, 1))

    def test_which_day3(self):
        self.assertEqual(61, which_day(2000, 3, 1))

    def test_which_day4(self):
        self.assertEqual(92, which_day(2000, 4, 1))


if __name__ == '__main__':
    unittest.main()
    bool()
