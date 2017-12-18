__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from time import sleep
import logging
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.空间列表.选企业空间.菜单栏.企业名片._OrgSpaceBCard import _OrgSpaceBCardHandle
from StoneUIFramework.public.common.datainfo import DataInfo

#关闭机构空间
class CloseSpace:
    def closeSpace(self,driver):
        """
            菜单栏用坐标定位：34行，实属无奈之举
        """
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_OrgSpaceBCard公有定位控件对象
        spaceB = _OrgSpaceBCardHandle(driver)
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        screen_path = cf.getParam('space',"path_001")#通过配置文件获取截图的路径
        #测试数据
        d = DataInfo()#创建DataInfo()对象
        # self.easyname = d.cell("test1",2,2,)
        self.menu_x = int(d.cell("test1",2,11))#fullname
        self.menu_y = int(d.cell("test1",2,12,))#easyname
        sleep(2)
        try:
            #为了保证不中途退出，需要第一次进入的时候检查是否存在该机构，如果存在，先关闭
            spaceB.Kjlb_browseorgspaceByID_click(0)#点击进入
            sleep(2)
            # driver.tap([(self.menu_x,self.menu_y)], 500)#菜单栏
            spaceB.Kjlb_browseorgspace_menu_click()#菜单栏
            spaceB.Kjlb_browseorgspace_menu_bcard_click()#企业名片
            spaceB.Kjlb_browseorgspace_menu_bcard_menu_click()#菜单栏
            spaceB.Kjlb_browseorgspace_menu_bcard_menu_close_click()#关闭
            tools.getScreenShot(screen_path,"关闭空间确认")
            spaceB.Kjlb_browseorgspace_menu_bcard_menu_close_confirm_click()#确认关闭
            tools.getScreenShot(screen_path,"存在该机构将其关闭了")
        finally:
            tools.getScreenShot(screen_path,'finallyclosespace')#截图
            logging.info("FinishCloseSpace@@!!!!!!!")#打印错误的日志