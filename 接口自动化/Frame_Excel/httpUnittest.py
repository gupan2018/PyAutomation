__author__ = 'Administrator'
import unittest
import mysql.connector
from Frame_db.HttpRequest import HttpRequest
import configparser

path_urls = "test_urls.conf"

class Http_Unittest(unittest.TestCase):
    def __init__(self, test_case_id, http, test_method, sheet_obj_read, sheet_obj_write):
        super(Http_Unittest,self).__init__(test_method)
        conf = configparser.ConfigParser()
        conf.read(path_urls)
        self.test_case_id = test_case_id
        self.test_method = test_method
        self.http = http
        req_name = sheet_obj_read.cell_value(test_case_id, 0)
        print(req_name)

        #根据测试的req_name获取对应的url
        self.test_url = conf.get("url",req_name)
        self.sheet_obj_read = sheet_obj_read
        self.sheet_obj_write = sheet_obj_write

    def test_register(self):
        #读取测试结果并组装请求数据
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        mobilephone = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 2)))
        regname = self.sheet_obj_read.cell_value(self.test_case_id, 3)
        pwd = '123456'
        test_method = self.test_method
        test_desc = "测试注册接口"
        response = {}

        test_data = {
            "mobilephone":mobilephone,
            "regname":regname,
            "pwd":pwd
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        #写入测试结果
        self.sheet_obj_write.write(self.test_case_id, 0, "register")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 2, mobilephone)
        self.sheet_obj_write.write(self.test_case_id, 3, regname)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_login(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        mobilephone = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 2)))
        pwd = '123456'

        test_method = self.test_method
        test_desc = "测试登录接口"
        response = {}

        test_data = {
            "mobilephone":mobilephone,
            "pwd":pwd
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "login")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 2, mobilephone)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)


    def test_recharge(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        mobilephone = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 2)))
        amount = self.sheet_obj_read.cell_value(self.test_case_id, 4)
        test_method = self.test_method
        test_desc = "测试充值接口"
        response = {}

        test_data = {
            "mobilephone":mobilephone,
            "amount":amount
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "recharge")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 2, mobilephone)
        self.sheet_obj_write.write(self.test_case_id, 4, amount)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)


    def test_withdraw(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        mobilephone = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 2)))
        amount = self.sheet_obj_read.cell_value(self.test_case_id, 4)
        test_method = self.test_method
        test_desc = "测试提现接口"
        response = {}

        test_data = {
            "mobilephone":mobilephone,
            "amount":amount
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "withdraw")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 2, mobilephone)
        self.sheet_obj_write.write(self.test_case_id, 4, amount)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_list(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        test_method = self.test_method
        test_desc = "测试获取用户列表接口"
        response = {}
        test_data = {}

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "list")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_bidLoan(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        amount = self.sheet_obj_read.cell_value(self.test_case_id, 4)
        memberId = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 5)))
        pwd = '123456'
        loanId = 1
        test_method = self.test_method
        test_desc = "测试投标/竞标接口"
        response = {}

        test_data = {
            "amount":amount,
            "memberId":memberId,
            "pwd":pwd,
            "loanId":loanId
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "bidLoan")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 4, amount)
        self.sheet_obj_write.write(self.test_case_id, 5, memberId)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_add(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        amount = self.sheet_obj_read.cell_value(self.test_case_id, 4)
        memberId = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 5)))
        title = self.sheet_obj_read.cell_value(self.test_case_id, 6)
        loanRate = self.sheet_obj_read.cell_value(self.test_case_id, 7)
        loanTerm = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 8)))
        loanDateType = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 9)))
        repaymemtWay = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 10)))
        biddingDays = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 11)))

        test_method = self.test_method
        test_desc = "测试新增项目接口"
        response = {}

        test_data = {
            "amount":amount,
            "memberId":memberId,
            "title":title,
            "loanRate":loanRate,
            "loanTerm":loanTerm,
            "loanDateType":loanDateType,
            "repaymemtWay":repaymemtWay,
            "biddingDays":biddingDays
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "add")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 4, amount)
        self.sheet_obj_write.write(self.test_case_id, 5, memberId)
        self.sheet_obj_write.write(self.test_case_id, 6, title)
        self.sheet_obj_write.write(self.test_case_id, 7, loanRate)
        self.sheet_obj_write.write(self.test_case_id, 8, loanTerm)
        self.sheet_obj_write.write(self.test_case_id, 9, loanDateType)
        self.sheet_obj_write.write(self.test_case_id, 10, repaymemtWay)
        self.sheet_obj_write.write(self.test_case_id, 11, biddingDays)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_audit(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        id = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 12)))
        status = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 13)))

        test_method = self.test_method
        test_desc = "测试审核接口"
        response = {}

        test_data = {
            "id":id,
            "status":status
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "audit")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 12, id)
        self.sheet_obj_write.write(self.test_case_id, 13, status)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_getLoanList(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        test_method = self.test_method
        test_desc = "测试生成标列表接口"
        response = {}

        test_data = {}

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "getLoanList")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_generateRepayments(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        id = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 12)))
        test_method = self.test_method
        test_desc = "测试生成回款计划接口"
        response = {}

        test_data = {
            "id":id
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "generateRepayments")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 12, id)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_getInvestsByMemberId(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        memberId = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 5)))
        test_method = self.test_method
        test_desc = "测试获取用户所有投资记录接口"
        response = {}

        test_data = {
            "memberId":memberId,
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "getInvestsByMemberId")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 5, memberId)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_getInvestsByLoanId(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        loanId = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 12)))
        test_method = self.test_method
        test_desc = "测试获取标的所有投资记录接口"
        response = {}

        test_data = {
            "loanId":loanId,
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "getInvestsByLoanId")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 12, loanId)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

    def test_getFinanceLogList(self):
        http_method = self.sheet_obj_read.cell_value(self.test_case_id, 1)
        memberId = str(int(self.sheet_obj_read.cell_value(self.test_case_id, 5)))
        test_method = self.test_method
        test_desc = "测试获取用户流水记录接口"
        response = {}

        test_data = {
            "memberId":memberId
        }

        if http_method == "GET":
            response = self.http.get_req(self.test_url, test_data)
        elif http_method == "POST":
            response = self.http.post_req(self.test_url, test_data)
        else:
            print("error in class Http_Unittest")

        res_status = response["status"]
        res_code = response["code"]
        res_msg = response["msg"]

        self.sheet_obj_write.write(self.test_case_id, 0, "getFinanceLogList")
        self.sheet_obj_write.write(self.test_case_id, 1, http_method)
        self.sheet_obj_write.write(self.test_case_id, 5, memberId)
        self.sheet_obj_write.write(self.test_case_id, 14, test_method)
        self.sheet_obj_write.write(self.test_case_id, 15, test_desc)
        self.sheet_obj_write.write(self.test_case_id, 16, res_status)
        self.sheet_obj_write.write(self.test_case_id, 17, res_code)
        self.sheet_obj_write.write(self.test_case_id, 18, res_msg)

#下面是测试代码
'''
path_http = "http.conf"
http = HttpRequest(path_http)
test_Demo = Http_Unittest("test_register", "GET", http)
test_Demo.test_register()'''
