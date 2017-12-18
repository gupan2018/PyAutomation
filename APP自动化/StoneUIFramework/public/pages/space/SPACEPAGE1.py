__author__ = 'xiaoj'
#空间首页
from StoneUIFramework.public.common.basepage import Page

class _SPACEPAGE1(Page):
    #定位:空间列表
    def Kjlb(self):
        self.Kjlb = self.p.get_element("id->com.yunlu6.stone:id/navi_item_zone","空间列表")
        return self.Kjlb

    # 空间列表-主菜单
    def Kjlb_mainmenu(self):
        self.Kjlb_mainmenu = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-主菜单")
        return self.Kjlb_mainmenu

    # 空间列表-浏览空间列表(通过ID查找)
    def Kjlb_browseorgspaceByID(self):
        self.Kjlb_browseorgspaceByID = self.p.get_elements("id->com.yunlu6.stone:id/zone_company_title","空间列表-浏览企业空间(通过ID查找)")
        return self.Kjlb_browseorgspaceByID

    # 空间列表-浏览空间(通过name查找)
    def Kjlb_browseorgspaceByName(self,name):
        self.Kjlb_browseorgspaceByName = self.p.get_element("name->%s"%name,"定位空间列表-浏览企业空间(通过Name查找)失败")
        return self.Kjlb_browseorgspaceByName

    # 空间列表-搜索按钮
    def Kjlb_searchbutton(self):
        self.Kjlb_searchbutton = self.p.get_element("id->com.yunlu6.stone:id/navi_item_zone","空间列表-搜索按钮")
        return self.Kjlb_searchbutton

    # 空间列表-搜索框
    def Kjlb_searchspace(self):
        self.Kjlb_searchspace = self.p.get_element("id->com.yunlu6.stone:id/edit_text","空间列表-搜索框")
        return self.Kjlb_searchspace

    # 空间列表-主菜单-'+机构空间'
    def Kjlb_mainmenu_newspace(self):
        self.Kjlb_mainmenu_newspace = self.p.get_element("id->com.yunlu6.stone:id/btn_new_space","定位空间列表-主菜单-'+机构空间'失败")
        return self.Kjlb_mainmenu_newspace

    # 空间列表-主菜单-'+私人空间'
    def Kjlb_mainmenu_newpersonspace(self):
        self.Kjlb_mainmenu_newpersonspaceP = self.p.get_element("id->com.yunlu6.stone:id/btn_new_person_space","空间列表-主菜单-'+私人空间'")
        return self.Kjlb_mainmenu_newpersonspaceP

    # 空间列表-主菜单-分享名片
    def Kjlb_mainmenu_sharecard(self):
        self.Kjlb_mainmenu_sharecard = self.p.get_element("id->com.yunlu6.stone:id/btn_share_space","空间列表-主菜单-分享名片")
        return self.Kjlb_mainmenu_sharecard