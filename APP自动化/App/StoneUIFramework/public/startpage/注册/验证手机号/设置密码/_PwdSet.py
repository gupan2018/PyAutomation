__author__ = 'Administrator'
import logging
from StoneUIFramework.public.startpage.注册.验证手机号._VerifyTelp import _VerifyTelp

class _PwdSet(_VerifyTelp):
    def Reg_verifytelp_commit_back(self):
    #定位：注册-验证手机号-完成注册-返回
        try:
            __Reg_verifytelp_commit_back = self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon")
        except Exception as err:
            logging.info("Reg_verifytelp_commit_back:error@@!!!!!!!")
            assert False,\
                "注册-验证手机号-完成注册-返回失败"
        return __Reg_verifytelp_commit_back

    def Reg_verifytelp_commit_pwdinput(self):
    #定位：注册-验证手机号-完成注册-输入密码
        try:
            __Reg_verifytelp_commit_pwdinput = self.driver.find_element_by_id("com.yunlu6.stone:id/edit_newpsw")
        except Exception as err:
            logging.info("Reg_verifytelp_commit_pwdinput:error@@!!!!!!!")
            assert False,\
                "注册-验证手机号-完成注册-输入密码失败"
        return __Reg_verifytelp_commit_pwdinput

    def Reg_verifytelp_commit_pwdconfirm(self):
    #定位：注册-验证手机号-完成注册-确认密码
        try:
            __Reg_verifytelp_commit_pwdconfirm = self.driver.find_element_by_id("com.yunlu6.stone:id/edit_renewpsw")
        except Exception as err:
            logging.info("Reg_verifytelp_commit_pwdconfirm:error@@!!!!!!!")
            assert False,\
                "注册-验证手机号-完成注册-确认密码失败"
        return __Reg_verifytelp_commit_pwdconfirm

    def Reg_verifytelp_commit_commit(self):
    #定位：登录-注册-验证手机号-完成注册-完成
        try:
            __Reg_verifytelp_commit_commit = self.driver.find_element_by_id("com.yunlu6.stone:id/edit_commit")
        except Exception as err:
            logging.info("Reg_verifytelp_commit_commit:error@@!!!!!!!")
            assert False,\
                "注册-验证手机号-完成注册-完成失败"
        return __Reg_verifytelp_commit_commit