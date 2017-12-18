__author__ = 'Administrator'
import mysql.connector
from datetime import datetime
import time

'''
#组装查询列表
assemble_testList(cursor, test_list)
#根据列表数据，执行对应sql
exe_sql(cursor, test_list, http)
'''

def assemble_testList(cursor, test_list):
    #request_name = 'getFinanceLogList'
    #sql = "SELECT case_id FROM ygg_test_data WHERE request_name = '%s'"%request_name

    #在存储测试用例的表中搜索case_id的数值，并将搜索结果以列表的形式返回
    sql = "SELECT case_id FROM ygg_test_data02"
    try:
        cursor.execute(sql)
    except mysql.connector.Error as e:
        print("组装查询id列表失败，错误原因如下：\n",e)

    #将要测试测case_id放到列表中
    list = cursor.fetchall()
    for record in list:
        test_list.append(record[0])

#执行sql语句
#测试数据都是放在数据库中，定义这个函数是为了从数据库中拿取测试数据，并将其放在datalist中
def exec_select_sql(cursor, test_case, http, datalist):
        #查询对应case_id中的所有字段的数值，利用fetchone()函数存储在list中，便于取用
        sql = 'SELECT * FROM ygg_test_data02 WHERE case_id = %s'%test_case
        try:
            cursor.execute(sql)
        except mysql.connector.Error as e:
            print(e)

        list = cursor.fetchone()

        #执行sql语句，查询对应case_id要测试的请求，根据请求名执行不同的存储数据操作
        sql = "SELECT request_name FROM ygg_test_data02 WHERE case_id = %s"%test_case
        try:
            cursor.execute(sql)
        except mysql.connector.Error as e:
            print(e)

        request_name = cursor.fetchone()[0]
        #print(request_name)

        #将公用的请求先存储公用的请求数据，差异化的存储数据根据req_name的不同进行存储
        test_url = list[3]
        http_method = list[1]
        test_method = list[17]

        #不同的请求所需要的测试数据不一样，以request_name为标识，按不同的request_name封装不同的测试数据
        if request_name == 'register':
            mobilephone = list[4]
            regname = list[5]
            test_data = {
                "mobilephone":mobilephone,
                "regname":regname,
                "pwd":"123456"
            }
            datalist.append(test_data)

        elif request_name == 'login':
            mobile_phone = list[4]
            test_data = {
                "mobilephone":mobile_phone,
                "pwd":"123456"
            }
            datalist.append(test_data)

        elif request_name == 'recharge':
            mobile_phone = list[4]
            amount = list[7]
            test_data = {
                "mobilephone":mobile_phone,
                "amount":amount
            }
            datalist.append(test_data)

        elif request_name == 'withdraw':
            mobile_phone = list[4]
            amount = list[7]
            test_data = {
                "mobilephone":mobile_phone,
                "amount":amount
            }
            datalist.append(test_data)

        elif request_name == 'list':
            test_data = {}
            datalist.append(test_data)

        elif request_name == 'bidLoan':
            memberId = list[8]
            amount = list[7]
            password = '123456'
            loanId = '1000'

            test_data = {
                "memberId":memberId,
                "amount":amount,
                "password":password,
                "loanId":loanId
            }
            datalist.append(test_data)

        elif request_name == 'add':
            memberId = list[8]
            amount = list[7]
            title = list[9]
            loanRate = list[10]
            loanTerm = list[11]
            loanDateType = list[12]
            repaymemtWay = list[13]
            biddingDays = list[14]

            test_data = {
                "memberId":memberId,
                "amount":amount,
                "title":title,
                "loanRate":loanRate,
                "loanTerm":loanTerm,
                "loanDateType":loanDateType,
                "repaymemtWay":repaymemtWay,
                "biddingDays":biddingDays
            }
            datalist.append(test_data)

        elif request_name == 'audit':
            id = list[15]
            status = list[16]
            test_data = {
                "id":id,
                "status":status
            }
            datalist.append(test_data)

        elif request_name == 'getLoanList':
            test_data = {}
            datalist.append(test_data)

        elif request_name == 'getInvestsByMemberId':
            memberId = list[8]
            test_data = {
                "memberId":memberId
            }
            datalist.append(test_data)

        elif request_name == 'generateRepayments':
            id = list[15]
            test_data = {
                "id":id
            }
            datalist.append(test_data)

        elif request_name == 'getInvestsByLoanId':
            loanId = list[15]
            test_data = {
                "loanId":loanId
            }
            datalist.append(test_data)

        elif request_name == 'getFinanceLogList':
            memberId = list[8]
            test_data = {
                "memberId":memberId
            }
            datalist.append(test_data)

        #将测试数据全存储到test_data中
        datalist.append(test_url)
        datalist.append(http_method)
        datalist.append(test_method)

def test_begin(test_method, http, test_url, test_data):
    #根据不同的请求方式，进行不同类型的http请求的测试
    if test_method == "GET":
        http.get_req(test_url, test_data)
    elif test_method == "POST":
        http.post_req(test_url, test_data)
    else:
        print("test_method错误，只支持POST和GET方法")

def print_test_report(start_time, HtmlReport, cursor):
    end_time = datetime.now()
    run_time = end_time - start_time
    html_report = HtmlReport(cursor)
    html_report.set_time_took(str(run_time))
    html_report.generate_html("前程贷接口测试报告", "圆滚滚的测试报告" + str(time.time())+ ".html")
    #用str(time.time())占位，否则输出文件名格式出错