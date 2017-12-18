__author__ = 'Administrator'
import configparser
import mysql.connector

class RunCase():
    def __init__(self, path, cousor, wb):
        self.__path = path
        self.cousor = cousor
        self.read_wb = wb.getReadWb()
        self.write_wb = wb.getWriteWb()

    def runcase(self):
        insert_sql = ''
        test_data = ''
        conf = configparser.ConfigParser()
        conf.read(self.__path)

        read_sheet_obj = self.read_wb.sheets()[0]
        read_sheet_rows = read_sheet_obj.nrows
        read_sheet_cols = read_sheet_obj.ncols
        print(read_sheet_rows, read_sheet_cols)

        for row in range(1, read_sheet_rows):
            if read_sheet_obj.cell_value(row, 0) == "register":
                request_name = "register"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "register")
                mobile_phone = int(read_sheet_obj.cell_value(row, 2))
                regname = read_sheet_obj.cell_value(row, 3)
                test_method = 'test_register'
                test_desc = '测试注册接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, mobilephone, regname, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, mobile_phone, regname, test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "login":
                request_name = "login"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "login")
                mobile_phone = int(read_sheet_obj.cell_value(row, 2))
                test_method = 'test_login'
                test_desc = '测试登录接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, mobilephone, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, mobile_phone, test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "recharge":
                request_name = "recharge"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "recharge")
                mobile_phone = int(read_sheet_obj.cell_value(row, 2))
                amount = read_sheet_obj.cell_value(row, 4)
                test_method = 'test_recharge'
                test_desc = '测试充值接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, mobilephone, amount, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, mobile_phone, amount, test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "withdraw":
                request_name = "withdraw"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "withdraw")
                mobile_phone = int(read_sheet_obj.cell_value(row, 2))
                amount = read_sheet_obj.cell_value(row, 4)
                test_method = 'test_withdraw'
                test_desc = '测试提现接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, mobilephone, amount, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, mobile_phone, amount, test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "list":
                request_name = "list"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "list")
                test_method = 'test_list'
                test_desc = '测试获取用户列表接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "bidLoan":
                request_name = "bidLoan"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "bidLoan")
                amount = str(int(read_sheet_obj.cell_value(row, 4)))
                memberId = str(int(read_sheet_obj.cell_value(row, 5)))
                test_method = 'test_bidLoan'
                test_desc = '测试投标/竞标接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, amount, memberId, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, amount,memberId,test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "add":
                request_name = "add"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "add")
                amount = str(int(read_sheet_obj.cell_value(row, 4)))
                memberId = str(int(read_sheet_obj.cell_value(row, 5)))
                title = read_sheet_obj.cell_value(row, 6)
                loanRate = read_sheet_obj.cell_value(row, 7)
                loanTerm = str(int(read_sheet_obj.cell_value(row, 8)))
                loanDateType = str(int(read_sheet_obj.cell_value(row, 9)))
                repaymemtWay = str(int(read_sheet_obj.cell_value(row, 10)))
                biddingDays = str(int(read_sheet_obj.cell_value(row, 11)))

                test_method = 'test_add'
                test_desc = '测试新增项目接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, amount, memberId, title, loanRate, loanTerm, loanDateType, repaymemtWay, biddingDays, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, amount,memberId, title, loanRate, loanTerm, loanDateType, repaymemtWay, biddingDays,test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "audit":
                request_name = "audit"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "audit")
                id = str(int(read_sheet_obj.cell_value(row, 12)))
                status = str(int(read_sheet_obj.cell_value(row, 13)))
                test_method = 'test_audit'
                test_desc = '测试审核接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, id, status, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, id,status,test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "getLoanList":
                request_name = "getLoanList"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "getLoanList")
                test_method = 'test_getLoanList'
                test_desc = '测试生成标列表接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "generateRepayments":
                request_name = "generateRepayments"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "generateRepayments")
                id = str(int(read_sheet_obj.cell_value(row, 12)))
                test_method = 'test_generateRepayments'
                test_desc = '测试生成回款计划接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, id, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, id,test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "getInvestsByMemberId":
                request_name = "getInvestsByMemberId"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "getInvestsByMemberId")
                memberId = str(int(read_sheet_obj.cell_value(row, 5)))
                test_method = 'test_getInvestsByMemberId'
                test_desc = '测试获取用户所有投资记录接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, memberId, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, memberId,test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "getInvestsByLoanId":
                request_name = "getInvestsByLoanId"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "getInvestsByLoanId")
                id = str(int(read_sheet_obj.cell_value(row, 12)))
                test_method = 'test_getInvestsByLoanId'
                test_desc = '测试获取标的所有投资记录接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, id, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, id,test_method, test_desc)
                print(insert_sql%test_data)

            elif read_sheet_obj.cell_value(row, 0) == "getFinanceLogList":
                request_name = "getFinanceLogList"
                http_method = read_sheet_obj.cell_value(row, 1)
                request_url = conf.get("url", "getFinanceLogList")
                memberId = str(int(read_sheet_obj.cell_value(row, 5)))
                test_method = 'test_getFinanceLogList'
                test_desc = '测试获取用户流水记录接口'
                insert_sql = 'INSERT INTO ygg_test_data02 (http_method, request_name, request_url, memberId, test_method, test_desc)' \
                             ' VALUES ' \
                             '(%s, %s, %s, %s, %s, %s)'
                test_data = (http_method, request_name, request_url, memberId,test_method, test_desc)
                print(insert_sql%test_data)

            try:
                self.cousor.execute(insert_sql, test_data)
                self.cousor.execute("commit")
            except mysql.connector.Error as e:
                print(e)
                self.cousor.execute("rollback")


