__author__ = 'Administrator'
#登出确认页
from StoneUIFramework.public.setting.系统设置._Syssetting import _Syssetting
import logging

class _Logout(_Syssetting):
    def Syssetting_logout_confirm(self):
        #定位:设置-系统安全-退出-确定
        try:
            __Syssetting_logout_confirm = self.driver.find_element_by_id("android:id/button1")
        except Exception as err:
            logging.info("Syssetting_logout_confirm:error@@!!!!!!!")
            assert False,\
                "点击设置-系统安全-退出-确定失败"
        return __Syssetting_logout_confirm

    def Syssetting_logout_cancel(self):
        #定位:设置-系统安全-退出-取消
        try:
            __Syssetting_logout_cancel = self.driver.find_element_by_id("android:id/button2")
        except Exception as err:
            logging.info("Syssetting_logout_cancel:error@@!!!!!!!")
            assert False,\
                "点击设置-系统安全-退出-取消"
        return __Syssetting_logout_cancel