__author__ = 'Administrator'
#注册首页
import logging
from StoneUIFramework.public.startpage._Startpage import _Startpage
from appium import webdriver

class _Register(_Startpage):
    #定位：注册-返回
    def Reg_back(self):
        try:
            __Reg_back = self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon")
        except Exception as err:
            logging.info("Reg_back:error@@!!!!!!!")
            assert False,\
                "注册-返回失败"
        return __Reg_back

    def Reg_telp(self):
    #定位：注册-输入手机号
        try:
            __Reg_telp = self.driver.find_element_by_id("com.yunlu6.stone:id/register_et_photo")
        except Exception as err:
            logging.info("Reg_telp:error@@!!!!!!!")
            assert False,\
                "注册-输入手机号失败"
        return __Reg_telp

    def Reg_authcodeinput(self):
    #定位：注册-输入图片验证码
        try:
            __Reg_authcodeinput = self.driver.find_element_by_id("com.yunlu6.stone:id/register_et_verification_code")
        except Exception as err:
            logging.info("Reg_authcodeinput:error@@!!!!!!!")
            assert False,\
                "注册-输入图片验证码失败"
        return __Reg_authcodeinput

    def Reg_authcodechange(self):
    #定位：注册-更换图片验证码
        try:
            __Reg_authcodechange = self.driver.find_element_by_id("com.yunlu6.stone:id/register_im_verification_code")
        except Exception as err:
            logging.info("Reg_authcodechange:error@@!!!!!!!")
            assert False,\
                "注册-更换图片验证码失败"
        return __Reg_authcodechange

    def Reg_agreeprotocol(self):
    #定位：注册-同意百石堂服务协议
        try:
            __Reg_agreeprotocol = self.driver.find_element_by_id("com.yunlu6.stone:id/register_tv_agreement")
        except Exception as err:
            logging.info("Reg_agreeprotocol:error@@!!!!!!!")
            assert False,\
                "登录-注册-同意百石堂服务协议失败"
        return __Reg_agreeprotocol

    def Reg_next(self):
    #定位：注册-下一步
        try:
            __Reg_next = self.driver.find_element_by_id("com.yunlu6.stone:id/register_btn_next")
        except Exception as err:
            logging.info("Reg_next:error@@!!!!!!!")
            assert False,\
                "登录-注册-进入下一步失败"
        return __Reg_next