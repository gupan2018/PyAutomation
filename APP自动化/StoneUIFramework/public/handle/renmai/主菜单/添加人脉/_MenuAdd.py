__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.主菜单.添加人脉._MenuAdd import _MenuAdd
from StoneUIFramework.public.handle.renmai.主菜单._Menu import _MenuHandle

class _MenuAddHandle(_MenuHandle, _MenuAdd):
    #定位：人脉首页-主菜单-+人脉
    def RMSY_menu_add_click(self):
        return self.p.click(self.RMSY_menu_add())

    #定位：人脉首页-主菜单-+人脉-返回
    def RMSY_menu_add_back_click(self):
        return self.p.click(self.RMSY_menu_add_back())

    #定位：人脉首页-主菜单-+人脉-清空
    def RMSY_menu_add_clear_click(self):
        return  self.p.click(self.RMSY_menu_add_clear())

    #定位：人脉首页-主菜单-+人脉-输入姓名
    def RMSY_menu_add_nameinput_sendkeys(self, text):
        return self.p.click(self.RMSY_menu_add_nameinput(), text)

    #定位：人脉首页-主菜单-+人脉-输入手机号
    def RMSY_menu_add_telinput_sendkeys(self, text):
        return self.p.send_keys(self.RMSY_menu_add_telinput(), text)

    #定位：人脉首页-主菜单-+人脉-同步手机通讯录
    def RMSY_menu_add_syscontacts_click(self):
        return self.p.click(self.RMSY_menu_add_syscontacts())

    #定位：人脉首页-主菜单-+人脉-名片夹选择加入
    def RMSY_menu_add_addbycard_click(self):
        return self.p.click(self.RMSY_menu_add_addbycard())

    #定位：人脉首页-主菜单-+人脉-添加
    def RMSY_menu_add_add_click(self):
        return self.p.click(self.RMSY_menu_add_add())