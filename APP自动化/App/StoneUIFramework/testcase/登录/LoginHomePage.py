__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.startpage.登录._Login import _Login
from StoneUIFramework.public.common.datainfo import DataInfo

class LoginHomePage():
    def __init__(self):
        d = DataInfo("login.xlsx")#创建DataInfo()对象
        self.telp = str(int(d.cell("test1",2,1)))#获取手机号136667618021
        self.pwd = d.cell("test1",2,2)#获取密码free930923

    def loginHomePage(self, driver, section = "login"):
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        screen_path = cf.getParam(section,"path_001")#通过配置文件获取截图的路径
        try:
            #创建_Login公有定位控件对象
            loginHandle = _Login(driver)
            sleep(2)
            tools.getScreenShot(screen_path, "app欢迎界面")
            #点击登录按钮，进入到登录界面
            loginHandle.Login().click()

            #------------------------进行登录操作-------------------------------
            #手机号13667618021
            #密码free930923

            #输入登录手机号
            loginHandle.Login_telp().send_keys(self.telp)
            sleep(1)
            #输入登录密码
            loginHandle.Login_pwd().send_keys(self.pwd)
            sleep(1)
            tools.getScreenShot(screen_path, "登录信息")
            loginHandle.Login_login().click()
            tools.getScreenShot(screen_path, "点击登录")
            sleep(2)
        finally:
            tools.getScreenShot(screen_path,'finallyloginHomePage')#截图
            logging.info("finallyloginHomePage@@!!!!!!!")#打印错误的日志