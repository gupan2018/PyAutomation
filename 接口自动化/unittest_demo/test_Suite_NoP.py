__author__ = 'Administrator'
import unittest
from unittest_demo.test02 import testMath

suite = unittest.TestSuite()
suite.addTest(testMath("test_add"))
suite.addTest(testMath("test_sub"))

runner = unittest.TextTestRunner()
runner.run(suite)