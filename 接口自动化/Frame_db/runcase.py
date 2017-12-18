__author__ = 'Administrator'

import mysql.connector
import unittest
from datetime import datetime
from Frame_db.runcase_func import assemble_testList
from Frame_db.runcase_func import exec_select_sql
from Frame_db.httpUnittest import Http_Unittest
from Frame_db.html_report import HtmlReport
import time
from Frame_db.runcase_func import print_test_report

class Runcase:
    def run_Case(self, http, cnn, mode, start_time):
        #生成游标
        cursor = cnn.cursor()

        #获取mode值，根据mode值确定执行测试用例的方式
        flag = int(mode.getMode())

        #定义test_list列表变量，用于存储要执行的测试用例的编号
        test_list = []
        suite = unittest.TestSuite()#定义测试集变量

        #flag=0时，测试所有的测试用例
        if flag == 0:
            assemble_testList(cursor, test_list)

        #flag=1时，测试指定编号的测试用例
        elif flag == 1:
            test_list.extend(mode.getList())
        else:
            print("mode.conf 中mode值配置错误，只能为0和1")

        #获取需要执行的测试用例的条数
        test_len = len(test_list)

        #获取执行用例条数n，执行n条用例
        for i in range(0, test_len):
            #定义列表变量，存储查询到的数据
            data_list = []
            #执行sql语句，从存储测试用例的表中拿取测试用例，并将这些数据存储在data_liat中
            '''
            cxec_select_sql中传入各参数的含义如下：
            cursor：操作数据库的游标
            test_list[i]：需要执行的测试用例编号
            data_list：列表形式数据，用于存储测试数据
            http：没用
            '''
            exec_select_sql(cursor, test_list[i], http, data_list)

            #取用列表变量中的数据，便于后续测试
            test_data = data_list[0]
            test_url = data_list[1]
            http_method = data_list[2]
            test_method = data_list[3]

            #利用将测试数据添加到测试集中
            print(test_url, test_method)

            '''
            将测试用例添加到测试集中，函数参数含义如下：
            test_list[i]：需要测试的测试用例编号
            test_method：格式为test_*，根据这个参数确定要执行哪一个单元测试函数
            http_method：需要测试Get还是POST方法
            http：http对象，里面封装了发送GET请求和POST请求的方法
            test_url：每个测试模块对应的url
            test_data：测试数据
            cursor：操作数据库的游标
            '''
            suite.addTest(Http_Unittest(test_list[i],test_method, http_method, http, test_url, test_data, cursor))

        #利用测试集中的数据开始测试
        runner = unittest.TextTestRunner()
        runner.run(suite)

        #打印测试报告
        print_test_report(start_time, HtmlReport, cursor)

        #关闭游标
        cursor.close()
        cnn.close()