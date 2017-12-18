__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表._SearchLabel import _SearchLabel

class _SearchLabelMenu(_SearchLabel):
    #定位：人脉首页-搜索-标签列表-主菜单
    def RMSY_search_label_menu(self):
        self.RMSY_search_label_menu = self.p.get_element("id->com.yunlu6.stone:id/iv_more", "人脉首页-搜索-标签列表-主菜单")
        return self.RMSY_search_label_menu

    #------------------------------批量操作---------------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作
    def RMSY_search_label_menu_bcp(self):
        self.RMSY_search_label_menu_bcp = self.p.get_element("id->com.yunlu6.stone:id/batch_operate", "人脉首页-搜索-标签列表-主菜单-批量操作")
        return self.RMSY_search_label_menu_bcp

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-返回
    def RMSY_search_label_menu_bcp_back(self):
        self.RMSY_search_label_menu_bcp_back = self.p.get_element("id->com.yunlu6.stone:id/iv_batch_back", "人脉首页-搜索-标签列表-主菜单-批量操作-返回")
        return self.RMSY_search_label_menu_bcp_back

    #---------------------全选-----------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选
    def RMSY_search_label_menu_bcp_all(self):
        self.RMSY_search_label_menu_bcp_all = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-搜索-标签列表-主菜单-批量操作-全选")
        return self.RMSY_search_label_menu_bcp_all

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-返回
    def RMSY_search_label_menu_bcp_all_back(self):
        self.RMSY_search_label_menu_bcp_all_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-搜索-标签列表-主菜单-批量操作-全选-返回")
        return self.RMSY_search_label_menu_bcp_all_back

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-全选
    def RMSY_search_label_menu_bcp_all_all(self):
        self.RMSY_search_label_menu_bcp_all_all = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-搜索-标签列表-主菜单-批量操作-全选-全选")
        return self.RMSY_search_label_menu_bcp_all_all

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-打标签

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-黑名单

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-换名片

    #---------------------------选择联系人---------------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人
    def RMSY_search_label_menu_bcp_selectcontact(self):
        self.RMSY_search_label_menu_bcp_selectcontact = self.p.get_elements("id->com.yunlu6.stone:id/iv_select", "人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人")
        return self.RMSY_search_label_menu_bcp_selectcontact

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-返回
    def RMSY_search_label_menu_bcp_selectcontact_back(self):
        self.RMSY_search_label_menu_bcp_selectcontact_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人-返回")
        return self.RMSY_search_label_menu_bcp_selectcontact_back

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-全选
    def RMSY_search_label_menu_bcp_selectcontact_all(self):
        self.RMSY_search_label_menu_bcp_selectcontact_all = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人-全选")
        return self.RMSY_search_label_menu_bcp_selectcontact_all

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人-打标签

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人-黑名单

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人-换名片