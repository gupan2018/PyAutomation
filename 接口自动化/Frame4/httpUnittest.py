__author__ = 'Administrator'
import unittest
from HttpRequest import HttpRequest

class Http_Unittest(unittest.TestCase):
    def __init__(self, test_method, http_method, http, test_url, test_data):
        super(Http_Unittest,self).__init__(test_method)
        self.http = http
        self.test_url = test_url
        self.test_data = test_data
        self.http_method = http_method

    def test_register(self):
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            self.assertEqual(response["code"], "10001", "register请求失败")
        except AssertionError as e:
            print(str(e))

#下面是测试代码
'''
path_http = "http.conf"
http = HttpRequest(path_http)
test_Demo = Http_Unittest("test_register", "GET", http)
test_Demo.test_register()'''
