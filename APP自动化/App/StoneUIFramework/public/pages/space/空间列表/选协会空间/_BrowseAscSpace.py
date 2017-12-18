__author__ = 'xiaoj'
from StoneUIFramework.public.pages.space.空间列表.废_SpaceIndex import _SpaceIndexPage

class _BrowseAscSpacePage(_SpaceIndexPage):
    # 空间列表-浏览协会空间
    def Kjlb_browseascspace(self):
        self.Kjlb_browseascspace = self.p.find_elements_by_id("id->com.yunlu6.stone:id/zone_company_title","空间列表-浏览协会空间")
        return self.Kjlb_browseascspace

    #-------------------------------------------------------菜单栏下所有元素定位------------------------------------------------
    #--------------------------------------团队-------------------------------------
    # 空间列表-浏览协会空间-菜单栏-团队
    def Kjlb_browseascspace_menu_team(self):
        self.Kjlb_browseascspace_menu_team = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_member""空间列表-浏览协会空间-菜单栏-团队")
        return self.Kjlb_browseascspace_menu_team

    # 空间列表-浏览协会空间-菜单栏-团队-返回
    def Kjlb_browseascspace_menu_team_back(self):
        self.Kjlb_browseascspace_menu_team_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-团队-返回")
        return self.Kjlb_browseascspace_menu_team_back

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏
    def Kjlb_browseascspace_menu_team_menu(self):
        self.Kjlb_browseascspace_menu_team_menu = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览协会空间-菜单栏-团队-菜单栏")
        return self.Kjlb_browseascspace_menu_team_menu

    #---------------人事任免所有元素定位---------------
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免
    def Kjlb_browseascspace_menu_team_menu_assignjob(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob = self.p.get_element("id->com.yunlu6.stone:id/pop_teamedit_personnel","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-返回
    def Kjlb_browseascspace_menu_team_menu_assignjob_back(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-返回")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_back

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-搜索栏
    def Kjlb_browseascspace_menu_team_menu_assignjob_search(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_search = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_keyword","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-搜索栏")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_search

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-搜索按钮
    def Kjlb_browseascspace_menu_team_menu_assignjob_searchbtn(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_search","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-搜索按钮")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_searchbtn

    #---------------联系人列表---------------
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact = self.p.find_elements_by_id("id->com.yunlu6.stone:id/removaljobs_name","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-返回
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_back(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_back = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-返回")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_back

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-确认
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_confrim(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_confirm = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-确认")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_confirm

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-部门名称
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_department(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_department = self.p.find_elements_by_id("id->com.yunlu6.stone:id/setjobs_unassi_jobname","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-部门名称")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_department

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-职位名称
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname = self.p.find_elements_by_id("id->com.yunlu6.stone:id/tag_id","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-职位名称")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-移除
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete = self.p.get_element("id->com.yunlu6.stone:id/setjobs_dele","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-移除")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete

    #---------------人事任免新增---------------
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson = self.p.get_element("id->com.yunlu6.stone:id/removaljobs_addperson_img","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-返回
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-返回")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索栏
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search = self.p.get_element("id->com.yunlu6.stone:id/img_btn_search","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索栏")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索按钮
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_search","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索按钮")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-全选
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-全选")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选列表
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_choose(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all = self.p.find_elements_by_id("id->com.yunlu6.stone:id/item_client_tv_checked","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-联系人列表
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contact(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contact = self.p.find_elements_by_id("id->com.yunlu6.stone:id/item_client_username_tv","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contact

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-添加(确认)
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_client_operate","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-添加")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm

    #---------------我的部门所有元素定位---------------
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门
    def Kjlb_browseascspace_menu_team_menu_mydepartment(self):
        self.Kjlb_browseascspace_menu_team_menu_mydepartment = self.p.get_element("id->com.yunlu6.stone:id/pop_teamedit_personnel","空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门")
        return self.Kjlb_browseascspace_menu_team_menu_mydepartment

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门-返回
    def Kjlb_browseascspace_menu_team_menu_mydepartment_back(self):
        self.Kjlb_browseascspace_menu_team_menu_mydepartment_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back","空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门-返回")
        return self.Kjlb_browseascspace_menu_team_menu_mydepartment_back

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门-搜索
    def Kjlb_browseascspace_menu_team_menu_mydepartment_seek(self):
        self.Kjlb_browseascspace_menu_team_menu_mydepartment_seek = self.p.get_element("id->com.yunlu6.stone:id/et_seek","空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门-搜索")
        return self.Kjlb_browseascspace_menu_team_menu_mydepartment_seek

    #---------------团队编辑所有元素定位---------------
    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑
    def Kjlb_browseascspace_menu_team_teamedit(self):
        self.Kjlb_browseascspace_menu_team_teamedit = self.p.get_element("id->com.yunlu6.stone:id/companyteam_btn_edit","空间列表-浏览协会空间-菜单栏-团队-团队编辑")
        return self.Kjlb_browseascspace_menu_team_teamedit

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮
    def Kjlb_browseascspace_menu_team_teamedit_numeidt(self):
        self.Kjlb_browseascspace_menu_team_teamedit_numeidt = self.p.get_element("id->com.yunlu6.stone:id/companyteam_item_edit","空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数按钮")
        return self.Kjlb_browseascspace_menu_team_teamedit_numeidt

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit(self):
        self.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit = self.p.get_element("id->com.yunlu6.stone:id/teamedit_jobs_editnum","空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮")
        return self.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel(self):
        self.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel = self.p.get_element("id->com.yunlu6.stone:id/teamedit_cancleedit","空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮-否")
        return self.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm(self):
        self.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm = self.p.get_element("id->com.yunlu6.stone:id/teamedit_commitedit","空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数-职位人数按钮-是")
        return self.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm

