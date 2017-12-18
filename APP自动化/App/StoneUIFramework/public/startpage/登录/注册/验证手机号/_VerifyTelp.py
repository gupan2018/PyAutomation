__author__ = 'Administrator'
#登录首页-注册-验证手机号
import logging
from StoneUIFramework.public.startpage.登录.注册._Register import _Register

class _VerifyTelp(_Register):
    #定位：登录-注册-下一步-返回
    def Login_reg_verifytelp_back(self):
        try:
            __Login_reg_verifytelp_back = self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon")

        except Exception as err:
            logging.info("Login_reg_verifytelp_back:error@@!!!!!!!")
            assert False,\
                "登录-注册-下一步-返回失败"
        return __Login_reg_verifytelp_back

    def Login_reg_verifytelp_authcodeinput(self):
    #定位：登录-注册-下一步-输入验证码
        try:
            __Login_reg_verifytelp_authcodeinput = self.driver.find_element_by_id("com.yunlu6.stone:id/regist_captcha")
        except Exception as err:
            logging.info("Login_reg_verifytelp_authcodeinput:error@@!!!!!!!")
            assert False,\
                "登录-注册-下一步-输入验证码失败"
        return __Login_reg_verifytelp_authcodeinput

    def Login_reg_verifytelp_authcodeget(self):
    #定位：登录-注册-下一步-获取验证码
        try:
            __Login_reg_verifytelp_authcodeget = self.driver.find_element_by_id("com.yunlu6.stone:id/regist_getcptcha")
        except Exception as err:
            logging.info("Login_reg_verifytelp_authcodeget:error@@!!!!!!!")
            assert False,\
                "登录-注册-下一步-获取验证码失败"
        return __Login_reg_verifytelp_authcodeget

    def Login_reg_verifytelp_authcodevoice(self):
    #定位：登录-注册-下一步-语音验证码
        try:
            __Login_reg_verifytelp_authcodevoice = self.driver.find_element_by_id("com.yunlu6.stone:id/regist_voicecaptcha")
        except Exception as err:
            logging.info("Login_reg_verifytelp_authcodevoice:error@@!!!!!!!")
            assert False,\
                "登录-注册-下一步-获取语言验证码失败"
        return __Login_reg_verifytelp_authcodevoice

    def Login_reg_verifytelp_commit(self):
    #定位：登录-注册-下一步-完成注册
        try:
            __Login_reg_verifytelp_commit = self.driver.find_element_by_id("com.yunlu6.stone:id/regist_commit")
        except Exception as err:
            logging.info("Login_reg_verifytelp_commit:error@@!!!!!!!")
            assert False,\
                "登录-注册-下一步-完成注册失败"
        return __Login_reg_verifytelp_commit