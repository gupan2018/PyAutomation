__author__ = 'Administrator'

import mysql.connector
from Frame3_03.myfunc import assemble_testList
from Frame3_03.myfunc import exe_sql
from Frame3_03.myfunc import test_begin

class Runcase:
    def run_Case(self, http, cnn, mode):
        flag = int(mode.getMode())
        cursor = cnn.cursor()
        test_list = []

        if flag == 0:
            try:
                assemble_testList(cursor, test_list)
            except mysql.connector.Error as e:#执行数据库操作，操作失败后关闭，若数据库操作成功后也关闭会影响后续代码执行
                print("组装查询id列表失败，错误原因如下：\n",e)
                cursor.close()
                cnn.close()

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
                exe_sql(cursor, test_list[i], http, data_list)

                #取用列表变量中的数据，便于后续测试
                test_url = data_list[0]
                test_data = data_list[1]
                test_method = data_list[2]

                #开始测试
                test_begin(test_method, http, test_url, test_data)

        except mysql.connector.Error as e:
            print(e)
        finally:
                cursor.close()
                cnn.close()