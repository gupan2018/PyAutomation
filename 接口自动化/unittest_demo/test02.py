__author__ = 'Administrator'
import unittest

from unittest_demo.classTest import Test01


class testMath(unittest.TestCase):
    def test_add(self):
        result = Test01(1, 2).add()

        try:
            self.assertEqual(result, 2, "加法错误，请重新输入")
        except AssertionError as e:
            print("error", e)

    def test_sub(self):
        result = Test01(1, 2).sub()
        try:
            self.assertEqual(result, -1, "减法错误，请重新输入")
        except AssertionError:
            print("error")

    def test_multi(self):
        result = Test01(1, 2).multi()
        try:
            self.assertEqual(result, 2, "乘法错误，请重新输入")
        except AssertionError:
            print("error")

    def test_div(self):
        result = Test01(2, 1).div()
        try:
            self.assertEqual(result, 2, "乘法错误，请重新输入")
        except AssertionError:
            print("error")