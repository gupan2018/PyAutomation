__author__ = 'xiaoj'
from time import sleep
from appium import webdriver
import os
import configparser

class Connect:
    def __init__(self):
        pass
    def connect(self):
        cf = configparser.ConfigParser()
        #获取当前文件夹的父目录的父目录的绝对路径
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        file_path = os.path.join(BASE_DIR,"config","connect.conf")
        cf.read(file_path)#读取配置文件
        desired_caps = eval(cf.get("APP","desired_caps1"))
        #初始化appium连接
        try:
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        except:
            assert False ,"初始化appium连接失败,程序已退出!!!"
        sleep(2)
        return driver
