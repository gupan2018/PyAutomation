__author__ = 'Administrator'
#coding=utf-8
import unittest
from time import sleep
import logging

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.空间列表.选企业空间._BrowseOrgSpace import _BrowseOrgSpaceHandle
from StoneUIFramework.public.handle.space.空间列表.选企业空间.菜单栏.产品._OrgSpaceProduct import _OrgSpaceProductHandle
from StoneUIFramework.testcase.空间.test2_上下架产品.CreateProduct import CreateProduct
from StoneUIFramework.testcase.空间.test2_上下架产品.DeleteProduct import DeleteProduct
from StoneUIFramework.public.common.datainfo import DataInfo

#上下架产品
class space_Product(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建_BrowseOrgSpace公有定位控件对象
        self.spaceB = _BrowseOrgSpaceHandle(self.driver)
        #创建_OrgSpaceProduct公有定位控件对象
        self.spaceP = _OrgSpaceProductHandle(self.driver)
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space',"path_002")#通过配置文件获取截图的路径
        self.log_path = cf.getParam('space',"log")#通过配置文件获取日志的路径
        self.logfile = cf.getParam('space',"logfile")#日志文件名
        sleep(2)
        #创建CreateProduct和DeleteProduct对象
        self.cr = CreateProduct()
        self.dl = DeleteProduct()
        #测试数据
        d = DataInfo()#创建DataInfo()对象
        self.spacename = d.cell("test2",2,1)#空间名
        self.proname = d.cell("test2",2,3)
    def test_spaceproduct(self):
        """
            菜单栏用坐标定位：56行，实属无奈之举
        """
        try:
            # self.tools.coverUpdate(self.log_path,self.screen_path)#覆盖更新日志,覆盖更新截图
            self.tools.getLog(self.logfile)#打印日志
        #1.点击进入空间界面
            self.spaceP.Kjlb().click()#点击进入空间列表
            sleep(1)
            self.spaceP.Kjlb_browseorgspaceByName_click(self.spacename)#点击进入测试空间123
            sleep(2)
            self.spaceP.Kjlb_browseorgspace_menu_click()#点击菜单栏
            # self.driver.tap([(self.menu_x,self.menu_y)], 500)#菜单栏
            self.spaceP.Kjlb_browseorgspace_menu_product_click()#点击产品
            self.tools.getScreenShot(self.screen_path,"产品新建界面")
        #2.新建产品
            self.cr.createProduct(self.driver)
        #3.未发布列表:发布
            self.spaceP.Kjlb_browseorgspace_menu_product_unlock_click()#点击未发布列表
            self.tools.getScreenShot(self.screen_path,"未发布列表")
            self.spaceP.Kjlb_browseorgspace_menu_product_unlock_list_byname_click(self.proname)#点击新建的那个产品
            self.spaceP.Kjlb_browseorgspace_menu_product_unlock_list_menu_click()#点击菜单栏
            self.spaceP.Kjlb_browseorgspace_menu_product_unlock_list_menu_release_click()#点击发布
            self.spaceP.Kjlb_browseorgspace_menu_product_unlock_list_menu_release_confirm_click()#点击确定
        #4.进入已发布列表
            self.spaceP.Kjlb_browseorgspace_menu_product_lock_click()#点击进入已发布列表
            self.tools.getScreenShot(self.screen_path,"已发布列表")
            self.spaceP.Kjlb_browseorgspace_menu_product_lock_list_byname_click(self.proname)#点击新建的那个产品
        #5.下架产品
            self.spaceP.Kjlb_browseorgspace_menu_product_lock_list_offshelf_click()#点击下架
            self.spaceP.Kjlb_browseorgspace_menu_product_lock_list_offshelf_sure_click()#确定下架
        #6.删除产品,还原测试场景
            self.spaceP.Kjlb_browseorgspace_menu_product_unlock_click()#点击未发布列表
            self.spaceP.Kjlb_browseorgspace_menu_product_unlock_list_byname_click(self.proname)#点击新建的那个产品
            self.dl.deleteProduct(self.driver)#删除产品，回归
        finally:
            self.tools.getScreenShot(self.screen_path,'finally')#截图
            logging.info("FinishAll@@!!!!!!!")#打印错误的日志
            self.driver.quit()