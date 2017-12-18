__author__ = 'Administrator'
import unittest
from unittest_demo.test import TestMath


#这种测试方法出错
suite = unittest.TestSuite()
suite.addTest(TestMath("test_add"))
suite.addTest(TestMath("test_sub"))
suite.addTest(TestMath("test_multi"))
suite.addTest(TestMath("test_div"))

runner = unittest.TextTestRunner()
runner.run(suite)

'''
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)'''
#    pass
