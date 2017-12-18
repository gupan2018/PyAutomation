__author__ = 'Administrator'
import configparser
import os
path_test = os.path.dirname(os.path.abspath(__file__))
print(path_test)
#读取配置文件

conf = configparser.ConfigParser() #创建一个对象
conf.read("myConf.conf") #读取配置文件，read函数参数为配置文件地址（可相对路径，也可绝对路径）

#返回配置文件的片段
s = conf.sections()
print(s)

#返回指定片段(section)下的所有option
mysql = conf.options("mysql")
print(mysql)

#返回指定片段下所有的键值对
mysql = conf.items("mysql")
print(mysql)

#得到指定片段，指定option的value值，返回类型为string类型
value1 = conf.get("mysql", "db_user")
print(value1)

#将指定片段，指定option的value值强制转换为int类型
value2 = conf.getint("mysql", "db_port")
print(type(value2))

#另一种读取配置文件的方法
value3 = conf["mysql"]["db_database"]
print(value3)