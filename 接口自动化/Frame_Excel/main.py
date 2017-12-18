__author__ = 'Administrator'
'''
1）新建一个unittest类，对获取用户信息接口进行单元测试
2）runcase循环类，修改函数，引入测试套件
3）注意super写法
'''

from Frame_Excel.runcase import Runcase
from Frame_Excel.HttpRequest import HttpRequest
from Frame_Excel.mode import Mode
from _datetime import datetime
from Frame_Excel.wb import Workbook

path_http = "test\\http.conf"
path_mode = "mode.conf"
path_excel_read = "test_data.xlsx"
path_exvel_write = "圆滚滚的测试报告.xls"

#定义主函数
if __name__ == "__main__" :
    start_time = datetime.now()

    #创建一个Workbook对象，传入存储测试数据的Excel文件的路径以及输出测试报告的Excel文件的路径
    wb = Workbook(path_excel_read, path_exvel_write)

    #创建一个HTTP对象，里面定义了进行get请求以及post请求的方法
    http = HttpRequest(path_http)
    mode = Mode(path_mode)

    runcase = Runcase()
    runcase.run_Case(http, wb, mode)