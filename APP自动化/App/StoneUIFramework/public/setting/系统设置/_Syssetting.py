__author__ = 'Administrator'
#系统设置页
from StoneUIFramework.public.setting._Setting import _Setting
import logging

class _Syssetting(_Setting):
    def Syssetting_back(self):
        #定位:设置-系统安全-返回
        try:
            __Syssetting_back = self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon")
        except Exception as err:
            logging.info("Syssetting_back:error@@!!!!!!!")
            assert False,\
                "点击设置-系统安全-返回失败"
        return __Syssetting_back

    def Syssetting_wifisync(self):
        #定位:设置-系统安全-WI-FI同步按钮
        try:
            __Syssetting_wifisync = self.driver.find_element_by_id("com.yunlu6.stone:id/aboutus_wifibtn")
        except Exception as err:
            logging.info("Syssetting_wifisync:error@@!!!!!!!")
            assert False,\
                "点击设置-系统安全-WI-FI同步按钮失败"
        return __Syssetting_wifisync

    def Syssetting_pwdalter(self):
        #定位:设置-系统安全-修改密码
        try:
            __Syssetting_pwdalter = self.driver.find_element_by_id("com.yunlu6.stone:id/sliding_safe_editpsw")
        except Exception as err:
            logging.info("Syssetting_pwdalter:error@@!!!!!!!")
            assert False,\
                "点击设置-系统安全-修改密码失败"
        return __Syssetting_pwdalter

    def Syssetting_cachewipe(self):
        #定位:设置-系统安全-清理缓存
        try:
            __Syssetting_cachewipe = self.driver.find_element_by_id("com.yunlu6.stone:id/aboutus_cleandata")
        except Exception as err:
            logging.info("Syssetting_cachewipe:error@@!!!!!!!")
            assert False,\
                "点击设置-系统安全-清理缓存失败"
        return __Syssetting_cachewipe

    def Syssetting_logout(self):
        #定位:设置-系统安全-退出
        try:
            __Syssetting_logout = self.driver.find_element_by_id("com.yunlu6.stone:id/aboutus_loginout")
        except Exception as err:
            logging.info("Syssetting_logout:error@@!!!!!!!")
            assert False,\
                "点击设置-系统安全-退出失败"
        return __Syssetting_logout