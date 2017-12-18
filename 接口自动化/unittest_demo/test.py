import unittest

from parameterized import parameterized

from unittest_demo.classTest import Test01


class TestMath(unittest.TestCase):
    @parameterized.expand([
        ("0", 1, 2, 3),
        ("1", 23, 21, 44),
        ("2", 33., 21, 54),
        ("4", 19, 10, 29),
    ])

    def test_add(self, name, a, b, c):
        try:
            self.assertEqual(Test01(a, b).add(), c)
        except AssertionError:
            print("计算结果与预期不符:",name)

    @parameterized.expand([
        ("5", 3, 2, 1),
        ("6", 7, 5, 2),
        ("7", 9, 1, 8),
    ])

    def test_sub(self, name, a, b, c):
        print(name, a, b, c)
        try:
            self.assertEqual(Test01(a, b).sub(), c)
        except AssertionError:
            print("计算结果与预期不符{}", name)

    @parameterized.expand([
        ("8", 19, 10, 190),
        ("9", 1, 2, 2),
        ("10", 2, 6, 12),
    ])

    def test_multi(self, name, a, b, c):
        try:
            self.assertEqual(Test01(a, b).multi(), c)
        except AssertionError:
            print("计算结果与预期不符{}", name)

    @parameterized.expand([
        ("11", 11, 1, 11),
        ("12", 12, 2, 6),
        ("13", 20, 4, 5),
    ])

    def test_div(self, name, a, b, c):
        try:
            self.assertEqual(Test01(a, b).div(), c)
        except AssertionError:
            print("计算结果与预期不符{}", name)