__author__ = 'Administrator'
#同意百石堂服务协议
import logging
from StoneUIFramework.public.startpage.注册._Register import _Register

class _AgreeProtocol(_Register):
    #定位：注册-同意百石堂服务协议
    def Reg_agreeprotocol_back(self):
        try:
            __Reg_agreeprotocol_back = self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon")
        except Exception as err:
            logging.info("Reg_agreeprotocol_back:error@@!!!!!!!")
            assert False,\
                "注册-同意百石堂服务协议-返回失败"
        return __Reg_agreeprotocol_back