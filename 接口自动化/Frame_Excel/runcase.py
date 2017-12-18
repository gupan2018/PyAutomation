__author__ = 'Administrator'

import mysql.connector
import unittest
from Frame_Excel.runcase_func import assemble_testList
from Frame_Excel.httpUnittest import Http_Unittest

class Runcase:
    def run_Case(self, http, wb, mode):

        wb_read = wb.getReadWb()
        wb_write = wb.getWriteWb()

        #读取第一张Excel文件中的第一张表
        sheet_obj_read = wb_read.sheets()[0]

        #将测试结果存储Excel中
        sheet_obj_write = wb_write.add_sheet("test_result")

        flag = int(mode.getMode())
        test_list = []

        suite = unittest.TestSuite()#定义测试集变量

        if flag == 0:
            test_Num = sheet_obj_read.nrows
            assemble_testList(test_Num, test_list)

        elif flag == 1:
            list = mode.getList()
            test_list.extend(list)
        else:
            print("mode.conf 中mode值配置错误，只能为0和1")

        #写存储测试结果的Excel表的表头
        sheet_obj_write.write(0, 0, "测试模块")
        sheet_obj_write.write(0, 1, "http_method")
        sheet_obj_write.write(0, 2, "mobilephone")
        sheet_obj_write.write(0, 3, "regname")
        sheet_obj_write.write(0, 4, "amount")
        sheet_obj_write.write(0, 5, "memberId")
        sheet_obj_write.write(0, 6, "title")
        sheet_obj_write.write(0, 7, "loanRate")
        sheet_obj_write.write(0, 8, "LoanTerm")
        sheet_obj_write.write(0, 9, "loanDateType")
        sheet_obj_write.write(0, 10, "repaymentWay")
        sheet_obj_write.write(0, 11, "biddingDays")
        sheet_obj_write.write(0, 12, "id")
        sheet_obj_write.write(0, 13, "status")
        sheet_obj_write.write(0, 14, "test_method")
        sheet_obj_write.write(0, 15, "test_desc")
        sheet_obj_write.write(0, 16, "result_status")
        sheet_obj_write.write(0, 17, "code")
        sheet_obj_write.write(0, 18, "msg")

        for i in test_list:
            #获取测试的模块名
            req_name = sheet_obj_read.cell_value(i, 0)
            test_method = "test_" + req_name

            suite.addTest(Http_Unittest(i, http, test_method, sheet_obj_read,sheet_obj_write))

        #利用测试集中的数据开始测试
        runner = unittest.TextTestRunner()
        runner.run(suite)
        wb.saveWriteWb()