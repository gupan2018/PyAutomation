__author__ = 'Administrator'

'''
根据添加项目--审核--注册--充值--投资，做一个完整的业务流程的自动化代码请求
'''

from Frame_relevance.database import Database
from Frame_relevance.runcase import Runcase
from Frame_relevance.HttpRequest import HttpRequest

path_background = "db_background.conf"
path_test_data = "test_data.conf"
path_http = "http.conf"
path_mode = "mode.conf"

if __name__ == "__main__":
    #获取后台数据库连接
    cnn_background = Database(path_background).connect_db()
    http = HttpRequest(path_http)

    runcase = Runcase()
    if runcase.run_Case(http,cnn_background, path_test_data) == False:
        print("测试失败")
    else:
        print("测试成功")