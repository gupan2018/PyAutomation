__author__ = 'Administrator'
#起始页
from StoneUIFramework.public.common.basepage import Page
import logging

class _Startpage(Page):
    def Search(self):
        #定位:任你搜，任你搜
        try:
            __Search = self.driver.find_element_by_id("com.yunlu6.stone:id/start_search")
        except Exception as err:
            logging.info("Search:error@@!!!!!!!")
            assert False,\
                "搜索失败"
        return __Search

    def Product(self):
    #定位：产品
        try:
            __Product = self.driver.find_element_by_id("com.yunlu6.stone:id/start_buildstone")
        except Exception as err:
            logging.info("Product:error@@!!!!!!!")
            assert False,\
                "点击产品失败"
        return __Product

    def Company(self):
    #定位：企业
        try:
            __Company = self.driver.find_element_by_id("com.yunlu6.stone:id/company_search")
        except Exception as err:
            logging.info("Company:error@@!!!!!!!")
            assert False,\
                "点击企业失败"
        return __Company

    def Login(self):
    #定位：登录
        try:
            __Login = self.driver.find_element_by_id("com.yunlu6.stone:id/main_login")
        except Exception as err:
            logging.info("Login:error@@!!!!!!!")
            assert False,\
                "点击登录失败"
        return __Login

    def Register(self):
    #定位：注册
        try:
            __Register = self.driver.find_element_by_id("com.yunlu6.stone:id/main_register")
        except Exception as err:
            logging.info("Register:error@@!!!!!!!")
            assert False,\
                "点击注册失败"
        return __Register