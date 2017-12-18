#!/usr/bin/env python
# -*- coding:utf-8 -*-

#引入pyh模块
from Frame_db.pyh import *
import time
import os

#利用第三方的pyh库完成html报告的生成
class HtmlReport:
    def __init__(self, cursor):
        self.title = '接口测试报告'#网页标签名称
        self.filename = ''#结果文件名
        self.time_took = '00:00:00'#测试耗时
        self.success_num = 0#测试通过的用例数
        self.fail_num = 0#测试失败的用例数
        self.error_num = 0#运行出错的用例数
        self.case_total = 0#运行测试用例总数
        self.cursor = cursor

    #生成HTML报告
    def generate_html(self,head, file):
            page = PyH(self.title)
            page << h1(head, align='center') #标题居中

            page << p('测试总耗时：' + self.time_took)

            #查询测试用例总数
            query = ('SELECT count(case_id) FROM ygg_test_result02')
            self.cursor.execute(query)
            self.case_total = self.cursor.fetchone()[0]

            #查询测试失败的用例数
            self.cursor.execute('SELECT count(case_id) FROM ygg_test_result02 WHERE result_status = %s',('0',))
            self.fail_num = self.cursor.fetchone()[0]

            #查询测试通过的用例数
            self.cursor.execute('SELECT count(case_id) FROM ygg_test_result02 WHERE result_status = %s',('1',))
            self.success_num = self.cursor.fetchone()[0]


            page << p('测试用例数：' + str(self.case_total) + '&nbsp'*10 + '成功用例数：' + str(self.success_num) +
                      '&nbsp'*10 + '失败用例数：' + str(self.fail_num) + '&nbsp'*10 )
            #表格标题caption 表格边框border 单元边沿与其内容之间的空白cellpadding 单元格之间间隔为cellspacing

            tab = table( border='1', cellpadding='1', cellspacing='0', cl='table',  style='word-break:break-all; word-wrap:break-all;')
            tab1 = page << tab
            tab1 << tr(td('用例ID', bgcolor='#ABABAB', align='center')
                       + td('HTTP方法', bgcolor='#ABABAB', align='center')
                       + td('接口名称', bgcolor='#ABABAB', align='center')
                       + td('请求URL', bgcolor='#ABABAB', align='center')
                       + td('电话号码', bgcolor='#ABABAB', align='center')
                       + td('注册名字', bgcolor='#ABABAB', align='center')
                       + td('密码', bgcolor='#ABABAB', align='center')
                       + td('金额/年利率', bgcolor='#ABABAB', align='center')
                       + td('用户Id', bgcolor='#ABABAB', align='center')
                       + td('借款标题', bgcolor='#ABABAB', align='center')
                       + td('年利率', bgcolor='#ABABAB', align='center')
                       + td('借款期限', bgcolor='#ABABAB', align='center')
                       + td('借款期限类型', bgcolor='#ABABAB', align='center')
                       + td('还款方式', bgcolor='#ABABAB', align='center')
                       + td('竞标天数', bgcolor='#ABABAB', align='center')
                       + td('项目Id', bgcolor='#ABABAB', align='center')
                       + td('标状态', bgcolor='#ABABAB', align='center')
                       + td('测试方法', bgcolor='#ABABAB', align='center')
                       + td('测试描述', bgcolor='#ABABAB', align='center')
                       + td('执行状态', bgcolor='#ABABAB', align='center')
                       + td('状态码', bgcolor='#ABABAB', align='center')
                       + td('测试结果', bgcolor='#ABABAB', align='center'))
                       

            #查询所有测试结果并记录到html文档
            query = ('SELECT case_id, http_method, request_name, request_url,'
                          'mobilephone,regname, pwd, amount, memberId, title, loanRate, loanTerm, loanDateType, repaymemtWay, biddingDays, id, status, test_method, test_desc, result_status, code, msg FROM ygg_test_result02')
            self.cursor.execute(query)
            query_result = self.cursor.fetchall()

            for row in query_result:
                tab1<< tr(td(int(row[0]), align='center') + td(row[1]) +
                              td(row[2]) + td(row[3], align='center') +
                              td(row[4]) + td(row[5]) + td(row[6]) +
                              td(row[7], align='center') + td(row[8])+td(row[9]) + td(row[10]) +
                              td(row[11], align='center') + td(row[12]) +
                              td(row[13]) + td(row[14], align='center') +
                              td(row[15]) + td(row[16]) + td(row[17]) +
                              td(row[18], align='center') + td(row[19])+td(row[20]) + td(row[21])
                )

            self._set_result_filename(file)
            page.printOut(self.filename)#生成测试报告到本地
            '''
            此处是每次运行完成后清理test_result表中的数据
            如果不清空那么下次运行的时候在插入数据的时候id会重复而报错
            '''
            try:
                query = ('DELETE FROM ygg_test_result02')
                self.cursor.execute(query)
                self.cursor.execute('commit')
            except Exception as e:
                #回滚
                print('%s' % e)
                self.cursor.execute('rollback')
            
            self.cursor.close()

    #设置结果文件名
    def _set_result_filename(self, filename):
        self.filename = filename
        #判断是否为目录
        if os.path.isdir(self.filename):
            raise IOError("%s must point to a file" % filename)
        elif '' == self.filename:
            raise IOError('filename can not be empty')
        else:
            parent_path, ext = os.path.splitext(filename)
            tm = time.strftime('%Y,%m,%d,%H,%M,%S', time.localtime())
            self.filename = parent_path + "_" + tm + ext

    #统计运行耗时
    def set_time_took(self, time):
        self.time_took = time
        return self.time_took
