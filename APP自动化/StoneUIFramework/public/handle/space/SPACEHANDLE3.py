__author__ = 'xiaoj'
#空间首页
from StoneUIFramework.public.handle.space.SPACEHANDLE2 import _SPACEHANDLE2

class _SPACEHANDLE3(_SPACEHANDLE2):
#***************************************【PAGE2】产品Kjlb_browseorgspace_menu_product***************************************
   #  空间列表-浏览企业空间-菜单栏-产品-返回:点击
    def Kjlb_browseorgspace_menu_product_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_back())

     #  空间列表-浏览企业空间-菜单栏-产品-新建:点击
    def Kjlb_browseorgspace_menu_product_new_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new())

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_click(self,n):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list()[n])

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找
    def Kjlb_browseorgspace_menu_product_unlock_list_byname(self,name):
        self.Kjlb_browseorgspace_menu_product_unlock_list_bynameP = self.p.get_elements("name->%s"%name,"空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找")
        return self.Kjlb_browseorgspace_menu_product_unlock_list_bynameP

     #  空间列表-浏览企业空间-菜单栏-产品-未发布
    def Kjlb_browseorgspace_menu_product_unlock_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock())

     #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_byname_click(self,name):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_byname(name)[0])

     #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品名查找:点击
    def Kjlb_browseorgspace_menu_product_lock_list_byname_click(self,name):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_byname(name)[0])

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表:点击
    def Kjlb_browseorgspace_menu_product_lock_list_click(self,n):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list()[n])

    #  空间列表-浏览企业空间-菜单栏-产品-已发布:点击
    def Kjlb_browseorgspace_menu_product_lock_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock())

    # 空间列表-浏览企业空间-菜单栏-产品-收款账号:点击
    def Kjlb_browseorgspace_menu_product_account_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_account())

    # 空间列表-浏览企业空间-菜单栏-产品-搜索:点击
    def Kjlb_browseorgspace_menu_product_seek_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_seek())

#***************************************【PAGE2】团队Kjlb_browseorgspace_menu_team***************************************
    # 空间列表-浏览企业空间-菜单栏-团队-返回:点击
    def Kjlb_browseorgspace_menu_team_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_back())

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏:点击
    def Kjlb_browseorgspace_menu_team_menu_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu())

     # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob())

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门:点击
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_mydepartment())

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-返回:点击
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_mydepartment_back())

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-搜索:点击
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_seek_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_mydepartment_seek())

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑:点击
    def Kjlb_browseorgspace_menu_team_teamedit_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_teamedit())

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮列表:点击
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self,n):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_teamedit_numeidtL()[n])

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数:发送文本
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit(),text)

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否:点击
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel())

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是:点击
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm())

#***************************************【PAGE2】资讯Kjlb_browseorgspace_menu_archivies***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-返回:点击
    def Kjlb_browseorgspace_menu_archivies_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_back())

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮:点击
    def Kjlb_browseorgspace_menu_archivies_new_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new())

    # 空间列表-浏览企业空间-菜单栏-资讯-图片新增:点击
    def Kjlb_browseorgspace_menu_archivies_picadd_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_picadd())

    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表:点击
    def Kjlb_browseorgspace_menu_archivies_pic_click(self,n):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_pic()[n])

#***************************************【PAGE2】企业名片Kjlb_browseorgspace_menu_bcard***************************************
    # 空间列表-浏览企业空间-菜单栏-企业名片-返回:点击
    def Kjlb_browseorgspace_menu_bcard_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_back())

     # 空间列表-浏览企业空间-菜单栏-企业名片-企业资信:点击
    def Kjlb_browseorgspace_menu_bcard_credit_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_credit())

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏:点击
    def Kjlb_browseorgspace_menu_bcard_menu_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu())

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队:点击
    def Kjlb_browseorgspace_menu_bcard_menu_quitteam_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_quitteam())

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-是:点击
    def Kjlb_browseorgspace_menu_bcard_menu_quitteam_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_confirm())

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-否:点击
    def Kjlb_browseorgspace_menu_bcard_menu_quitteam_cancel_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_cancell())

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-附近商家:点击
    def Kjlb_browseorgspace_menu_bcard_menu_nearby_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_nearby())

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑:点击
    def Kjlb_browseorgspace_menu_bcard_menu_edit_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_edit())

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-设置:点击
    def Kjlb_browseorgspace_menu_bcard_menu_setting_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_setting())

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-关闭:点击
    def Kjlb_browseorgspace_menu_bcard_menu_close_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_close())

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share())

    # 空间列表-浏览企业空间-菜单栏-企业名片-联系方式列表:点击
    def Kjlb_browseorgspace_menu_bcard_contactlist_click(self,n):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_contactlist()[n])

    # 空间列表-浏览企业空间-菜单栏-企业名片-资讯:点击
    def Kjlb_browseorgspace_menu_bcard_archivies_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_archivies())

    # 空间列表-浏览企业空间-菜单栏-企业名片-点击创建产品:点击
    def Kjlb_browseorgspace_menu_bcard_newpro_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_newpro())

#***************************************【PAGE2】访客Kjlb_browseorgspace_menu_visitor***************************************
    # 空间列表-浏览企业空间-菜单栏-访客-访客列表:点击
    def Kjlb_browseorgspace_menu_visitor_list_click(self,n):
        return self.p.click(self.Kjlb_browseorgspace_menu_visitor_list()[n])

    # 空间列表-浏览企业空间-菜单栏-访客-访客列表-返回:点击
    def Kjlb_browseorgspace_menu_visitor_list_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_visitor_list_back())

#***************************************【PAGE2】客户Kjlb_browseorgspace_menu_customer***************************************
    # 空间列表-浏览企业空间-菜单栏-客户-返回:点击
    def Kjlb_browseorgspace_menu_customer_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_back())

     # 空间列表-浏览企业空间-菜单栏-客户-搜索框:发送文本
    def Kjlb_browseorgspace_menu_customer_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_customer_search(),text)

    # 空间列表-浏览企业空间-菜单栏-客户-搜索:点击
    def Kjlb_browseorgspace_menu_customer_seek_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_seek())

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏:点击
    def Kjlb_browseorgspace_menu_customer_menu_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu())

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表
    def Kjlb_browseorgspace_menu_customer_clist_click(self,n):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_clist()[n])

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户:点击
    def Kjlb_browseorgspace_menu_customer_menu_add_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_add())

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作:点击
    def Kjlb_browseorgspace_menu_customer_menu_batch_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_batch())

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-返回:点击
    def Kjlb_browseorgspace_menu_customer_menu_batch_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_batch_back())

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选:点击
    def Kjlb_browseorgspace_menu_customer_menu_batch_all_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_batch_all())

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-圆圈勾选列表:点击
    def Kjlb_browseorgspace_menu_customer_menu_batch_choose_click(self,n):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_batch_choose()[n])

#***************************************【PAGE2】业务升级Kjlb_browseorgspace_menu_upgrade***************************************
    # 空间列表-浏览企业空间-菜单栏-业务升级-开启:点击
    def Kjlb_browseorgspace_menu_upgrade_open_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_upgrade_open())

    # 空间列表-浏览企业空间-菜单栏-业务升级-返回:点击
    def Kjlb_browseorgspace_menu_upgrade_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_upgrade_back())

#***************************************【PAGE2】照片列表(包括点击照片加数据)Kjlb_browseperspace_piclist***************************************
    # 空间列表-浏览私人空间-照片列表-菜单栏
    def Kjlb_browseperspace_piclist_menu_click(self,n):
        return self.p.click(self.Kjlb_browseperspace_piclist_menu()[n])

    # 空间列表-浏览私人空间-照片列表-分类到
    def Kjlb_browseperspace_piclist_classify_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_classify())

   # 空间列表-浏览私人空间-照片列表-编辑
    def Kjlb_browseperspace_piclist_edit_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_edit())

    # 空间列表-浏览私人空间-照片列表-返回
    def Kjlb_browseperspace_piclist_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_back())

   # 空间列表-浏览私人空间-照片列表-照片本身
    def Kjlb_browseperspace_piclist_itself_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_itself())

    # 空间列表-浏览私人空间-文件夹名称列表
    def Kjlb_browseperspace_foldername_click(self,n):
        return self.p.click(self.Kjlb_browseperspace_foldernameP()[n])

    # 空间列表-浏览私人空间-加数据-相册
    def Kjlb_browseperspace_addData_ByAlbum_click(self):
        return self.p.click(self.Kjlb_browseperspace_addData_ByAlbum())

#***************************************【PAGE2】菜单栏-名片Kjlb_browseperspace_menu_card***************************************
    # 空间列表-浏览私人空间-菜单栏-名片-返回
    def Kjlb_browseperspace_menu_card_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_back())

    # 空间列表-浏览私人空间-菜单栏-名片-分享
    def Kjlb_browseperspace_menu_card_share_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share())

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信
    def Kjlb_browseperspace_menu_card_share_wechat_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_wechat())

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信朋友圈
    def Kjlb_browseperspace_menu_card_share_circle_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_circle())

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ空间
    def Kjlb_browseperspace_menu_card_share_qqzone_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_qqzone())

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ
    def Kjlb_browseperspace_menu_card_share_qq_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_qq())

    # 空间列表-浏览私人空间-菜单栏-名片-分享-新浪微博
    def Kjlb_browseperspace_menu_card_share_sina_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_sina())

    # 空间列表-浏览私人空间-菜单栏-名片-分享-取消
    def Kjlb_browseperspace_menu_card_share_cancel_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_cancel())

    # 空间列表-浏览私人空间-菜单栏-名片-手机
    def Kjlb_browseperspace_menu_card_phone_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_phone())

    # 空间列表-浏览私人空间-菜单栏-名片-邮箱
    def Kjlb_browseperspace_menu_card_email_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_email())

    # 空间列表-浏览私人空间-菜单栏-名片-地址
    def Kjlb_browseperspace_menu_card_address_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_address())

    # 空间列表-浏览私人空间-菜单栏-名片-QQ
    def Kjlb_browseperspace_menu_card_QQ_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_QQ())

    # 空间列表-浏览私人空间-菜单栏-名片-有效期
    def Kjlb_browseperspace_menu_card_limit_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_limit())

    # 空间列表-浏览私人空间-菜单栏-编辑-删除文件夹列表
    def Kjlb_browseperspace_menu_edit_deletefolder_click(self,n):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_deletefolder()[n])

    # 空间列表-浏览私人空间-菜单栏-编辑-修改文件夹图标列表
    def Kjlb_browseperspace_menu_edit_editfolder_click(self,n):
        return  self.p.click(self.Kjlb_browseperspace_menu_edit_editfolderP()[n])

     # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表
    def Kjlb_browseperspace_menu_edit_editfolder_fname_sendkeys(self,name):
        return self.p.send_keys(self.Kjlb_browseperspace_menu_edit_editfolder_fname(),name)

     # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-是
    def Kjlb_browseperspace_menu_edit_editfolder_fname_OK_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_OK())

    # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-否
    def Kjlb_browseperspace_menu_edit_editfolder_fname_NO_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NO())

    # 空间列表-浏览私人空间-菜单栏-编辑-+数据
    def Kjlb_browseperspace_menu_edit_adddata_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_adddata())

    # 空间列表-浏览私人空间-菜单栏-编辑-空间类型
    def Kjlb_browseperspace_menu_edit_spacetype_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacetype())

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间
    def Kjlb_browseperspace_menu_edit_deletespace_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_deletespace())

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-是
    def Kjlb_browseperspace_menu_edit_deletespace_OK_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_deletespace_OK())

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-否
    def Kjlb_browseperspace_menu_edit_deletespace_NO_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_deletespace_NO())

    # 空间列表-浏览私人空间-菜单栏-编辑-返回
    def Kjlb_browseperspace_menu_edit_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_back())

     # 空间列表-浏览私人空间-菜单栏-编辑-空间名
    def Kjlb_browseperspace_menu_edit_spacename_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacename())

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称列表(0)
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_sendkeys(self,n,name):
        return self.p.send_keys(self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit()[n],name)

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-是
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_OK_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_OK())

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-否
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NO_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NO())

#***************************************【PAGE2】菜单栏-客户Kjlb_browseperspace_menu_customer***************************************
    # 空间列表-浏览私人空间-菜单栏-客户-返回
    def Kjlb_browseperspace_menu_customer_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_back())

    # 空间列表-浏览私人空间-菜单栏-客户-搜索栏
    def Kjlb_browseperspace_menu_customer_search_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_search())

     # 空间列表-浏览私人空间-菜单栏-客户-搜索按钮
    def Kjlb_browseperspace_menu_customer_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_searchbtn())

    # 空间列表-浏览私人空间-菜单栏-客户-菜单
    def Kjlb_browseperspace_menu_customer_menu_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_menu())

    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户
    def Kjlb_browseperspace_menu_customer_menu_addcus_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_menu_addcus())

   # 空间列表-浏览私人空间-菜单栏-客户-客户列表
    def Kjlb_browseperspace_menu_customer_clist_click(self,n):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_clist()[n])

    # 空间列表-浏览私人空间-菜单栏-客户-群聊
    def Kjlb_browseperspace_menu_customer_gchat_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_gchat())

    # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称
    def Kjlb_browseperspace_menu_addfolder_confirm_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_addfolder_confirm())

     # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称
    def Kjlb_browseperspace_menu_addfolder_foldername_sendkeys(self,name):
        return self.p.send_keys(self.Kjlb_browseperspace_menu_addfolder_foldername(),name)

    # 空间列表-浏览私人空间-菜单栏-+文件夹-返回
    def Kjlb_browseperspace_menu_addfolder_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_addfolder_back())

#***************************************【PAGE2】+数据Kjlb_browseperspace_adata***************************************
    # 空间列表-浏览私人空间-加数据-相册
    def Kjlb_browseperspace_adata_ByAlbum_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata_ByAlbum())

    # 空间列表-浏览私人空间-加数据-拍照
    def Kjlb_browseperspace_adata_ByTakepic_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata_ByTakepic())

    # 空间列表-浏览私人空间-加数据-取消
    def Kjlb_browseperspace_adata_cancel_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata_cancel())

#***************************************【PAGE2】更多Kjlb_browseperspace_more***************************************
    # 空间列表-浏览私人空间-更多-照片列表
    def Kjlb_browseperspace_more_piclist_click(self,n):
        return self.p.click(self.Kjlb_browseperspace_more_piclist()[n])

    # 空间列表-浏览私人空间-更多-返回
    def Kjlb_browseperspace_more_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_back())

    # 空间列表-浏览私人空间-更多-菜单栏
    def Kjlb_browseperspace_more_menu_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu())

    # 空间列表-浏览私人空间-更多-菜单栏-上传
    def Kjlb_browseperspace_more_menu_upload_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload())

    # 空间列表-浏览私人空间-更多-菜单栏-上传-相册
    def Kjlb_browseperspace_more_menu_upload_ByAlbum_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload_ByAlbum())

    # 空间列表-浏览私人空间-更多-菜单栏-上传-拍照
    def Kjlb_browseperspace_more_menu_upload_ByTakepic_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload_ByTakepic())

    # 空间列表-浏览私人空间-更多-菜单栏-上传-取消
    def Kjlb_browseperspace_more_menu_upload_cancel_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload_cancel())

    # 空间列表-浏览私人空间-更多-菜单栏-编辑
    def Kjlb_browseperspace_more_menu_edit_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_edit())

    # 空间列表-浏览私人空间-更多-菜单栏-排序
    def Kjlb_browseperspace_more_menu_sort_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_sort())