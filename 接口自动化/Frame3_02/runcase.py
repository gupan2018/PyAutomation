__author__ = 'Administrator'

import mysql.connector
from myfunc import assemble_testList
from myfunc import exe_sql

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
            exe_sql(cursor, test_list, http)
        except mysql.connector.Error as e:
            print(e)
        finally:
                cursor.close()
                cnn.close()