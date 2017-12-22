# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)

from conf import settings
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.sendEmail import SendEmail
import time
import os
import time

def new_report(report_dir):
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
    file_new = os.path.join(report_dir, lists[-1])
    return file_new

def run():
    format_time = "%Y-%m-%d %H_%M_%S"
    report_dir = settings.BASE_DIR + '\\report'
    report_path = settings.BASE_DIR + '\\report\\%stest_sinaemail.html' % time.strftime(format_time)
    discover = unittest.defaultTestLoader.discover(settings.BASE_DIR + '\\core\\testCases', pattern='test*.py')
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='新浪邮箱测试报告',
        description='测试用例执行情况：'
    )

    runner.run(discover)
    fp.close()

    email_op_obj = SendEmail('完成测试用例执行')
    # email_op_obj.add_text("test for send text")
    report = new_report(report_dir)
    email_op_obj.add_file_content(report)
    email_op_obj.send_email()