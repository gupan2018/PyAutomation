__author__ = 'xiaoj'
from StoneUIFramework.public.pages.space.空间列表.选协会空间.菜单栏._AscSpaceMenu import _AscSpaceMenuPage

class _AscSpaceAddMemberPage(_AscSpaceMenuPage):
    #--------------------------------------加会员-------------------------------------
    #定位:空间列表-浏览协会空间-菜单栏-加会员
    def Kjlb_browseascspace_menu_addvip(self):
        self.Kjlb_browseascspace_menu_addvip = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_addvip","空间列表-浏览协会空间-菜单栏-会员失败")
        return self.Kjlb_browseascspace_menu_addvip

    #定位:空间列表-浏览协会空间-菜单栏-加会员-取消
    def Kjlb_browseascspace_menu_addvip_cancel(self):
        self.Kjlb_browseascspace_menu_addvip_cancel = self.p.get_element("id->com.yunlu6.stone:id/pop_assvip_cancle","空间列表-浏览协会空间-菜单栏-会员-取消失败")
        return self.Kjlb_browseascspace_menu_addvip_cancel

    #--------------------个人会员下所有元素定位------------------
    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员
    def Kjlb_browseascspace_menu_addvip_addperson(self):
        self.Kjlb_browseascspace_menu_addvip_addperson = self.p.get_element("id->com.yunlu6.stone:id/pop_assvip_addperson","空间列表-浏览协会空间-菜单栏-会员-个人会员失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-返回
    def Kjlb_browseascspace_menu_addvip_addperson_back(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-个人会员-返回失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_back

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索栏
    def Kjlb_browseascspace_menu_addvip_addperson_search(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_search = self.p.get_element("id->com.yunlu6.stone:id/et_search","空间列表-浏览协会空间-菜单栏-会员-个人会员-搜索栏失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_search
    
    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索按钮
    def Kjlb_browseascspace_menu_addvip_addperson_searchbtn(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览协会空间-菜单栏-会员-个人会员-搜索按钮失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_searchbtn

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-全选
    def Kjlb_browseascspace_menu_addvip_addperson_all(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_all = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览协会空间-菜单栏-会员-个人会员-全选失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_all

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-圆圈勾选列表
    def Kjlb_browseascspace_menu_addvip_addperson_choose(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_choose = self.p.get_elements("id->com.yunlu6.stone:id/item_client_tv_checked","空间列表-浏览协会空间-菜单栏-会员-个人会员-圆圈勾选失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_choose

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-添加
    def Kjlb_browseascspace_menu_addvip_addperson_confirm(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_confirm = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_client_operate","空间列表-浏览协会空间-菜单栏-会员-个人会员-添加失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_confirm

    #-------------------企业会员下所有元素定位------------------
    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员
    def Kjlb_browseascspace_menu_addvip_addcompany(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany = self.p.get_element("id->com.yunlu6.stone:id/pop_assvip_addcompany","空间列表-浏览协会空间-菜单栏-会员-企业会员失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-返回
    def Kjlb_browseascspace_menu_addvip_addcompany_back(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-企业会员-返回失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_back

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏
    def Kjlb_browseascspace_menu_addvip_addcompany_search(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_search = self.p.get_element("id->com.yunlu6.stone:id/et_search","空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索栏失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_search

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索按钮
    def Kjlb_browseascspace_menu_addvip_addcompany_searchbtn(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索按钮失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_searchbtn

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-圆圈勾选列表
    def Kjlb_browseascspace_menu_addvip_addcompany_choose(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_choose = self.p.get_element("id->com.yunlu6.stone:id/item_client_tv_checked","空间列表-浏览协会空间-菜单栏-会员-企业会员-圆圈勾选失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_choose

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-确定
    def Kjlb_browseascspace_menu_addvip_addcompany_confirm(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_confirm = self.p.get_element("id->com.yunlu6.stone:id/company_search_assadd","空间列表-浏览协会空间-菜单栏-会员-企业会员-确定失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_confirm

    #---------------菜单栏--------------
    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-菜单栏
    def Kjlb_browseascspace_menu_addvip_addcompany_menu(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_menu = self.p.get_element("id->com.yunlu6.stone:id/iv_more","空间列表-浏览协会空间-菜单栏-会员-企业会员-菜单栏失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_menu

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_nearby = self.p.get_element("id->com.yunlu6.stone:id/ll_recover","空间列表-浏览协会空间-菜单栏-会员-企业会员-我的附近失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_nearby

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-返回
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_back(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_back = self.p.get_element("id->com.yunlu6.stone:id/buildstione_backe","空间列表-浏览协会空间-菜单栏-会员-企业会员-我的附近-返回失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_back

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-搜索栏
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_search(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_search = self.p.get_element("id->com.yunlu6.stone:id/et_search","空间列表-浏览协会空间-菜单栏-会员-企业会员-我的附近-搜索栏失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_search

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-搜索按钮
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_searchbtn","空间列表-浏览协会空间-菜单栏-会员-企业会员-我的附近-搜索按钮失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-确定
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm = self.p.get_element("id->com.yunlu6.stone:id/iv_more","空间列表-浏览协会空间-菜单栏-会员-企业会员-我的附近-确定失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-路线
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_route(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_route = self.p.get_elements("id->com.yunlu6.stone:id/tv","空间列表-浏览协会空间-菜单栏-会员-企业会员-我的附近-路线失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_route

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-路线-返回
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back = self.p.get_elements("id->com.yunlu6.stone:id/tv","空间列表-浏览协会空间-菜单栏-会员-企业会员-我的附近-路线-返回失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back