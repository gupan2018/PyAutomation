__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from time import sleep
import logging
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.setting.系统设置.退出._Logout import _Logout

class LogoutHomePage():
    def __init__(self):
        pass

    def logoutHomePage(self, driver):
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        screen_path = cf.getParam("login","path_001")#通过配置文件获取截图的路径
        try:
            #创建_Logout公有定位控件对象
            logouthandle = _Logout(driver)
            sleep(2)
            tools.getScreenShot(screen_path, "退出登录前界面")
            #点击设置界面，调出设置页
            logouthandle.Entersetting().click()

            #------------------------进行登出操作-------------------------------
            #点击系统设置
            logouthandle.Syssetting().click()
            sleep(1)
            #点击退出按钮
            logouthandle.Syssetting_logout().click()
            sleep(1)
            tools.getScreenShot(screen_path, "点击登出")
            logouthandle.Syssetting_logout_confirm().click()
            sleep(1)
            tools.getScreenShot(screen_path, "登出成功")
        finally:
            tools.getScreenShot(screen_path,'finallylogoutHomePage')#截图
            logging.info("finallylogoutHomePage@@!!!!!!!")#打印错误的日志