__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表.主菜单._SearchLabelMenu import _SearchLabelMenu
from StoneUIFramework.public.handle.renmai.搜索.标签列表._SearchLabel import _SearchLabelHandle

class _SearchLabelMenuHandle(_SearchLabelMenu, _SearchLabelHandle):
    #定位：人脉首页-搜索-标签列表-主菜单
    def RMSY_search_label_menu_click(self):
        return self.p.click(self.RMSY_search_label_menu())

    #------------------------------批量操作---------------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作
    def RMSY_search_label_menu_bcp_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp())

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-返回
    def RMSY_search_label_menu_bcp_back_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp_back())

    #---------------------全选-----------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选
    def RMSY_search_label_menu_bcp_all_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp_all())

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-返回
    def RMSY_search_label_menu_bcp_all_back_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp_all_back())

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-全选
    def RMSY_search_label_menu_bcp_all_all_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp_all_all())

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-打标签

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-黑名单

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-换名片

    #---------------------------选择联系人---------------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人
    def RMSY_search_label_menu_bcp_selectcontact_click(self, n):
        return self.p.click(self.RMSY_search_label_menu_bcp_selectcontact()[n])

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-返回
    def RMSY_search_label_menu_bcp_selectcontact_back_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp_selectcontact_back())

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-全选
    def RMSY_search_label_menu_bcp_selectcontact_all_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp_selectcontact_all())

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人-打标签

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人-黑名单

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人-换名片