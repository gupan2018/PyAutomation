__author__ = 'Administrator'
from StoneUIFramework.public.common.basepage import Page

class _RENMAIPAGE1(Page):
    #定位：人脉首页
    def RMSY(self):
        self.RMSY = self.p.get_element("id->com.yunlu6.stone:id/navi_item_connection", "人脉首页")
        return self.RMSY

    #定位：人脉首页-搜索输入框
    def RMST_searchinput(self):
        self.RMST_searchinput = self.p.get_element("id->com.yunlu6.stone:id/img_btn_search", "人脉首页-搜索输入框")
        return self.RMST_searchinput

    #定位：人脉首页-搜索按钮
    def RMSY_searchbtn(self):
        self.RMSY_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv", "人脉首页-搜索输入框")

    #定位：人脉首页-联系人列表
    def RMSY_clickcontacts(self):
        self.RMSY_clickcontacts = self.p.get_elements("id->com.yunlu6.stone:id/iv_arrow", "人脉首页-点击联系人")
        return self.RMSY_clickcontacts

    #定位：人脉首页-同步通讯录
    def RMSY_syscontacts(self):
        self.RMSY_syscontacts = self.p.get_element("id->com.yunlu6.stone:id/bt_start_mailer", "人脉首页-同步通讯录")
        return self.RMSY_syscontacts

    #定位：人脉首页-主菜单
    def RMSY_menu(self):
        self.RMSY_menu = self.p.get_elements("id->com.yunlu6.stone:id/iv_right", "人脉首页-主菜单")
        return self.RMSY_menu

    #定位：人脉首页-主菜单-+人脉
    def RMSY_menu_add(self):
        self.RMSY_menu_add = self.p.get_element("id->com.yunlu6.stone:id/contacts_expand", "人脉首页-主菜单-+人脉")
        return self.RMSY_menu_add

    #定位：人脉首页-主菜单-批量操作
    def RMSY_menu_bcp(self):
        self.RMSY_menu_bcp = self.p.get_element("id->com.yunlu6.stone:id/batch_operate", "人脉首页-主菜单-批量操作")
        return self.RMSY_menu_bcp

    #定位：人脉首页-主菜单-批量操作-返回
    def RMSY_menu_bcp_back(self):
        self.RMSY_menu_bcp_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-主菜单-批量操作-返回")
        return self.RMSY_menu_bcp_back

    #定位：人脉首页-主菜单-批量操作-全选
    def RMSY_menu_bcp_all(self):
        self.RMSY_menu_bcp_all = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-主菜单-批量操作-全选")
        return self.RMSY_menu_bcp_all

    #定位：人脉首页-主菜单-批量操作-全选-返回
    def RMSY_menu_bcp_all_back(self):
        self.RMSY_menu_bcp_all_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-主菜单-批量操作-全选-返回")
        return self.RMSY_menu_bcp_all_back

    #定位：人脉首页-主菜单-批量操作-全选-取消
    def RMSY_menu_bcp_all_cancel(self):
        self.RMSY_menu_bcp_all_cancel = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-主菜单-批量操作-全选-取消")
        return self.RMSY_menu_bcp_all_cancel

    #定位：人脉首页-主菜单-批量操作-全选-选择联系人
    def RMSY_menu_bcp_all_select(self):
        self.RMSY_menu_bcp_all_select = self.p.get_elements("id->com.yunlu6.stone:id/tv_all", "人脉首页-主菜单-批量操作-全选-选择联系人")
        return self.RMSY_menu_bcp_all_select

    #---------------------黑名单-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-黑名单

    #---------------------打标签-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-打标签

    #---------------------换名片-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-换名片
