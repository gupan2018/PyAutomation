__author__ = 'Administrator'
#注册首页
import logging
from StoneUIFramework.public.startpage.登录._Login import _Login
from appium import webdriver

class _Register(_Login):
    #定位：登录-注册-返回
    def Login_reg_back(self):
        try:
            __Login_reg_back = self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon")
        except Exception as err:
            logging.info("Login_reg_back:error@@!!!!!!!")
            assert False,\
                "登录-注册-返回失败"
        return __Login_reg_back

    def Login_reg_telp(self):
    #定位：登录-注册-输入手机号
        try:
            __Login_reg_telp = self.driver.find_element_by_id("com.yunlu6.stone:id/register_et_photo")
        except Exception as err:
            logging.info("Login_reg_telp:error@@!!!!!!!")
            assert False,\
                "登录-注册-输入手机号失败"
        return __Login_reg_telp

    def Login_reg_authcodeinput(self):
    #定位：登录-注册-输入图片验证码
        try:
            __Login_reg_authcodeinput = self.driver.find_element_by_id("com.yunlu6.stone:id/register_et_verification_code")
        except Exception as err:
            logging.info("Login_reg_authcodeinput:error@@!!!!!!!")
            assert False,\
                "登录-注册-输入图片验证码失败"
        return __Login_reg_authcodeinput

    def Login_reg_authcodechange(self):
    #定位：登录-注册-更换图片验证码
        try:
            __Login_reg_authcodechange = self.driver.find_element_by_id("com.yunlu6.stone:id/register_im_verification_code")
        except Exception as err:
            logging.info("Login_reg_authcodechange:error@@!!!!!!!")
            assert False,\
                "登录-注册-更换图片验证码失败"
        return __Login_reg_authcodechange

    def Login_reg_agreeprotocol(self):
    #定位：登录-注册-同意百石堂服务协议
        try:
            __Login_reg_agreeprotocol = self.driver.find_element_by_id("com.yunlu6.stone:id/register_tv_agreement")
        except Exception as err:
            logging.info("Login_reg_agreeprotocol:error@@!!!!!!!")
            assert False,\
                "登录-注册-同意百石堂服务协议失败"
        return __Login_reg_agreeprotocol

    def Login_reg_next(self):
    #定位：登录-注册-下一步
        try:
            __Login_reg_next = self.driver.find_element_by_id("com.yunlu6.stone:id/register_btn_next")
        except Exception as err:
            logging.info("Login_reg_next:error@@!!!!!!!")
            assert False,\
                "登录-注册-进入下一步失败"
        return __Login_reg_next