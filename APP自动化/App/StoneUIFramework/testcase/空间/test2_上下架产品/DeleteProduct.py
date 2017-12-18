__author__ = 'Administrator'
#coding=utf-8
from time import sleep
import logging

from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.空间列表.选企业空间.菜单栏.产品._OrgSpaceProduct import _OrgSpaceProductHandle

#上架产品
class DeleteProduct:
    def __init__(self):#初始化测试数据
       pass
    def deleteProduct(self,driver):
        try:
            #创建工具类
            self.tools = Tools(driver)#tools工具
            #创建_OrgSpaceProduct公有定位控件对象
            self.spaceP = _OrgSpaceProductHandle(driver)
            #创建读取配置信息对象
            self.cf = GlobalParam('config','path_file.conf')
            #获取截图路径、日志路径、日志名
            self.screen_path = self.cf.getParam('space',"path_002")#通过配置文件获取截图的路径
            sleep(2)
            #-----------------删除产品-----------------
        #1.点击菜单栏
            self.spaceP.Kjlb_browseorgspace_menu_product_unlock_list_menu_click()#点击菜单栏
        #2.点击删除
            self.spaceP.Kjlb_browseorgspace_menu_product_unlock_list_menu_delete_click()#删除产品
            self.tools.getScreenShot(self.screen_path,"删除产品后列表")
        finally:
            self.tools.getScreenShot(self.screen_path,'finally')#截图
            logging.info("FinishDeleteProduct@@!!!!!!!")#打印错误的日志