__author__ = 'Administrator'

import mysql.connector
from myfunc import assemble_sql
from myfunc import store_data

class Runcase:
    def run_Case(self, http, cnn, mode):
        flag = int(mode.getMode())
        cursor = cnn.cursor()
        #定义变量组装sql语句
        sql = ''
        #定义变量，存储数据
        test_method = []
        http_data = []
        test_url = []

        #采用if语句组装sql语句
        if flag == 0:
            sql += 'SELECT * FROM test_data'
        elif flag == 1:
            #组装sql语句
            sql = assemble_sql(mode, str, sql)

        try:
            #执行sql语句
            cursor.execute(sql)
            result = cursor.fetchall()

            #存储查询到的数据
            for res in result:
                store_data(res, test_url, test_method, http_data)

        except mysql.connector.Error as e:
            print(e)
        finally:
            cursor.close()
            cnn.close()

        print("下面开始测试")
        for i in range(0, len(test_method)):
            #修改http对象中的变量
            http.reg_url = test_url[i]
            http.reg_data = http_data[i]
            #根据要求执行测试用例
            if test_method[i] == 'GET':
                http.get_req()
            elif test_method[i] == 'POST':
                http.post_req()
            else:
                print("请求方式错误，只能使用GET和POST方法")