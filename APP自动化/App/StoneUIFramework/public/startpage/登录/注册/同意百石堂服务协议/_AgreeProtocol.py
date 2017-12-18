__author__ = 'Administrator'
#同意百石堂服务协议
import logging
from StoneUIFramework.public.startpage.登录.注册._Register import _Register

class _AgreeProtocol(_Register):
    #定位：登录-注册-同意百石堂服务协议
    def Login_reg_agreeprotocol_back(self):
        try:
            __Login_reg_agreeprotocol_back = self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon")
        except Exception as err:
            logging.info("Login_reg_agreeprotocol_back:error@@!!!!!!!")
            assert False,\
                "登录-注册-同意百石堂服务协议-返回失败"
        return __Login_reg_agreeprotocol_back