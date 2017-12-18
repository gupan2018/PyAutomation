__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
import logging

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.testcase.登录.LoginHomePage import LoginHomePage
from StoneUIFramework.testcase.登录.LogoutHomePage import LogoutHomePage

class space_Create(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('login',"path_001")#通过配置文件获取截图的路径
        self.log_path = cf.getParam('login',"log_001")#通过配置文件获取日志的路径
        self.filename = cf.getParam('login',"filename_001")#日志文件名
        #创建LoginHomePage和LogoutHomePage对象
        self.login = LoginHomePage()
        self.logout = LogoutHomePage()
        sleep(2)

    def test_login(self):
        try:
            self.tools.coverUpdate(self.log_path,self.screen_path)#覆盖更新日志,覆盖更新截图
            self.tools.getLog(self.filename)#打印日志
            #-------------判断进入应用时是否处于登录状态------------
            #先进行判断，是否处于登录状态，如果处于登录状态，则登出
            #对于已登录的用户，在左上方会有一个设置按钮，对于未登录用户，没有这个按钮，通过查找这个元素来判断用户是否登录
            if self.driver.find_elements_by_id("com.yunlu6.stone:id/iv_left") != []:
                self.logout.logoutHomePage(self.driver)
            #-------------进行登录操作------------
            self.login.loginHomePage(self.driver)
            logging.info("success@@!!!!!!!")#宣布成功

        finally:
            self.tools.getScreenShot(self.screen_path,'finally')#截图
            logging.info("finally@@!!!!!!!")#打印错误的日志
            self.driver.quit()