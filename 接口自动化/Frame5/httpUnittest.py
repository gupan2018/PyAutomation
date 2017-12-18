__author__ = 'Administrator'
import unittest
import mysql.connector

class Http_Unittest(unittest.TestCase):
    def __init__(self, test_case_id, test_method, http_method, http, test_url, test_data, cousor):
        super(Http_Unittest,self).__init__(test_method)
        self.test_case_id = test_case_id
        self.test_method = test_method
        self.http = http
        self.test_url = test_url
        self.test_data = test_data
        self.http_method = http_method
        self.mobilephone = test_data["mobilephone"]
        self.regname = test_data["regname"]
        self.cursor = cousor

    def test_register(self):
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO test_result ' \
                         '(case_id, http_method, request_name, request_url, mobilephone, regname, test_method, test_desc, status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'register',self.test_url, self.mobilephone, self.regname, self.test_method, "测试注册接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")

        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")
        try:
            self.assertEqual(response["code"], "10001", "register请求失败")
        except AssertionError as e:
            print(str(e))
            #pass




#下面是测试代码
'''
path_http = "http.conf"
http = HttpRequest(path_http)
test_Demo = Http_Unittest("test_register", "GET", http)
test_Demo.test_register()'''
