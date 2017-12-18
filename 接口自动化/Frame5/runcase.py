__author__ = 'Administrator'

import mysql.connector
import unittest
from Frame5.runcase_func import assemble_testList
from Frame5.runcase_func import exec_select_sql
from Frame5.httpUnittest import Http_Unittest

class Runcase:
    def run_Case(self, http, cnn, mode):
        flag = int(mode.getMode())
        cursor = cnn.cursor()
        test_list = []
        response = {}
        suite = unittest.TestSuite()#定义测试集变量

        if flag == 0:
            assemble_testList(cursor, test_list)

        elif flag == 1:
            test_list.extend(mode.getList())
        else:
            print("mode.conf 中mode值配置错误，只能为0和1")

        try:
            #获取执行用例条数n，执行n条用例
            list_len = len(test_list)
            for i in range(0, list_len):
                #定义列表变量，存储查询到的数据
                data_list = []
                #执行sql语句
                exec_select_sql(cursor, test_list[i], http, data_list)

                #取用列表变量中的数据，便于后续测试
                test_url = data_list[0]
                test_data = data_list[1]
                http_method = data_list[2]
                test_method = data_list[3]

                #利用测试集进行测试
                suite.addTest(Http_Unittest(test_list[i],test_method, http_method, http, test_url, test_data, cursor))

            #利用测试集中的数据开始测试
            runner = unittest.TextTestRunner()
            runner.run(suite)

        except mysql.connector.Error as e:
            print(e)
        finally:
                cursor.close()
                cnn.close()