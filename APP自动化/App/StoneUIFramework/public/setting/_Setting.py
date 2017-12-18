__author__ = 'Administrator'
#设置页
from StoneUIFramework.public.common.basepage import Page
import logging

class _Setting(Page):
    def Entersetting(self):
        #定位:设置按钮
        try:
            __Entersetting = self.driver.find_element_by_id("com.yunlu6.stone:id/iv_left")
        except Exception as err:
            logging.info("Entersetting:error@@!!!!!!!")
            assert False,\
                "点击设置按钮失败"
        return __Entersetting

    def Avater(self):
        #定位：点击头像
        try:
            __Avater = self.driver.find_element_by_id("com.yunlu6.stone:id/main_slid_userimg")
        except Exception as err:
            logging.info("Avater:error@@!!!!!!!")
            assert False,\
                "点击头像失败"
        return __Avater

    def Basicinfo(self):
        #定位：点击基本信息
        try:
            __Basicinfo = self.driver.find_element_by_id("com.yunlu6.stone:id/main_slid_ll_userinfo")
        except Exception as err:
            logging.info("Basicinfo:error@@!!!!!!!")
            assert False,\
                "点击基本信息失败"
        return __Basicinfo

    def Syssetting(self):
        #定位：点击系统设置
        try:
            __Syssetting = self.driver.find_element_by_id("com.yunlu6.stone:id/main_slid_ll_safe")
        except Exception as err:
            logging.info("Syssetting:error@@!!!!!!!")
            assert False,\
                "点击系统设置失败"
        return __Syssetting

    def Aboutus(self):
        #定位：点击关于我们
        try:
            __Aboutus = self.driver.find_element_by_id("com.yunlu6.stone:id/main_slid_ll_aboutus")
        except Exception as err:
            logging.info("Aboutus:error@@!!!!!!!")
            assert False,\
                "点击关于我们失败"
        return __Aboutus

