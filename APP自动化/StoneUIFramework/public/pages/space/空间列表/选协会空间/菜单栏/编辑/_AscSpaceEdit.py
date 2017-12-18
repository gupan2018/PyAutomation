__author__ = 'xiaoj'
from StoneUIFramework.public.pages.space.空间列表.选协会空间.菜单栏._AscSpaceMenu import _AscSpaceMenuPage

class _AscSpaceEditPage(_AscSpaceMenuPage):
    #---------------------------------------编辑----------------------------------
    # 空间列表-浏览协会空间-菜单栏-编辑
    def Kjlb_browseascspace_menu_edit(self):
        self.Kjlb_browseascspace_menu_edit = self.p.get_elements("id->com.yunlu6.stone:id/btn_pop_association_edit","空间列表-浏览协会空间-菜单栏-编辑")
        return self.Kjlb_browseascspace_menu_edit

    # 空间列表-浏览协会空间-菜单栏-编辑-返回
    def Kjlb_browseascspace_menu_edit_back(self):
        self.Kjlb_browseascspace_menu_edit_back = self.p.get_elements("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览协会空间-菜单栏-编辑-返回")
        return self.Kjlb_browseascspace_menu_edit_back

    # 空间列表-浏览协会空间-菜单栏-编辑-勾选
    def Kjlb_browseascspace_menu_edit_confirm(self):
        self.Kjlb_browseascspace_menu_edit_confirm = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览协会空间-菜单栏-编辑-勾选")
        return self.Kjlb_browseascspace_menu_edit_confirm

    # 空间列表-浏览协会空间-菜单栏-编辑-企业全称
    def Kjlb_browseascspace_menu_edit_fullname(self):
        self.Kjlb_browseascspace_menu_edit_fullname = self.p.get_element("id->com.yunlu6.stone:id/company_name","空间列表-浏览协会空间-菜单栏-编辑-企业全称")
        return self.Kjlb_browseascspace_menu_edit_fullname

    # 空间列表-浏览协会空间-菜单栏-编辑-企业简称
    def Kjlb_browseascspace_menu_edit_simplename(self):
        self.Kjlb_browseascspace_menu_edit_simplename = self.p.get_element("id->com.yunlu6.stone:id/company_introduce","空间列表-浏览协会空间-菜单栏-编辑-企业简称")
        return self.Kjlb_browseascspace_menu_edit_simplename

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区
    def Kjlb_browseascspace_menu_edit_address(self):
        self.Kjlb_browseascspace_menu_edit_address = self.p.get_element("id->com.yunlu6.stone:id/company_address","空间列表-浏览协会空间-菜单栏-编辑-所在地区")
        return self.Kjlb_browseascspace_menu_edit_address

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区-所在地区列表
    def Kjlb_browseascspace_menu_edit_address_list(self):
        self.Kjlb_browseascspace_menu_edit_address_list = self.p.get_elements("id->com.yunlu6.stone:id/tv_address" ,"空间列表-浏览协会空间-菜单栏-编辑-所在地区")
        return self.Kjlb_browseascspace_menu_edit_address_list

    # 空间列表-浏览协会空间-菜单栏-编辑-详细地址
    def Kjlb_browseascspace_menu_edit_detailaddress(self):
        self.Kjlb_browseascspace_menu_edit_detailaddress = self.p.get_element("id->com.yunlu6.stone:id/company_address_det","空间列表-浏览协会空间-菜单栏-编辑-详细地址")
        return self.Kjlb_browseascspace_menu_edit_detailaddress

    # 空间列表-浏览协会空间-菜单栏-编辑-联系人
    def Kjlb_browseascspace_menu_edit_contact(self):
        self.Kjlb_browseascspace_menu_edit_contact = self.p.get_element("id->com.yunlu6.stone:id/people_name","空间列表-浏览协会空间-菜单栏-编辑-联系人")
        return self.Kjlb_browseascspace_menu_edit_contact

    # 空间列表-浏览协会空间-菜单栏-编辑-手机号
    def Kjlb_browseascspace_menu_edit_phone(self):
        self.Kjlb_browseascspace_menu_edit_phone = self.p.get_element("id->com.yunlu6.stone:id/mobile_phone","空间列表-浏览协会空间-菜单栏-编辑-手机号")
        return self.Kjlb_browseascspace_menu_edit_phone

    # 空间列表-浏览协会空间-菜单栏-编辑-座机号
    def Kjlb_browseascspace_menu_edit_landline(self):
        self.Kjlb_browseascspace_menu_edit_landline = self.p.get_element("id->com.yunlu6.stone:id/phone","空间列表-浏览协会空间-菜单栏-编辑-座机号")
        return self.Kjlb_browseascspace_menu_edit_landline

    # 空间列表-浏览协会空间-菜单栏-编辑-邮箱
    def Kjlb_browseascspace_menu_edit_email(self):
        self.Kjlb_browseascspace_menu_edit_email = self.p.get_element("id->com.yunlu6.stone:id/email","空间列表-浏览协会空间-菜单栏-编辑-邮箱")
        return self.Kjlb_browseascspace_menu_edit_email

    # 空间列表-浏览协会空间-菜单栏-编辑-QQ
    def Kjlb_browseascspace_menu_edit_QQ(self):
        self.Kjlb_browseascspace_menu_edit_QQ = self.p.get_element("id->com.yunlu6.stone:id/qq","空间列表-浏览协会空间-菜单栏-编辑-QQ")
        return self.Kjlb_browseascspace_menu_edit_QQ

    # 空间列表-浏览协会空间-菜单栏-编辑-网站
    def Kjlb_browseascspace_menu_edit_website(self):
        self.Kjlb_browseascspace_menu_edit_website = self.p.get_element("id->com.yunlu6.stone:id/website","空间列表-浏览协会空间-菜单栏-编辑-网站")
        return self.Kjlb_browseascspace_menu_edit_website

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo
    def Kjlb_browseascspace_menu_edit_logo(self):
        self.Kjlb_browseascspace_menu_edit_logo = self.p.get_element("id->com.yunlu6.stone:id/iv_open_logo","空间列表-浏览协会空间-菜单栏-编辑-Logo")
        return self.Kjlb_browseascspace_menu_edit_logo

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo-相册
    def Kjlb_browseascspace_menu_edit_logo_album(self):
        self.Kjlb_browseascspace_menu_edit_logo_album = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_album","空间列表-浏览协会空间-菜单栏-编辑-Logo-相册")
        return self.Kjlb_browseascspace_menu_edit_logo_album

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo-拍照
    def Kjlb_browseascspace_menu_edit_logo_takepic(self):
        self.Kjlb_browseascspace_menu_edit_logo_takepic = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_take_pictures","空间列表-浏览协会空间-菜单栏-编辑-Logo-拍照")
        return self.Kjlb_browseascspace_menu_edit_logo_takepic

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo-取消
    def Kjlb_browseascspace_menu_edit_logo_cancel(self):
        self.Kjlb_browseascspace_menu_edit_logo_cancel = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_cancel","空间列表-浏览协会空间-菜单栏-编辑-Logo-取消")
        return self.Kjlb_browseascspace_menu_edit_logo_cancel