__author__ = 'Administrator'
'''
mode = 0，跑指定序列的用例
mode = 1，跑所有用例

1. 新增一个配置文件：mode.conf
2. 新增一个mode模块，里面有一个Mode类，里面有3个函数
    a)初始化函数，获取到mode配置文件里面的值
    b)返回mode的值
    c）返回list的值
3. 修改runmode函数，增加if与else逻辑来判断如何跑用例，根据数据库中的http_method来判断使用get还是post方法来跑用例
'''

from runcase import Runcase
from database import Database
from HttpRequest import HttpRequest
from mode import Mode

path_http = "http.conf"
path_db = "db.conf"
path_mode = "mode.conf"

http = HttpRequest(path_http)
cnn = Database(path_db).connect_db()
mode = Mode(path_mode)

runcase = Runcase()
runcase.run_Case(http, cnn, mode)
