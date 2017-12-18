__author__ = 'Administrator'
'''
1）新建一个unittest类，对获取用户信息接口进行单元测试
2）runcase循环类，修改函数，引入测试套件
3）注意super写法
'''

from Frame_db.runcase import Runcase
from Frame_db.database import Database
from Frame_db.HttpRequest import HttpRequest
from Frame_db.mode import Mode
from _datetime import datetime
import time

#定义主函数
if __name__ == "__main__" :
    start_time = datetime.now()

    path_http = "http.conf"
    path_db = "db.conf"
    path_mode = "mode.conf"

    #定义一个Http对象
    http = HttpRequest(path_http)

    #定义一个连接数据库的对象
    cnn = Database(path_db).connect_db()

    #定义一个mode对象，该对象封装了如何读取测试用例
    mode = Mode(path_mode)

    #执行测试用例
    runcase = Runcase()
    runcase.run_Case(http, cnn, mode, start_time)