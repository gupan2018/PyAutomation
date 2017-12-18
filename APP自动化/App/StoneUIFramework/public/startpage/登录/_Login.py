__author__ = 'Administrator'
#登录首页
import logging
from StoneUIFramework.public.startpage._Startpage import _Startpage
from appium import webdriver

class _Login(_Startpage):
    #定位:登录-返回
    def Login_back(self):
        try:
            __Login_back = self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon")
        except Exception as err:
            logging.info("Login_back:error@@!!!!!!!")
            assert False,\
                "登录-返回失败"
        return __Login_back

    #定位：登录-输入手机号
    def Login_telp(self):
        try:
            __Login_telp = self.driver.find_element_by_id("com.yunlu6.stone:id/login_et_photo")
        except Exception as err:
            logging.info("Login_telp:error@@!!!!!!!")
            assert False,\
                "登录-输入手机号失败"
        return __Login_telp

    #定位：登录-输入密码
    def Login_pwd(self):
        try:
            __Login_pwd = self.driver.find_element_by_id("com.yunlu6.stone:id/login_et_password")
        except Exception as err:
            logging.info("Login_pwd:error@@!!!!!!!")
            assert False,\
                "登录-输入密码失败"
        return __Login_pwd

    #定位：登录-点击登录
    def Login_login(self):
        try:
            __Login_login = self.driver.find_element_by_id("com.yunlu6.stone:id/login_btn")
        except Exception as err:
            logging.info("Login_login:error@@!!!!!!!")
            assert False, \
                "登录-登录失败"
        return __Login_login

    #定位：登录-忘记密码
    def Login_forgetpwd(self):
        try:
            __Login_forgetpwd = self.driver.find_element_by_id("com.yunlu6.stone:id/login_tv_forgetPassword")
        except Exception as err:
            logging.info("Login_forgetpwd:error@@!!!!!!!")
            assert False,\
                "登录-忘记密码失败"
        return __Login_forgetpwd

    #定位：登录-注册
    def Login_reg(self):
        try:
            __Login_reg = self.driver.find_element_by_id("com.yunlu6.stone:id/login_tv_register")
        except Exception as err:
            logging.info("Login_reg:error@@!!!!!!!")
            assert False,\
                "登录-注册账号失败"
        return __Login_reg