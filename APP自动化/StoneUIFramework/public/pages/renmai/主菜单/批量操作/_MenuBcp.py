__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.主菜单._Menu import _Menu

class _MenuBcp(_Menu):
    #定位：人脉首页-主菜单-批量操作
    def RMSY_menu_bcp(self):
        self.RMSY_menu_bcp = self.p.get_element("id->com.yunlu6.stone:id/batch_operate", "人脉首页-主菜单-批量操作")
        return self.RMSY_menu_bcp

    #定位：人脉首页-主菜单-批量操作-返回
    def RMSY_menu_bcp_back(self):
        self.RMSY_menu_bcp_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-主菜单-批量操作-返回")
        return self.RMSY_menu_bcp_back

    #---------------------------------------------------全选所有元素定位------------------------------------------------------
    #定位：人脉首页-主菜单-批量操作-全选
    def RMSY_menu_bcp_all(self):
        self.RMSY_menu_bcp_all = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-主菜单-批量操作-全选")
        return self.RMSY_menu_bcp_all

    #定位：人脉首页-主菜单-批量操作-全选-返回
    def RMSY_menu_bcp_all_back(self):
        self.RMSY_menu_bcp_all_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-主菜单-批量操作-全选-返回")
        return self.RMSY_menu_bcp_all_back

    #定位：人脉首页-主菜单-批量操作-全选-全选
    def RMSY_menu_bcp_all_all(self):
        self.RMSY_menu_bcp_all_all = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-主菜单-批量操作-全选-全选")
        return self.RMSY_menu_bcp_all_all

    #---------------------黑名单-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-黑名单

    #---------------------打标签-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-打标签

    #---------------------换名片-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-换名片

    #---------------------------------------------------联系人列表所有元素定位------------------------------------------------------
    def RMSY_menu_bcp_contacts(self):
        self.RMSY_menu_bcp_contacts = self.p.get_elements("id->com.yunlu6.stone:id/iv_select", "人脉首页-主菜单-批量操作-联系人列表")
        return self.RMSY_menu_bcp_contacts