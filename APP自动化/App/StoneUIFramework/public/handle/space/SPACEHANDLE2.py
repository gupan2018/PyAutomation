__author__ = 'xiaoj'
#空间首页
from StoneUIFramework.public.handle.space.SPACEHANDLE1 import _SPACEHANDLE1

class _SPACEHANDLE2(_SPACEHANDLE1):
#*********************************【PAGE1】+机构空间：Kjlb_mainmenu_newspace*********************************
    # 空间列表-主菜单-'+机构空间'-机构全称:发送文本
    def Kjlb_mainmenu_newspace_orgname_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_mainmenu_newspace_orgname(),text)

    # 空间列表-主菜单-'+机构空间'-机构简称:发送文本
    def Kjlb_mainmenu_newspace_orgintro_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_mainmenu_newspace_orgintro(),text)

     # 空间列表-主菜单-'+机构空间'-新建机构空间标题:点击
    def Kjlb_mainmenu_newspace_orgtitle_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_orgtitle())

    # 空间列表-主菜单-'+机构空间'-机构类型:点击
    def Kjlb_mainmenu_newspace_orgtype_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_orgtype())

    # 空间列表-主菜单-'+机构空间'-机构类型-企业:点击
    def Kjlb_mainmenu_newspace_orgtype_company_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_orgtype_company())

    # 空间列表-主菜单-'+机构空间'-机构类型-协会:点击
    def Kjlb_mainmenu_newspace_orgtype_association_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_orgtype_association())

     # 空间列表-主菜单-'+机构空间'-产业角色:点击
    def Kjlb_mainmenu_newspace_industry_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_industry())

    # 空间列表-主菜单-'+机构空间'-产业角色-产业角色标签列表:点击
    def Kjlb_mainmenu_newspace_industry_tag_click(self,n):
        return self.p.click(self.Kjlb_mainmenu_newspace_industry_tag()[n])

    # 空间列表-主菜单-'+机构空间'-客户类型:点击
    def Kjlb_mainmenu_newspace_customertype_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_customertype())

    # 空间列表-主菜单-'+机构空间'-客户类型-客户类型标签列表:点击
    def Kjlb_mainmenu_newspace_customertype_tag_click(self,n):
        return self.p.click(self.Kjlb_mainmenu_newspace_customertype_tag()[n])

    # 空间列表-主菜单-'+机构空间'-客户类型-客户类型确定:点击
    def Kjlb_mainmenu_newspace_customertype_confirm_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_customertype_confirm())

    # 空间列表-主菜单-'+机构空间'-所在地区:点击
    def Kjlb_mainmenu_newspace_area_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_area())

    # 空间列表-主菜单-'+机构空间'-所在地区-省市区列表:点击
    def Kjlb_mainmenu_newspace_area_address_click(self,n):
        return self.p.click(self.Kjlb_mainmenu_newspace_area_address()[n])

    # 空间列表-主菜单-'+机构空间'-详细地址框:点击
    def Kjlb_mainmenu_newspace_addressdetail_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_addressdetail())

    # 空间列表-主菜单-'+机构空间'-详细地址按钮:点击
    def Kjlb_mainmenu_newspace_mapdetail_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_mapdetail())

    # 空间列表-主菜单-'+机构空间'-提交:点击
    def Kjlb_mainmenu_newspace_affirm_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_affirm())

    #----------------------对公账号验证-----------------------
    # 空间列表-主菜单-'+机构空间'-去验证:点击
    def Kjlb_mainmenu_newspace_verifynow_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow())

    # 空间列表-主菜单-'+机构空间'-去验证-返回:点击
    def Kjlb_mainmenu_newspace_verifynow_back_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow_back())

    # 空间列表-主菜单-'+机构空间'-去验证-真实姓名:点击
    def Kjlb_mainmenu_newspace_verifynow_sovereigntyname_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow_sovereigntyname())

    # 空间列表-主菜单-'+机构空间'-去验证-身份证号:点击
    def Kjlb_mainmenu_newspace_verifynow_idnumber_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow_idnumber())

    # 空间列表-主菜单-'+机构空间'-去验证-银行开户名:点击
    def Kjlb_mainmenu_newspace_verifynow_bankname_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow_bankname())

    # 空间列表-主菜单-'+机构空间'-去验证-开户银行:发送文本
    def Kjlb_mainmenu_newspace_verifynow_soverbank_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_mainmenu_newspace_verifynow_soverbank(),text)

    # 空间列表-主菜单-'+机构空间'-去验证-所在地区列表:点击
    def Kjlb_mainmenu_newspace_verifynow_soveraddress_list_click(self,n):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow_soveraddress_list()[n])

    # 空间列表-主菜单-'+机构空间'-去验证-所在地区列表:点击
    def Kjlb_mainmenu_newspace_verifynow_soveraddress_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow_soveraddress())

    # 空间列表-主菜单-'+机构空间'-去验证-支行:发送文本
    def Kjlb_mainmenu_newspace_verifynow_sovermybank_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_mainmenu_newspace_verifynow_sovermybank(),text)

    # 空间列表-主菜单-'+机构空间'-去验证-银行账号:发送文本
    def Kjlb_mainmenu_newspace_verifynow_soverbanknub_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_mainmenu_newspace_verifynow_soverbanknub(),text)

    # 空间列表-主菜单-'+机构空间'-去验证-审核费:点击
    def Kjlb_mainmenu_newspace_verifynow_money_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow_money())

    # 空间列表-主菜单-'+机构空间'-去验证-确定提交:点击
    def Kjlb_mainmenu_newspace_verifynow_soversave_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow_soversave())

    # 空间列表-主菜单-'+机构空间'-去验证-确定提交-返回:点击
    def Kjlb_mainmenu_newspace_verifynow_soversave_back_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace_verifynow_soversave_back())

#*********************************【PAGE1】+私人空间空间：Kjlb_mainmenu_newpersonspace*********************************
   # 空间列表-主菜单-'+私人空间'-返回:点击
    def Kjlb_mainmenu_newpersonspace_back_click(self):
        return self.p.click(self.Kjlb_mainmenu_newpersonspace_back())

    # 空间列表-主菜单-'+私人空间'-选择空间类型列表:点击
    def Kjlb_mainmenu_newpersonspace_choosespacetype_click(self,n):
        return self.p.click(self.Kjlb_mainmenu_newpersonspace_choosespacetype()[n])

    # 空间列表-主菜单-'+私人空间-空间名称:发送文本
    def Kjlb_mainmenu_newpersonspace_spacename_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_mainmenu_newpersonspace_spacename(),text)

    # 空间列表-主菜单-'+私人空间'-切换空间类型:点击
    def Kjlb_mainmenu_newpersonspace_changespacetype_click(self):
        return self.p.click(self.Kjlb_mainmenu_newpersonspace_changespacetype())

     # 空间列表-主菜单-'+私人空间'-文件夹名称:发送文本
    def Kjlb_mainmenu_newpersonspace_foldername_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_mainmenu_newpersonspace_foldername(),text)

    # 空间列- 主菜单-'+私人空间'-推荐空间名标签:点击
    def Kjlb_mainmenu_newpersonspace_suggestspacenametag_click(self):
        return self.p.click(self.Kjlb_mainmenu_newpersonspace_suggestspacenametag())

    # 空间列表-主菜单-'+私人空间'-保存:点击
    def Kjlb_mainmenu_newpersonspace_save_click(self):
        return self.p.click(self.Kjlb_mainmenu_newpersonspace_save())

    # 空间列表-主菜单-'+私人空间'-主界面返回:点击
    def Kjlb_mainmenu_newpersonspace_mainback_click(self):
        return self.p.click(self.Kjlb_mainmenu_newpersonspace_mainback())

#*********************************【PAGE1】+分享名片：Kjlb_mainmenu_sharecard*********************************
    # 空间列表-主菜单-分享名片-返回:点击
    def Kjlb_mainmenu_sharecard_back_click(self):
        return self.p.click(self.Kjlb_mainmenu_sharecard_back())

    # 空间列表-主菜单-分享名片-分享:点击
    def Kjlb_mainmenu_sharecard_share_click(self):
        return self.p.click(self.Kjlb_mainmenu_sharecard_share())

    # 空间列表-主菜单-分享名片-手机:点击
    def Kjlb_mainmenu_sharecard_phone_click(self):
        return self.p.click(self.Kjlb_mainmenu_sharecard_phone())

    # 空间列表-主菜单-分享名片-邮箱:点击
    def Kjlb_mainmenu_sharecard_email_click(self):
        self.Kjlb_mainmenu_sharecard_email = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_email_cb","空间列表-主菜单-分享名片-邮箱")
        return self.p.click(self.Kjlb_mainmenu_sharecard_email())

    # 空间列表-主菜单-分享名片-地址:点击
    def Kjlb_mainmenu_sharecard_address_click(self):
        return self.p.click(self.Kjlb_mainmenu_sharecard_address())

    # 空间列表-主菜单-分享名片-QQ:点击
    def Kjlb_mainmenu_sharecard_qq_click(self):
        return self.p.click(self.Kjlb_mainmenu_sharecard_qq())

    # 空间列表-主菜单-分享名片-空间按钮:点击
    def Kjlb_mainmenu_sharecard_spacebutton_click(self):
        return self.p.click(self.Kjlb_mainmenu_sharecard_spacebutton())

#*********************************【PAGE1】【机构空间】浏览空间列表：Kjlb_browseorgspaceByID*********************************
    # 空间列表-浏览企业空间-返回:点击
    def Kjlb_browseorgspace_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_back())

    # 空间列表-浏览企业空间-菜单栏:点击
    def Kjlb_browseorgspace_menu_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu())

    # 空间列表-浏览企业空间-菜单栏-业务升级:点击
    def Kjlb_browseorgspace_menu_upgrade_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_upgrade())

    #  空间列表-浏览企业空间-菜单栏-产品:点击
    def Kjlb_browseorgspace_menu_product_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product())

    # 空间列表-浏览企业空间-菜单栏-企业名片:点击
    def Kjlb_browseorgspace_menu_bcard_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard())

    # 空间列表-浏览企业空间-菜单栏-团队:点击
    def Kjlb_browseorgspace_menu_team_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team())

    # 空间列表-浏览企业空f间-菜单栏-客户:点击
    def Kjlb_browseorgspace_menu_customer_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer())

    # 空间列表-浏览企业空间-菜单栏-访客:点击
    def Kjlb_browseorgspace_menu_visitor_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_visitor())

    # 空间列表-浏览企业空间-菜单栏-资讯:点击
    def Kjlb_browseorgspace_menu_archivies_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies())

#*********************************【PAGE1】【私人空间】浏览空间列表：Kjlb_browseorgspaceByID*********************************
    # 空间列表-浏览私人空间-返回-点击
    def Kjlb_browseperspace_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_back())

    # 空间列表-浏览私人空间-照片列表
    def Kjlb_browseperspace_piclist_click(self,n):
        return self.p.click(self.Kjlb_browseperspace_piclist()[n])

    # 空间列表-浏览私人空间-菜单栏
    def Kjlb_browseperspace_menu_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu())

    # 空间列表-浏览私人空间-菜单栏-客户
    def Kjlb_browseperspace_menu_customer_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer())

    # 空间列表-浏览私人空间-菜单栏-名片
    def Kjlb_browseperspace_menu_card_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card())

    # 空间列表-浏览私人空间-菜单栏-编辑
    def Kjlb_browseperspace_menu_edit_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit())

    # 空间列表-浏览私人空间-菜单栏-+文件夹
    def Kjlb_browseperspace_menu_addfolder_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_addfolder())

   # 空间列表-浏览私人空间-加数据
    def Kjlb_browseperspace_adata_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata())

    # 空间列表-浏览私人空间-更多
    def Kjlb_browseperspace_more_click(self):
        return self.p.click(self.Kjlb_browseperspace_more())