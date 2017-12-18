__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.空间列表.主菜单.机构空间._CreateOrgSpace import _CreateOrgSpaceHandle
from StoneUIFramework.public.common.datainfo import DataInfo

#创建机构空间
class CreateSpace:
    def __init__(self):#初始化测试数据
        d = DataInfo()#创建DataInfo()对象
        self.province = (d.cell("test1",2,4))#北京
        self.city = (d.cell("test1",2,5))#东城
        self.soverbank = d.cell("test1",2,7)#开户行
        self.sovermybank = d.cell("test1",2,8)#支行
        self.soverbanknub = int(d.cell("test1",2,9))#银行账号
        self.customertype = int(d.cell("test1",2,3))#客户类型
        self.industry = int(d.cell("test1",2,10))#产业角色
    def createSpace(self,driver,fullname,easyname):
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_CreateOrgSpace公有定位控件对象
        space = _CreateOrgSpaceHandle(driver)
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        screen_path = cf.getParam('space',"path_001")#通过配置文件获取截图的路径
        sleep(2)
        try:
        #1.空间首页
            space.Kjlb_click()
            tools.getScreenShot(screen_path,"空间首页")
        #2.右上角主菜单
            space.Kjlb_mainmenu_click()
        #3.+机构空间
            space.Kjlb_mainmenu_newspace_click()
            tools.getScreenShot(screen_path,"新建机构空间")
            #--------------------------新建机构空间-------------------------
            # 机构名称:(fullname):appium测试空间
            # 机构简称:(easyname):appium测试空间
            # 机构类型:企业
            # 产业角色:工厂
            # 客户类型:石材
            # 所在地区:北京-东城
            # 详细地址:不填
            space.Kjlb_mainmenu_newspace_orgname_sendkeys(fullname)#全称
            space.Kjlb_mainmenu_newspace_orgintro_sendkeys(easyname)#简称
            space.Kjlb_mainmenu_newspace_orgtitle_click()#点击标题
            space.Kjlb_mainmenu_newspace_orgtype_click()#机构类型
            space.Kjlb_mainmenu_newspace_orgtype_company_click()#机构类型：企业
            sleep(1)
            space.Kjlb_mainmenu_newspace_industry_click()#产业角色
            space.Kjlb_mainmenu_newspace_industry_tag_click(self.industry)#选择工厂
            space.Kjlb_mainmenu_newspace_customertype_click()#客户类型
            space.Kjlb_mainmenu_newspace_customertype_tag_click(self.customertype)#客户类型标签
            space.Kjlb_mainmenu_newspace_customertype_confirm_click()#点击确定
            space.Kjlb_mainmenu_newspace_area_click()#所在地区
            driver.find_element_by_name(self.province).click()
            driver.find_element_by_name(self.city).click()
            # space.Kjlb_mainmenu_newspace_area_address_click(self.province)#北京
            # space.Kjlb_mainmenu_newspace_area_address_click(self.city)#东城
            tools.getScreenShot(screen_path,"提交前截图")
            space.Kjlb_mainmenu_newspace_affirm_click()#点击提交

            #------------------------验证对公账号-------------------------------
            space.Kjlb_mainmenu_newspace_verifynow_click()#点击去验证
            tools.getScreenShot(screen_path,"收款账户验证")
            #开户银行:AAA
            #所在地区:北京-东城
            #支行:BBB
            #银行账号:123456
            space.Kjlb_mainmenu_newspace_verifynow_soverbank_sendkeys(self.soverbank)#开户银行
            space.Kjlb_mainmenu_newspace_verifynow_soveraddress_click()#所在地区
            # space.Kjlb_mainmenu_newspace_verifynow_soveraddress_list_click(self.province)#北京
            # space.Kjlb_mainmenu_newspace_verifynow_soveraddress_list_click(self.city)#东城
            driver.find_element_by_name(self.province).click()#北京
            driver.find_element_by_name(self.city).click()#东城
            space.Kjlb_mainmenu_newspace_verifynow_sovermybank_sendkeys(self.sovermybank)#支行
            space.Kjlb_mainmenu_newspace_verifynow_soverbanknub_sendkeys(self.soverbanknub)#银行账户
            tools.getScreenShot(screen_path,"收款账户验证信息填写")
            space.Kjlb_mainmenu_newspace_verifynow_soversave_click()#确定提交
            tools.getScreenShot(screen_path,"订单详情页")
            sleep(1)
            space.Kjlb_mainmenu_newspace_verifynow_soversave_back_click()#点击返回
            sleep(1)
        finally:
            tools.getScreenShot(screen_path,'finallycreatespace')#截图
            logging.info("FinishCreateSpace@@!!!!!!!")#打印错误的日志