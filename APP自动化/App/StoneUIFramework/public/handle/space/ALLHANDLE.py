    #---------------------------------------------------未发布列表所有元素定位------------------------------------------------------
    #  空间列表-浏览企业空间-菜单栏-产品-未发布:点击
    def Kjlb_browseorgspace_menu_product_unlock_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock())

    # 空间列表-浏览协会空间:点击
    def Kjlb_browseascspace_click(self):
        return self.p.click(self.Kjlb_browseascspace())

    # 空间列表-浏览协会空间-返回:点击
    def Kjlb_browseascspace_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_back())

    #定位:空间列表-浏览协会空间-菜单栏:点击
    def Kjlb_browseascspace_menu_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu())


    #---------------------------------------编辑----------------------------------
    # 空间列表-浏览协会空间-菜单栏-编辑:点击
    def Kjlb_browseascspace_menu_edit_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit())

    # 空间列表-浏览协会空间-菜单栏-编辑-返回:点击
    def Kjlb_browseascspace_menu_edit_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_back())

    # 空间列表-浏览协会空间-菜单栏-编辑-勾选:点击
    def Kjlb_browseascspace_menu_edit_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_confirm())

    # 空间列表-浏览协会空间-菜单栏-编辑-企业全称:发送文本
    def Kjlb_browseascspace_menu_edit_fullname_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_fullname(),text)

    # 空间列表-浏览协会空间-菜单栏-编辑-企业简称:发送文本
    def Kjlb_browseascspace_menu_edit_simplename_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_simplename(),text)

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区:点击
    def Kjlb_browseascspace_menu_edit_address_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_address())

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区-所在地区列表
    def Kjlb_browseascspace_menu_edit_address_list_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_address_list())

    # 空间列表-浏览协会空间-菜单栏-编辑-详细地址:发送文本
    def Kjlb_browseascspace_menu_edit_detailaddress_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_detailaddress(),text)

    # 空间列表-浏览协会空间-菜单栏-编辑-联系人:发送文本
    def Kjlb_browseascspace_menu_edit_contact_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_contact(),text)

    # 空间列表-浏览协会空间-菜单栏-编辑-手机号:发送文本
    def Kjlb_browseascspace_menu_edit_phone_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_phone(),text)

    # 空间列表-浏览协会空间-菜单栏-编辑-座机号:发送文本
    def Kjlb_browseascspace_menu_edit_landline_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_landline(),text)

    # 空间列表-浏览协会空间-菜单栏-编辑-邮箱:发送文本
    def Kjlb_browseascspace_menu_edit_email_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_email(),text)

    # 空间列表-浏览协会空间-菜单栏-编辑-QQ:发送文本
    def Kjlb_browseascspace_menu_edit_QQ_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_QQ(),text)

    # 空间列表-浏览协会空间-菜单栏-编辑-网站:发送文本
    def Kjlb_browseascspace_menu_edit_website_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_website(),text)

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo:点击
    def Kjlb_browseascspace_menu_edit_logo_sendkeys(self,text):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_logo())

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo-相册:点击
    def Kjlb_browseascspace_menu_edit_logo_album_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_logo_album())

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo-拍照:点击
    def Kjlb_browseascspace_menu_edit_logo_takepic_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_logo_takepic())

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo-取消:点击
    def Kjlb_browseascspace_menu_edit_logo_cancel_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_logo_cancel())

    #--------------------------------------团队-------------------------------------
    # 空间列表-浏览协会空间-菜单栏-团队:点击
    def Kjlb_browseascspace_menu_team_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team())

    # 空间列表-浏览协会空间-菜单栏-团队-返回:点击
    def Kjlb_browseascspace_menu_team_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_back())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏:点击
    def Kjlb_browseascspace_menu_team_menu_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu())

    #---------------人事任免所有元素定位---------------
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-返回:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_back())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-搜索栏:发送文本
    def Kjlb_browseascspace_menu_team_menu_assignjob_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_team_menu_assignjob_search(),text)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-搜索按钮:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_searchbtn())

    #---------------联系人列表---------------
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact()[n])

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-返回:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_back())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-确认:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_confrim_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_confirm())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-部门名称:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_department_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_department())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-职位名称:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-移除:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete())

    #---------------人事任免新增---------------
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-返回:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索栏:发送文本
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search(),text)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索按钮:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-全选:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选列表:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_choose_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all()[n])

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-联系人列表:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contact_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contact()[n])

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-添加(确认):点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm())

    #---------------我的部门所有元素定位---------------
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门:点击
    def Kjlb_browseascspace_menu_team_menu_mydepartment_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_mydepartment())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门-返回:点击
    def Kjlb_browseascspace_menu_team_menu_mydepartment_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_mydepartment_back())

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门-搜索:点击
    def Kjlb_browseascspace_menu_team_menu_mydepartment_seek_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_mydepartment_seek())

    #---------------团队编辑所有元素定位---------------
    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑:点击
    def Kjlb_browseascspace_menu_team_teamedit_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_teamedit())

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮:点击
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_teamedit_numeidt())

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数:发送文本
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit(),text)

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否:点击
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel())

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是:点击
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm())

    #--------------------------------------加会员-------------------------------------
    #定位:空间列表-浏览协会空间-菜单栏-加会员:点击
    def Kjlb_browseascspace_menu_addvip_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-取消:点击
    def Kjlb_browseascspace_menu_addvip_cancel_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_cancel())

    #--------------------个人会员下所有元素定位------------------
    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员:点击
    def Kjlb_browseascspace_menu_addvip_addperson_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-返回:点击
    def Kjlb_browseascspace_menu_addvip_addperson_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson_back())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索栏:发送文本
    def Kjlb_browseascspace_menu_addvip_addperson_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_addvip_addperson_search(),text)

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索按钮:点击
    def Kjlb_browseascspace_menu_addvip_addperson_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson_searchbtn())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-全选:点击
    def Kjlb_browseascspace_menu_addvip_addperson_all_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson_all())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-圆圈勾选列表:点击
    def Kjlb_browseascspace_menu_addvip_addperson_choose_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson_choose()[n])

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-添加:点击
    def Kjlb_browseascspace_menu_addvip_addperson_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson_confirm())

    #-------------------企业会员下所有元素定位------------------
    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-返回:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_back())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏:发送文本
    def Kjlb_browseascspace_menu_addvip_addcompany_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_addvip_addcompany_search(),text)

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索按钮:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_searchbtn())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-圆圈勾选列表:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_choose_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_choose()[n])

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-确定:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_confirm())

    #---------------菜单栏--------------
    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-菜单栏:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_menu_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_menu())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-返回:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_back())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-搜索栏:发送文本
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_search(),text)

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-搜索按钮:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-确定:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-路线:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_route())

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-路线-返回:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back())

    #--------------------------------------会员-------------------------------------
    # 空间列表-浏览协会空间-菜单栏-会员:点击
    def Kjlb_browseascspace_menu_vip_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip())

    # 空间列表-浏览协会空间-菜单栏-会员-返回:点击
    def Kjlb_browseascspace_menu_vip_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_back())

    # 空间列表-浏览协会空间-菜单栏-会员-搜索栏:发送文本
    def Kjlb_browseascspace_menu_vip_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_vip_search(),text)

    # 空间列表-浏览协会空间-菜单栏-会员-搜索按钮:点击
    def Kjlb_browseascspace_menu_vip_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_searchbtn())

    # 空间列表-浏览协会空间-菜单栏-会员-企业名录:点击
    def Kjlb_browseascspace_menu_vip_companylist_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_companylist())

    # 空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表:点击
    def Kjlb_browseascspace_menu_vip_companylist_companyname_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_companylist_companyname()[n])

    # 空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表-返回:点击
    def Kjlb_browseascspace_menu_vip_companylist_companyname_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_companylist_companyname_back())

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录:点击
    def Kjlb_browseascspace_menu_vip_personlist_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_personlist())

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表:点击
    def Kjlb_browseascspace_menu_vip_personlist_personname_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_personlist_personname()[n])

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表-返回
    def Kjlb_browseascspace_menu_vip_personlist_personname_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_personlist_personname_back())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏:点击
    def Kjlb_browseascspace_menu_vip_menu_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu())

    #-------------------------------菜单栏下所有元素定位---------------------------
    #--------------加会员---------------
    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-返回:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_back())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-搜索栏:发送文本
    def Kjlb_browseascspace_menu_vip_menu_addvip_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_vip_menu_addvip_search(),text)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-搜索按钮:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_searchbtn())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-圆圈勾选&个人:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_chooseperson_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_chooseperson())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-圆圈勾选&企业:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_choosecompany_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_choosecompany())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-全选:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_all_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_all())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-添加:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_confirm())

    #---------------管理----------------
    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-返回:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_back())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索栏:发送文本
    def Kjlb_browseascspace_menu_vip_menu_manage_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_vip_menu_manage_search(),text)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索按钮:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_searchbtn())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-取消:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-圆圈勾选&个人:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_chooseperson_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_chooseperson())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-圆圈勾选&企业:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-同意:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_agree_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_agree())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-拒绝:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_refuse_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_refuse())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-移除:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_delete_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_delete())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_companyname_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_companyname()[n])

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业-返回:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_companyname_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_companyname_back())

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_personname_click(self,n):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_personname()[n])

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人-返回:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_personname_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_personname_back())



