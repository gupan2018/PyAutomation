__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.主菜单.批量操作._MenuBcp import _MenuBcp
from StoneUIFramework.public.handle.renmai.主菜单._Menu import _MenuHandle

class _MenuBcpHandle_click(_MenuBcp, _MenuHandle):
    #定位：人脉首页-主菜单-批量操作
    def RMSY_menu_bcp_click(self):
        return self.p.click(self.RMSY_menu())

    #定位：人脉首页-主菜单-批量操作-返回
    def RMSY_menu_bcp_back_click(self):
        return self.p.click(self.RMSY_menu_bcp_back())

    #---------------------------------------------------全选所有元素定位------------------------------------------------------
    #定位：人脉首页-主菜单-批量操作-全选
    def RMSY_menu_bcp_all_click(self):
        return self.p.click(self.RMSY_menu_bcp_all())

    #定位：人脉首页-主菜单-批量操作-全选-返回
    def RMSY_menu_bcp_all_back_click(self):
        return self.p.click(self.RMSY_menu_bcp_all_back())

    #定位：人脉首页-主菜单-批量操作-全选-全选
    def RMSY_menu_bcp_all_all_click(self):
        return self.p.click(self.RMSY_menu_bcp_all_all())

    #---------------------黑名单-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-黑名单

    #---------------------打标签-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-打标签

    #---------------------换名片-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-换名片

    #---------------------------------------------------联系人列表所有元素定位------------------------------------------------------
    #定位：人脉首页-主菜单-批量操作-联系人列表
    def RMSY_menu_bcp_contacts_click(self, n):
        return self.p.click(self.RMSY_menu_bcp_contacts()[n])