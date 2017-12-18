__author__ = 'Administrator'
import unittest
import mysql.connector
from Frame_db.HttpRequest import HttpRequest

class Http_Unittest(unittest.TestCase):
    def __init__(self, test_case_id, test_method, http_method, http, test_url, test_data, cousor):
        #初始化函数中获取到想要查询测
        super(Http_Unittest,self).__init__(test_method)

        self.test_case_id = test_case_id
        self.test_method = test_method
        self.http = http
        self.test_url = test_url
        self.test_data = test_data
        self.http_method = http_method
        self.cursor = cousor

    def test_register(self):
        mobilephone = self.test_data["mobilephone"]
        regname = self.test_data["regname"]

        #根据HTTP方法进行对应的HTTP请求，将对应的请求的结果放到对应的response中
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")

        #组装插入数据的sql语句，将测试结果插入到存储测试结果的数据表中
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, mobilephone, regname, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'register',self.test_url, mobilephone, regname, self.test_method, "测试注册接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except Exception as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "register请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_login(self):
        mobilephone = self.test_data["mobilephone"]
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, mobilephone, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'login',self.test_url, mobilephone, self.test_method, "测试登录接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "login请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_recharge(self):
        mobilephone = self.test_data["mobilephone"]
        amount = self.test_data["amount"]

        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, mobilephone, amount, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'recharge',self.test_url, mobilephone, amount, self.test_method, "测试充值接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "recharge请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_withdraw(self):
        mobilephone = self.test_data["mobilephone"]
        amount = self.test_data["amount"]

        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, mobilephone, amount, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'withdraw',self.test_url, mobilephone, amount, self.test_method, "测试提现接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "withdraw请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_bidLoan(self):
        amount = self.test_data["amount"]
        memberId = self.test_data["memberId"]
        password = self.test_data["password"]

        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, test_method, amount, memberId, pwd, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'bidLoan',self.test_url, self.test_method, amount, memberId, password, "测试投标/竞标接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "bidLoan请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_list(self):
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'list',self.test_url, self.test_method, "测试获取用户列表接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "list请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_add(self):
        amount = self.test_data["amount"]
        memberId = self.test_data["memberId"]
        title = self.test_data["title"]
        loanRate = self.test_data["loanRate"]
        loanTerm = self.test_data["loanTerm"]
        loanDateType = self.test_data["loanDateType"]
        repaymemtWay = self.test_data["repaymemtWay"]
        biddingDays = self.test_data["biddingDays"]

        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, test_method, amount, memberId, title, loanRate, loanTerm, loanDateType, repaymemtWay, biddingDays, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'bidLoan',self.test_url, self.test_method, amount, memberId, title, loanRate, loanTerm, loanDateType, repaymemtWay, biddingDays, "测试增加项目接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "add请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_audit(self):
        id = self.test_data["id"]
        status = self.test_data["status"]

        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, id, status, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'audit',self.test_url, id, status, self.test_method, "测试审核接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except Exception as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "audit请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_getLoanList(self):
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'getLoanList',self.test_url, self.test_method, "测试获取标列表接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except Exception as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "getLoanList请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_generateRepayments(self):
        id = self.test_data["id"]
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, test_method, id, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'generateRepayments',self.test_url, self.test_method, id, "测试生成回款计划接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except Exception as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "generateRepayments请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_getInvestsByMemberId(self):
        memberId = self.test_data["memberId"]
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, memberId, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'getInvestsByMemberId',self.test_url, memberId, self.test_method, "测试获取用户所有投资记录接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "getInvestsByMemberId请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_getInvestsByLoanId(self):
        loanId = self.test_data["loanId"]
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, id, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'getInvestsByLoanId',self.test_url, loanId, self.test_method, "测试获取标的所有投资记录接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "getInvestsByLoanId请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

    def test_getFinanceLogList(self):
        memberId = self.test_data["memberId"]
        if self.http_method == "GET":
            response = self.http.get_req(self.test_url, self.test_data)
        elif self.http_method == "POST":
            response = self.http.post_req(self.test_url, self.test_data)
        else:
            print("error in class Http_Unittest")
        try:
            #将执行结果存到数据库中
            sql_insert = 'INSERT INTO ygg_test_result02 ' \
                         '(case_id, http_method, request_name, request_url, memberId, test_method, test_desc, result_status, code, msg) ' \
                         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_data = (self.test_case_id, self.http_method ,'getFinanceLogList',self.test_url, memberId, self.test_method, "测试获取用户流水接口",response["status"], response["code"], response["msg"])
            self.cursor.execute(sql_insert, insert_data)
            self.cursor.execute("commit")
        except mysql.connector.Error as e:
            print(e)
            self.cursor.execute("rollback")

        try:
            self.assertEqual(response["code"], "10001", "getFinanceLogList请求失败")
        except AssertionError as e:
            print(str(e))
            #pass

#下面是测试代码
'''
path_http = "http.conf"
http = HttpRequest(path_http)
test_Demo = Http_Unittest("test_register", "GET", http)
test_Demo.test_register()'''
