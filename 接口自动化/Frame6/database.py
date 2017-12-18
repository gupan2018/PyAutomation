__author__ = 'Administrator'
'''
1. 在集成1的基础上，把url和请求数据data都放到数据库里面去
2. 新建一个db.conf文件，里面存放数据库链接信息
3. 新建一个database模块，有一个Database类，函数有两个
    1）初始化函数，用来获取数据库链接信息
    2）第二个函数，用来创建数据库的链接cnn
4. 新建一个runcase模块，用来跑接口查询信息，有一个RunCase类，有一个run_Case方法，参数有http对象和cnn连接，直接就是用来跑接口测试的
'''
import mysql.connector
import configparser

class Database:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read(path)
        self.config = conf.get("mysql", "config")
        self.config = eval(self.config)

    def connect_db(self):
        cnn = mysql.connector.connect(**self.config)
        return cnn