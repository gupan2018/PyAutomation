__author = 'xiaoj'
from StoneUIFramework.public.pages.space.空间列表.选协会空间.菜单栏._AscSpaceMenu import _AscSpaceMenuPage

class _AscSpaceMemberPage(_AscSpaceMenuPage):
    #--------------------------------------会员-------------------------------------
    # 空间列表-浏览协会空间-菜单栏-会员
    def Kjlb_browseascspace_menu_vip(self):
        self.Kjlb_browseascspace_menu_vip = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_vip","空间列表-浏览协会空间-菜单栏-会员")
        return self.Kjlb_browseascspace_menu_vip

    # 空间列表-浏览协会空间-菜单栏-会员-返回
    def Kjlb_browseascspace_menu_vip_back(self):
        self.Kjlb_browseascspace_menu_vip_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-返回")
        return self.Kjlb_browseascspace_menu_vip_back

    # 空间列表-浏览协会空间-菜单栏-会员-搜索栏
    def Kjlb_browseascspace_menu_vip_search(self):
        self.Kjlb_browseascspace_menu_vip_search = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_keyword","空间列表-浏览协会空间-菜单栏-会员-搜索栏")
        return self.Kjlb_browseascspace_menu_vip_search

    # 空间列表-浏览协会空间-菜单栏-会员-搜索按钮
    def Kjlb_browseascspace_menu_vip_searchbtn(self):
        self.Kjlb_browseascspace_menu_vip_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_search","空间列表-浏览协会空间-菜单栏-会员-搜索按钮")
        return self.Kjlb_browseascspace_menu_vip_searchbtn

    # 空间列表-浏览协会空间-菜单栏-会员-企业名录
    def Kjlb_browseascspace_menu_vip_companylist(self):
        self.Kjlb_browseascspace_menu_vip_companylist = self.p.get_element("id->com.yunlu6.stone:id/ass_select_companylist","空间列表-浏览协会空间-菜单栏-会员-企业名录")
        return self.Kjlb_browseascspace_menu_vip_companylist

    # 空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表
    def Kjlb_browseascspace_menu_vip_companylist_companyname(self):
        self.Kjlb_browseascspace_menu_vip_companylist_companyname = self.p.get_elements("id->com.yunlu6.stone:id/ass_company_name","空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表")
        return self.Kjlb_browseascspace_menu_vip_companylist_companyname

    # 空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表-返回
    def Kjlb_browseascspace_menu_vip_companylist_companyname_back(self):
        self.Kjlb_browseascspace_menu_vip_companylist_companyname_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表-返回")
        return self.Kjlb_browseascspace_menu_vip_companylist_companyname_back

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录
    def Kjlb_browseascspace_menu_vip_personlist(self):
        self.Kjlb_browseascspace_menu_vip_personlist = self.p.get_element("id->com.yunlu6.stone:id/ass_select_personlist","空间列表-浏览协会空间-菜单栏-会员-个人名录")
        return self.Kjlb_browseascspace_menu_vip_personlist

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表
    def Kjlb_browseascspace_menu_vip_personlist_personname(self):
        self.Kjlb_browseascspace_menu_vip_personlist_personname = self.p.get_elements("id->com.yunlu6.stone:id/vip_name","空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表")
        return self.Kjlb_browseascspace_menu_vip_personlist_personname

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表-返回
    def Kjlb_browseascspace_menu_vip_personlist_personname_back(self):
        self.Kjlb_browseascspace_menu_vip_personlist_personname_back = self.p.get_elements("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表-返回")
        return self.Kjlb_browseascspace_menu_vip_personlist_personname_back

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏
    def Kjlb_browseascspace_menu_vip_menu(self):
        self.Kjlb_browseascspace_menu_vip_menu = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览协会空间-菜单栏-会员-菜单栏")
        return self.Kjlb_browseascspace_menu_vip_menu

    #-------------------------------菜单栏下所有元素定位---------------------------
    #--------------加会员---------------
    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员
    def Kjlb_browseascspace_menu_vip_menu_addvip(self):
        self.Kjlb_browseascspace_menu_vip_menu_addvip = self.p.get_element("id->com.yunlu6.stone:id/btn_add_vip","空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员")
        return self.Kjlb_browseascspace_menu_vip_menu_addvip

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-返回
    def Kjlb_browseascspace_menu_vip_menu_addvip_back(self):
        self.Kjlb_browseascspace_menu_vip_menu_addvip_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-返回")
        return self.Kjlb_browseascspace_menu_vip_menu_addvip_back

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-搜索栏
    def Kjlb_browseascspace_menu_vip_menu_addvip_search(self):
        self.Kjlb_browseascspace_menu_vip_menu_addvip_search = self.p.get_element("id->com.yunlu6.stone:id/buildstone_search_key","空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-返回")
        return self.Kjlb_browseascspace_menu_vip_menu_addvip_search

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-搜索按钮
    def Kjlb_browseascspace_menu_vip_menu_addvip_searchbtn(self):
        self.Kjlb_browseascspace_menu_vip_menu_addvip_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-搜索按钮")
        return self.Kjlb_browseascspace_menu_vip_menu_addvip_searchbtn

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-圆圈勾选&个人
    def Kjlb_browseascspace_menu_vip_menu_addvip_chooseperson(self):
        self.Kjlb_browseascspace_menu_vip_menu_addvip_chooseperson = self.p.get_elements("id->com.yunlu6.stone:id/item_client_tv_checked","空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-圆圈勾选&个人")
        return self.Kjlb_browseascspace_menu_vip_menu_addvip_chooseperson

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-圆圈勾选&企业
    def Kjlb_browseascspace_menu_vip_menu_addvip_choosecompany(self):
        self.Kjlb_browseascspace_menu_vip_menu_addvip_choosecompany = self.p.get_elements("id->com.yunlu6.stone:id/assadd_select_icon","空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-圆圈勾选&企业")
        return self.Kjlb_browseascspace_menu_vip_menu_addvip_choosecompany

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-全选
    def Kjlb_browseascspace_menu_vip_menu_addvip_all(self):
        self.Kjlb_browseascspace_menu_vip_menu_addvip_all = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-全选")
        return self.Kjlb_browseascspace_menu_vip_menu_addvip_all

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-添加
    def Kjlb_browseascspace_menu_vip_menu_addvip_confirm(self):
        self.Kjlb_browseascspace_menu_vip_menu_addvip_confirm = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_client_operate","空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-添加")
        return self.Kjlb_browseascspace_menu_vip_menu_addvip_confirm

    #---------------管理----------------
    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理
    def Kjlb_browseascspace_menu_vip_menu_manage(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage = self.p.get_element("id->com.yunlu6.stone:id/btn_add_manage","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理")
        return self.Kjlb_browseascspace_menu_vip_menu_manage

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-返回
    def Kjlb_browseascspace_menu_vip_menu_manage_back(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-返回")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_back

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索栏
    def Kjlb_browseascspace_menu_vip_menu_manage_search(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_search = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_keyword","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索栏")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_search

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索按钮
    def Kjlb_browseascspace_menu_vip_menu_manage_searchbtn(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_search","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索按钮")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_searchbtn

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑
    def Kjlb_browseascspace_menu_vip_menu_manage_edit(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_edit = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_edit

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-取消
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-取消")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-圆圈勾选&个人
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_chooseperson(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_edit_chooseperson = self.p.get_elements("id->com.yunlu6.stone:id/assperson_select","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-圆圈勾选&个人")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_edit_chooseperson

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-圆圈勾选&企业
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany = self.p.get_elements("id->com.yunlu6.stone:id/ass_company_select","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-圆圈勾选&企业")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-同意
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_agree(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_edit_agree = self.p.get_element("id->com.yunlu6.stone:id/ass_company_agree","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-同意")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_edit_agree

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-拒绝
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_refuse(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_edit_refuse = self.p.get_element("id->com.yunlu6.stone:id/ass_company_refuse","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-拒绝")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_edit_refuse

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-移除
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_delete(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_edit_delete = self.p.get_element("id->com.yunlu6.stone:id/ass_company_dele","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-移除")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_edit_delete

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业
    def Kjlb_browseascspace_menu_vip_menu_manage_companyname(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_companyname = self.p.get_elements("id->com.yunlu6.stone:id/ass_company_name","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_companyname

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业-返回
    def Kjlb_browseascspace_menu_vip_menu_manage_companyname_back(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_companyname_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业-返回")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_companyname_back

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人
    def Kjlb_browseascspace_menu_vip_menu_manage_personname(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_personname = self.p.get_elements("id->com.yunlu6.stone:id/vip_name","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_personname

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人-返回
    def Kjlb_browseascspace_menu_vip_menu_manage_personname_back(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_personname_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人-返回")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_personname_back