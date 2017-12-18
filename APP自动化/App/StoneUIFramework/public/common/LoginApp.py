__author__ = 'Administrator'
import unittest
from time import sleep
import logging

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.testcase.登录.LoginHomePage import LoginHomePage
from StoneUIFramework.testcase.登录.LogoutHomePage import LogoutHomePage

class LoginApp():
    def loginapp(self, driver, section = "login"):#最开始执行
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        screen_path = cf.getParam(section,"path_001")#通过配置文件获取截图的路径
        #创建LoginHomePage和LogoutHomePage对象
        cr = LoginHomePage()
        cl = LogoutHomePage()
        sleep(2)
        try:
            #-------------判断进入应用时是否处于登录状态------------
            #先进行判断，是否处于登录状态，如果处于登录状态，则登出
            #对于已登录的用户，在左上方会有一个设置按钮，对于未登录用户，没有这个按钮，通过查找这个元素来判断用户是否登录
            if driver.find_elements_by_id("com.yunlu6.stone:id/iv_left") == []:
                #-------------若用户未登录，进行登录操作------------
                LoginHomePage().loginHomePage(driver, section)
                logging.info("success@@!!!!!!!")#宣布成功
        except Exception as err:
            tools.getScreenShot(screen_path,'finally')#截图
            logging.info("finally@@!!!!!!!")#打印错误的日志

