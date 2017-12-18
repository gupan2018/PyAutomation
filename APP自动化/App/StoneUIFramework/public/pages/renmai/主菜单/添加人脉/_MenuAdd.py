__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.主菜单._Menu import _Menu

class _MenuAdd(_Menu):
    #定位：人脉首页-主菜单-+人脉
    def RMSY_menu_add(self):
        self.RMSY_menu_add = self.p.get_element("id->com.yunlu6.stone:id/contacts_expand", "人脉首页-主菜单-+人脉")
        return self.RMSY_menu_add

    #定位：人脉首页-主菜单-+人脉-返回
    def RMSY_menu_add_back(self):
        self.RMSY_menu_add_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-主菜单-+人脉-返回")
        return self.RMSY_menu_add_back

    #定位：人脉首页-主菜单-+人脉-清空
    def RMSY_menu_add_clear(self):
        self.RMSY_menu_add_clear = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv", "人脉首页-主菜单-+人脉-清空")
        return self.RMSY_menu_add_clear

    #定位：人脉首页-主菜单-+人脉-输入姓名
    def RMSY_menu_add_nameinput(self):
        self.RMSY_menu_add_nameinput = self.p.get_element("id->com.yunlu6.stone:id/contact_name", "人脉首页-主菜单-+人脉-输入姓名")
        return self.RMSY_menu_add_nameinput

    #定位：人脉首页-主菜单-+人脉-输入手机号
    def RMSY_menu_add_telinput(self):
        self.RMSY_menu_add_telinput = self.p.get_element("id->com.yunlu6.stone:id/contact_mobile", "人脉首页-主菜单-+人脉-输入手机号")
        return self.RMSY_menu_add_telinput

    #定位：人脉首页-主菜单-+人脉-同步手机通讯录
    def RMSY_menu_add_syscontacts(self):
        self.RMSY_menu_add_syscontacts = self.p.get_element("id->com.yunlu6.stone:id/btn_top", "人脉首页-主菜单-+人脉-同步手机通讯录")
        return self.RMSY_menu_add_syscontacts

    #定位：人脉首页-主菜单-+人脉-名片夹选择加入
    def RMSY_menu_add_addbycard(self):
        self.RMSY_menu_add_addbycard = self.p.get_element("id->com.yunlu6.stone:id/btn_card_add", "人脉首页-主菜单-+人脉-名片夹选择加入")
        return self.RMSY_menu_add_addbycard

    #定位：人脉首页-主菜单-+人脉-添加
    def RMSY_menu_add_add(self):
        self.RMSY_menu_add_add = self.p.get_element("id->com.yunlu6.stone:id/btn_add", "人脉首页-主菜单-+人脉-添加")
        return self.RMSY_menu_add_add