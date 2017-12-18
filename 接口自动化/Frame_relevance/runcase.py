__author__ = 'Administrator'

import mysql.connector
import configparser
from Frame_relevance.runcase_func import *

class Runcase:
    def run_Case(self, http, cnn_background, path_test_data):
        conf_test_data = configparser.ConfigParser()
        conf_test_data.read(path_test_data)

        cursor_background = cnn_background.cursor()

        #发起加标请求
        add_url = conf_test_data.get("add", "url")

        #新建一个flag变量，若值为0，则发送Get请求，若值为1，则发送POST请求
        flag = conf_test_data.get("add", "mode")
        add_data = eval(conf_test_data.get("add", "data"))

        add_memberId = add_data["memberId"]

        result = http_req_test(add_url, add_data, http, flag)

        if result["status"] == "0":
            print("新增项目失败，请核对数据")
            return False
        print(result["msg"])

        sql_select_loanId = "SELECT Id FROM loan WHERE MemberID = '%s' ORDER BY Id DESC"%add_memberId
        #print(sql_select_loanId)
        try:
            cursor_background.execute(sql_select_loanId)
        except mysql.connector.Error as e:
            print("查询标ID失败，请确认数据",e)
            return False

        list = cursor_background.fetchone()
        loanId = list[0]

        #获取审核请求url以及数据
        audit_url = conf_test_data.get("audit", "url")
        flag = conf_test_data.get("audit", "mode")
        status = conf_test_data.get("audit", "status")
        audit_data = {
            "id":loanId,
            "status":status
        }
        result = http_req_test(audit_url, audit_data, http, flag)
        if result["status"] == "0":
            print("审核失败，请确认数据")
            return False
        print(result["msg"])

        #获取注册请求数据
        register_url = conf_test_data.get("register","url")
        flag = conf_test_data.get("register", "mode")
        register_data = eval(conf_test_data.get("register","data"))
        #存储注册时的手机号，便于后续登录以及投标
        register_tel = register_data["mobilephone"]
        result = http_req_test(register_url, register_data, http, flag)

        if result["status"] == "0":
            if result["code"] == "20110":
                print("手机号已被注册")
            else:
                return False
        print(result["msg"])

        #获取登录数据
        login_url = conf_test_data.get("login","url")
        flag = conf_test_data.get("login", "mode")
        login_pwd = conf_test_data.get("login", "pwd")
        login_data = {
            "mobilephone":register_tel,
            "pwd":login_pwd
        }
        result = http_req_test(login_url, login_data, http, flag)
        if result["status"] == "0":
            print("登录失败，确认数据")
            return False
        print(result["msg"])

        #获取登录用户的memberId
        sql_select_loginUser_memberId = "SELECT Id FROM member WHERE MobilePhone = '%s'"%register_tel
        #print(sql_select_loginUser_memberId)
        try:
            cursor_background.execute(sql_select_loginUser_memberId)
        except mysql.connector.Error as e:
            print("查询登录用户ID失败，请确认数据",e)
            return False

        list = cursor_background.fetchone()
        login_memberId = list[0]

        #获取投标数据
        bidLoan_url = conf_test_data.get("bidLoan","url")
        flag = conf_test_data.get("bidLoan", "mode")
        bidLoan_amount = conf_test_data.get("bidLoan","amount")
        bidLoan_password = conf_test_data.get("bidLoan","password")
        bidLoan_data = {
            "memberId":login_memberId,
            "password":bidLoan_password,
            "loanId":loanId,
            "amount":bidLoan_amount
        }
        result = http_req_test(bidLoan_url, bidLoan_data, http, flag)
        if result["status"] == "0":
            print("登录失败，确认数据")
            return False
        print(result["msg"])

        #关闭游标
        cnn_background.close()
        #cnn_background.close()
        return True