__author__ = 'xiaoj'
#空间首页
from StoneUIFramework.public.pages.space.SPACEPAGE2 import _SPACEPAGE2

class _SPACEPAGE3(_SPACEPAGE2):
#***************************************【PAGE2】产品Kjlb_browseorgspace_menu_product***************************************
#  空间列表-浏览企业空间-菜单栏-产品-返回
    def Kjlb_browseorgspace_menu_product_back(self):
        self.Kjlb_browseorgspace_menu_product_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-产品-返回")
        return self.Kjlb_browseorgspace_menu_product_backP

    #  空间列表-浏览企业空间-菜单栏-产品-新建
    def Kjlb_browseorgspace_menu_product_new(self):
        self.Kjlb_browseorgspace_menu_product_newP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-产品-新建")
        return self.Kjlb_browseorgspace_menu_product_newP

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表
    def Kjlb_browseorgspace_menu_product_unlock_list(self):
        self.Kjlb_browseorgspace_menu_product_unlock_list = self.p.get_elements("id->com.yunlu6.stone:id/tv_productr_name","空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表")
        return self.Kjlb_browseorgspace_menu_product_unlock_list

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找
    def Kjlb_browseorgspace_menu_product_unlock_list_byname(self,name):
        self.Kjlb_browseorgspace_menu_product_unlock_list_bynameP = self.p.get_elements("name->%s"%name,"空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找")
        return self.Kjlb_browseorgspace_menu_product_unlock_list_bynameP

    #  空间列表-浏览企业空间-菜单栏-产品-未发布
    def Kjlb_browseorgspace_menu_product_unlock(self):
        self.Kjlb_browseorgspace_menu_product_unlockP = self.p.get_element("id->com.yunlu6.stone:id/tv_unlock", "空间列表-浏览企业空间-菜单栏-产品-未发布")
        return self.Kjlb_browseorgspace_menu_product_unlockP

     #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品名查找
    def Kjlb_browseorgspace_menu_product_lock_list_byname(self,name):
        self.Kjlb_browseorgspace_menu_product_lock_list_bynameP = self.p.get_elements("name->%s"%name,"空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品名查找")
        return self.Kjlb_browseorgspace_menu_product_lock_list_bynameP

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表
    def Kjlb_browseorgspace_menu_product_lock_list(self):
        self.Kjlb_browseorgspace_menu_product_lock_listP = self.p.get_element("id->com.yunlu6.stone:id/iv_productr","空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表")
        return self.Kjlb_browseorgspace_menu_product_lock_listP

    #  空间列表-浏览企业空间-菜单栏-产品-已发布
    def Kjlb_browseorgspace_menu_product_lock(self):
        self.Kjlb_browseorgspace_menu_product_lockP = self.p.get_element("id->com.yunlu6.stone:id/tv_lock","空间列表-浏览企业空间-菜单栏-产品-已发布")
        return self.Kjlb_browseorgspace_menu_product_lockP

     # 空间列表-浏览企业空间-菜单栏-产品-收款账号
    def Kjlb_browseorgspace_menu_product_account(self):
        self.Kjlb_browseorgspace_menu_product_accountP = self.p.get_element("name->%s"%"为保障交易安全顺畅，需验证贵司收款银行账户","空间列表-浏览企业空间-菜单栏-产品-收款账号")
        return self.Kjlb_browseorgspace_menu_product_accountP

    # 空间列表-浏览企业空间-菜单栏-产品-搜索
    def Kjlb_browseorgspace_menu_product_seek(self):
        self.Kjlb_browseorgspace_menu_product_seekP = self.p.get_element("id->com.yunlu6.stone:id/et_seek","空间列表-浏览企业空间-菜单栏-产品-搜索")
        return self.Kjlb_browseorgspace_menu_product_seekP

#***************************************【PAGE2】团队Kjlb_browseorgspace_menu_team***************************************
# 空间列表-浏览企业空间-菜单栏-团队-返回
    def Kjlb_browseorgspace_menu_team_back(self):
        self.Kjlb_browseorgspace_menu_team_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览企业空间-菜单栏-团队-返回")
        return self.Kjlb_browseorgspace_menu_team_back

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏
    def Kjlb_browseorgspace_menu_team_menu(self):
        self.Kjlb_browseorgspace_menu_team_menuT = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览企业空间-菜单栏-团队-菜单栏")
        return self.Kjlb_browseorgspace_menu_team_menuT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免
    def Kjlb_browseorgspace_menu_team_menu_assignjob(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjobT = self.p.get_element("id->com.yunlu6.stone:id/pop_teamedit_personnel","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjobT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门
    def Kjlb_browseorgspace_menu_team_menu_mydepartment(self):
        self.Kjlb_browseorgspace_menu_team_menu_mydepartmentT = self.p.get_element("id->com.yunlu6.stone:id/pop_teamedit_mydepartment","空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门")
        return self.Kjlb_browseorgspace_menu_team_menu_mydepartmentT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-返回
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_back(self):
        self.Kjlb_browseorgspace_menu_team_menu_mydepartment_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back","空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-返回")
        return self.Kjlb_browseorgspace_menu_team_menu_mydepartment_back

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-搜索
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_seek(self):
        self.Kjlb_browseorgspace_menu_team_menu_mydepartment_seek = self.p.get_element("id->com.yunlu6.stone:id/et_seek","空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-搜索")
        return self.Kjlb_browseorgspace_menu_team_menu_mydepartment_seek

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑
    def Kjlb_browseorgspace_menu_team_teamedit(self):
        self.Kjlb_browseorgspace_menu_team_teameditT = self.p.get_element("id->com.yunlu6.stone:id/companyteam_btn_edit","空间列表-浏览企业空间-菜单栏-团队-团队编辑")
        return self.Kjlb_browseorgspace_menu_team_teameditT

     # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮列表
    def Kjlb_browseorgspace_menu_team_teamedit_numeidtL(self):
        self.Kjlb_browseorgspace_menu_team_teamedit_numeidtT = self.p.get_elements("id->com.yunlu6.stone:id/companyteam_item_edit","空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数按钮列表")
        return self.Kjlb_browseorgspace_menu_team_teamedit_numeidtT

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit(self):
        self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumeditT = self.p.get_element("id->com.yunlu6.stone:id/teamedit_jobs_editnum","空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮")
        return self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumeditT

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel(self):
        self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancelT = self.p.get_element("id->com.yunlu6.stone:id/teamedit_cancleedit","空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮-否")
        return self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancelT

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm(self):
        self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirmT = self.p.get_element("id->com.yunlu6.stone:id/teamedit_commitedit","空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数-职位人数按钮-是")
        return self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirmT

#***************************************【PAGE2】资讯Kjlb_browseorgspace_menu_archivies***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-返回
    def Kjlb_browseorgspace_menu_archivies_back(self):
        self.Kjlb_browseorgspace_menu_archivies_back = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-资讯-返回")
        return self.Kjlb_browseorgspace_menu_archivies_back

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮
    def Kjlb_browseorgspace_menu_archivies_new(self):
        self.Kjlb_browseorgspace_menu_archivies_new = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-资讯-新增按钮")
        return self.Kjlb_browseorgspace_menu_archivies_new

    # 空间列表-浏览企业空间-菜单栏-资讯-图片新增
    def Kjlb_browseorgspace_menu_archivies_picadd(self):
        self.Kjlb_browseorgspace_menu_archivies_picaddA = self.p.get_element("id->com.yunlu6.stone:id/rl_add","空间列表-浏览企业空间-菜单栏-资讯-图片新增")
        return self.Kjlb_browseorgspace_menu_archivies_picaddA

     # 空间列表-浏览企业空间-菜单栏-资讯-图片列表
    def Kjlb_browseorgspace_menu_archivies_pic(self):
        self.Kjlb_browseorgspace_menu_archivies_picA = self.p.get_elements("id->com.yunlu6.stone:id/iv_profile","空间列表-浏览企业空间-菜单栏-资讯-图片列表")
        return self.Kjlb_browseorgspace_menu_archivies_picA

     # 空间列表-浏览企业空间-菜单栏-资讯-图片-标题
    def Kjlb_browseorgspace_menu_archivies_pic_title(self):
        self.Kjlb_browseorgspace_menu_archivies_pic_titleT = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_title","空间列表-浏览企业空间-菜单栏-资讯-图片-标题")
        return self.Kjlb_browseorgspace_menu_archivies_pic_titleT

    # 空间列表-浏览企业空间-菜单栏-资讯-图片-类型
    def Kjlb_browseorgspace_menu_archivies_pic_type(self):
        self.Kjlb_browseorgspace_menu_archivies_pic_typeT = self.p.get_element("id->com.yunlu6.stone:id/tv_profile","空间列表-浏览企业空间-菜单栏-资讯-图片-类型")
        return self.Kjlb_browseorgspace_menu_archivies_pic_typeT

#***************************************【PAGE2】企业名片Kjlb_browseorgspace_menu_bcard***************************************
    # 空间列表-浏览企业空间-菜单栏-企业名片-返回
    def Kjlb_browseorgspace_menu_bcard_back(self):
        self.Kjlb_browseorgspace_menu_bcard_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back","空间列表-浏览企业空间-菜单栏-企业名片-返回")
        return self.Kjlb_browseorgspace_menu_bcard_back

     # 空间列表-浏览企业空间-菜单栏-企业名片-企业资信
    def Kjlb_browseorgspace_menu_bcard_credit(self):
        self.Kjlb_browseorgspace_menu_bcard_credit = self.p.get_element("id->com.yunlu6.stone:id/companycard_level","空间列表-浏览企业空间-菜单栏-企业名片-企业资信")
        return self.Kjlb_browseorgspace_menu_bcard_credit

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏
    def Kjlb_browseorgspace_menu_bcard_menu(self):
        self.Kjlb_browseorgspace_menu_bcard_menuB = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏")
        return self.Kjlb_browseorgspace_menu_bcard_menuB

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队
    def Kjlb_browseorgspace_menu_bcard_menu_quitteam(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_quitteam = self.p.get_element("id->com.yunlu6.stone:id/bt_teamquit","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队")
        return self.Kjlb_browseorgspace_menu_bcard_menu_quitteam

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-否
    def Kjlb_browseorgspace_menu_bcard_menu_quitteam_cancel(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_cancell = self.p.get_element("id->com.yunlu6.stone:id/bt_cancel","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-否")
        return self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_cancell

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-是
    def Kjlb_browseorgspace_menu_bcard_menu_quitteam_confirm(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_confirm = self.p.get_element("id->com.yunlu6.stone:id/bt_affirm","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-是")
        return self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_confirm

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-附近商家
    def Kjlb_browseorgspace_menu_bcard_menu_nearby(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_nearby = self.p.get_element("id->com.yunlu6.stone:id/bt_nearby","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-附近商家")
        return self.Kjlb_browseorgspace_menu_bcard_menu_nearby

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑
    def Kjlb_browseorgspace_menu_bcard_menu_edit(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_editB = self.p.get_element("id->com.yunlu6.stone:id/bt_edit","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑")
        return self.Kjlb_browseorgspace_menu_bcard_menu_editB

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-设置
    def Kjlb_browseorgspace_menu_bcard_menu_setting(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_setting = self.p.get_element("id->com.yunlu6.stone:id/bt_setup","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-设置")
        return self.Kjlb_browseorgspace_menu_bcard_menu_setting

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-关闭
    def Kjlb_browseorgspace_menu_bcard_menu_close(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_close = self.p.get_element("id->com.yunlu6.stone:id/bt_close","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-关闭")
        return self.Kjlb_browseorgspace_menu_bcard_menu_close

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享
    def Kjlb_browseorgspace_menu_bcard_menu_share(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_share = self.p.get_element("id->com.yunlu6.stone:id/bt_share","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享")
        return self.Kjlb_browseorgspace_menu_bcard_menu_share

    # 空间列表-浏览企业空间-菜单栏-企业名片-联系方式列表
    def Kjlb_browseorgspace_menu_bcard_contactlist(self):
        self.Kjlb_browseorgspace_menu_bcard_contactB = self.p.get_elements("id->com.yunlu6.stone:id/contact_icon","空间列表-浏览企业空间-菜单栏-企业名片-联系方式列表")
        return self.Kjlb_browseorgspace_menu_bcard_contactB

    # 空间列表-浏览企业空间-菜单栏-企业名片-资讯
    def Kjlb_browseorgspace_menu_bcard_archivies(self):
        self.Kjlb_browseorgspace_menu_bcard_archivies = self.p.get_element("id->com.yunlu6.stone:id/btn_archivie","空间列表-浏览企业空间-菜单栏-企业名片-资讯")
        return self.Kjlb_browseorgspace_menu_bcard_archivies

    # 空间列表-浏览企业空间-菜单栏-企业名片-点击创建产品
    def Kjlb_browseorgspace_menu_bcard_newpro(self):
        self.Kjlb_browseorgspace_menu_bcard_newpro = self.p.get_element("id->com.yunlu6.stone:id/iv_crad_build_prod","空间列表-浏览企业空间-菜单栏-企业名片-点击创建产品")
        return self.Kjlb_browseorgspace_menu_bcard_newpro

#***************************************【PAGE2】访客Kjlb_browseorgspace_menu_visitor***************************************
 # 空间列表-浏览企业空间-菜单栏-访客-访客列表
    def Kjlb_browseorgspace_menu_visitor_list(self):
        self.Kjlb_browseorgspace_menu_visitor_list = self.p.get_element("id->com.yunlu6.stone:id/visitor_name","空间列表-浏览企业空间-菜单栏-访客-访客列表")
        return self.Kjlb_browseorgspace_menu_visitor_list

    # 空间列表-浏览企业空间-菜单栏-访客-访客列表-返回
    def Kjlb_browseorgspace_menu_visitor_list_back(self):
        self.Kjlb_browseorgspace_menu_visitor_list_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back","空间列表-浏览企业空间-菜单栏-访客-访客列表")
        return self.Kjlb_browseorgspace_menu_visitor_list_back

#***************************************【PAGE2】客户Kjlb_browseorgspace_menu_customer***************************************
    # 空间列表-浏览企业空间-菜单栏-客户-返回
    def Kjlb_browseorgspace_menu_customer_back(self):
        self.Kjlb_browseorgspace_menu_customer_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览企业空间-菜单栏-客户-返回")
        return self.Kjlb_browseorgspace_menu_customer_back

    # 空间列表-浏览企业空间-菜单栏-客户-搜索框
    def Kjlb_browseorgspace_menu_customer_search(self):
        self.Kjlb_browseorgspace_menu_customer_search = self.p.get_element("id->com.yunlu6.stone:id/et_search","空间列表-浏览企业空间-菜单栏-客户-搜索框")
        return self.Kjlb_browseorgspace_menu_customer_search

    # 空间列表-浏览企业空间-菜单栏-客户-搜索
    def Kjlb_browseorgspace_menu_customer_seek(self):
        self.Kjlb_browseorgspace_menu_customer_seek = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览企业空间-菜单栏-客户-搜索")
        return self.Kjlb_browseorgspace_menu_customer_seek

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏
    def Kjlb_browseorgspace_menu_customer_menu(self):
        self.Kjlb_browseorgspace_menu_customer_menu = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览企业空间-菜单栏-客户-菜单栏")
        return self.Kjlb_browseorgspace_menu_customer_menu

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表
    def Kjlb_browseorgspace_menu_customer_list(self):
        self.Kjlb_browseorgspace_menu_customer_clist = self.p.get_elements("id->com.yunlu6.stone:id/rl_out","空间列表-浏览企业空间-菜单栏-客户-客户列表")
        return self.Kjlb_browseorgspace_menu_customer_clist

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户
    def Kjlb_browseorgspace_menu_customer_menu_add(self):
        self.Kjlb_browseorgspace_menu_customer_menu_add = self.p.get_element("id->com.yunlu6.stone:id/btn_new_space","空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户")
        return self.Kjlb_browseorgspace_menu_customer_menu_add

     # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作
    def Kjlb_browseorgspace_menu_customer_menu_batch(self):
        self.Kjlb_browseorgspace_menu_customer_menu_batch = self.p.get_elements("id->com.yunlu6.stone:id/btn_share_space","空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作")
        return self.Kjlb_browseorgspace_menu_customer_menu_batch

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-返回
    def Kjlb_browseorgspace_menu_customer_menu_batch_back(self):
        self.Kjlb_browseorgspace_menu_customer_menu_batch_back = self.p.get_elements("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-返回")
        return self.Kjlb_browseorgspace_menu_customer_menu_batch_back

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选
    def Kjlb_browseorgspace_menu_customer_menu_batch_all(self):
        self.Kjlb_browseorgspace_menu_customer_menu_batch_all = self.p.get_elements("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选")
        return self.Kjlb_browseorgspace_menu_customer_menu_batch_all

     # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-圆圈勾选
    def Kjlb_browseorgspace_menu_customer_menu_batch_choose(self):
        self.Kjlb_browseorgspace_menu_customer_menu_batch_choose = self.p.get_elements("id->com.yunlu6.stone:id/iv_select","空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选")
        return self.Kjlb_browseorgspace_menu_customer_menu_batch_choose

#***************************************【PAGE2】业务升级Kjlb_browseorgspace_menu_upgrade***************************************
     # 空间列表-浏览企业空间-菜单栏-业务升级-开启
    def Kjlb_browseorgspace_menu_upgrade_open(self):
        self.Kjlb_browseorgspace_menu_upgrade_open = self.p.get_elements("id->com.yunlu6.stone:id/upgrade_open","空间列表-浏览企业空间-菜单栏-业务升级-开启")
        return self.Kjlb_browseorgspace_menu_upgrade_open

    # 空间列表-浏览企业空间-菜单栏-业务升级-返回
    def Kjlb_browseorgspace_menu_upgrade_back(self):
        self.Kjlb_browseorgspace_menu_upgrade_back = self.p.get_element("id->com.yunlu6.stone:id/companyupgrade_backe","空间列表-浏览企业空间-菜单栏-业务升级-返回")
        return self.Kjlb_browseorgspace_menu_upgrade_back

#***************************************【PAGE2】照片列表(包括点击照片加数据)Kjlb_browseperspace_piclist***************************************
    # 空间列表-浏览私人空间-照片列表-菜单栏
    def Kjlb_browseperspace_piclist_menu(self):
        self.Kjlb_browseperspace_piclist_menuP = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览私人空间-照片列表-菜单栏")
        return self.Kjlb_browseperspace_piclist_menuP

    # 空间列表-浏览私人空间-照片列表-分类到
    def Kjlb_browseperspace_piclist_classify(self):
        self.Kjlb_browseperspace_piclist_classifyP = self.p.get_element("id->com.yunlu6.stone:id/btn_new_space","空间列表-浏览私人空间-照片列表-分类到")
        return self.Kjlb_browseperspace_piclist_classifyP

    # 空间列表-浏览私人空间-照片列表-编辑
    def Kjlb_browseperspace_piclist_edit(self):
        self.Kjlb_browseperspace_piclist_editP = self.p.get_element("id->com.yunlu6.stone:id/btn_share_space","空间列表-浏览私人空间-照片列表-编辑")
        return self.Kjlb_browseperspace_piclist_editP

    # 空间列表-浏览私人空间-照片列表-返回
    def Kjlb_browseperspace_piclist_back(self):
        self.Kjlb_browseperspace_piclist_backP = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览私人空间-照片列表-返回")
        return self.Kjlb_browseperspace_piclist_backP

    #空间列表-浏览私人空间-照片列表-照片本身
    def Kjlb_browseperspace_piclist_itself(self):
        self.Kjlb_browseperspace_piclist_itselfP = self.p.get_element("id->com.yunlu6.stone:id/image","空间列表-浏览私人空间-照片列表-照片本身")
        return self.Kjlb_browseperspace_piclist_itselfP

    # 空间列表-浏览私人空间-文件夹名称列表
    def Kjlb_browseperspace_foldername(self):
        self.Kjlb_browseperspace_foldernameP = self.p.get_elements("id->com.yunlu6.stone:id/personzone_item_foldername","空间列表-浏览私人空间-文件夹名称列表")
        return self.Kjlb_browseperspace_foldernameP

    # 空间列表-浏览私人空间-加数据-相册
    def Kjlb_browseperspace_addData_ByAlbum(self):
        self.Kjlb_browseperspace_addData_ByAlbumP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_album","空间列表-浏览私人空间--加数据-相册")
        return self.Kjlb_browseperspace_addData_ByAlbumP

#***************************************【PAGE2】菜单栏-名片Kjlb_browseperspace_menu_card***************************************
    # 空间列表-浏览私人空间-菜单栏-名片-返回
    def Kjlb_browseperspace_menu_card_back(self):
        self.Kjlb_browseperspace_menu_card_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_edit_icon","空间列表-浏览私人空间-菜单栏-名片-返回")
        return self.Kjlb_browseperspace_menu_card_backP

    # 空间列表-浏览私人空间-菜单栏-名片-分享
    def Kjlb_browseperspace_menu_card_share(self):
        self.Kjlb_browseperspace_menu_card_shareP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_edit_menu_tv","空间列表-浏览私人空间-菜单栏-名片-分享")
        return self.Kjlb_browseperspace_menu_card_shareP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信
    def Kjlb_browseperspace_menu_card_share_wechat(self):
        self.Kjlb_browseperspace_menu_card_share_wechatP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_album","空间列表-浏览私人空间-菜单栏-名片-分享-微信")
        return self.Kjlb_browseperspace_menu_card_share_wechatP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信朋友圈
    def Kjlb_browseperspace_menu_card_share_circle(self):
        self.Kjlb_browseperspace_menu_card_share_circleP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_take_pictures","空间列表-浏览私人空间-菜单栏-名片-分享-微信朋友圈")
        return self.Kjlb_browseperspace_menu_card_share_circleP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ空间
    def Kjlb_browseperspace_menu_card_share_qqzone(self):
        self.Kjlb_browseperspace_menu_card_share_qqzoneP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_wifi_sync","空间列表-浏览私人空间-菜单栏-名片-分享-QQ空间")
        return self.Kjlb_browseperspace_menu_card_share_qqzoneP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ
    def Kjlb_browseperspace_menu_card_share_qq(self):
        self.Kjlb_browseperspace_menu_card_share_qqP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_qq","空间列表-浏览私人空间-菜单栏-名片-分享-QQ")
        return self.Kjlb_browseperspace_menu_card_share_qqP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-新浪微博
    def Kjlb_browseperspace_menu_card_share_sina(self):
        self.Kjlb_browseperspace_menu_card_share_sinaP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_weibo","空间列表-浏览私人空间-菜单栏-名片-分享-微博")
        return self.Kjlb_browseperspace_menu_card_share_sinaP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-取消
    def Kjlb_browseperspace_menu_card_share_cancel(self):
        self.Kjlb_browseperspace_menu_card_share_cancelP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_cancel","空间列表-浏览私人空间-菜单栏-名片-分享-取消")
        return self.Kjlb_browseperspace_menu_card_share_cancelP

    # 空间列表-浏览私人空间-菜单栏-名片-手机
    def Kjlb_browseperspace_menu_card_phone(self):
        self.Kjlb_browseperspace_menu_card_phoneP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_phone_cb","空间列表-浏览私人空间-菜单栏-名片-手机")
        return self.Kjlb_browseperspace_menu_card_phoneP

    # 空间列表-浏览私人空间-菜单栏-名片-邮箱
    def Kjlb_browseperspace_menu_card_email(self):
        self.Kjlb_browseperspace_menu_card_emailP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_email_cb","空间列表-浏览私人空间-菜单栏-名片-邮箱")
        return self.Kjlb_browseperspace_menu_card_emailP

    # 空间列表-浏览私人空间-菜单栏-名片-地址
    def Kjlb_browseperspace_menu_card_address(self):
        self.Kjlb_browseperspace_menu_card_addressP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_address_cb","空间列表-浏览私人空间-菜单栏-名片-地址")
        return self.Kjlb_browseperspace_menu_card_addressP

    # 空间列表-浏览私人空间-菜单栏-名片-QQ
    def Kjlb_browseperspace_menu_card_QQ(self):
        self.Kjlb_browseperspace_menu_card_QQP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_qq_cb","空间列表-浏览私人空间-菜单栏-名片-QQ")
        return self.Kjlb_browseperspace_menu_card_QQP

    # 空间列表-浏览私人空间-菜单栏-名片-有效期
    def Kjlb_browseperspace_menu_card_limit(self):
        self.Kjlb_browseperspace_menu_card_limitP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_userlife_tv","空间列表-浏览私人空间-菜单栏-名片-有效期")
        return self.Kjlb_browseperspace_menu_card_limitP

    # 空间列表-浏览私人空间-菜单栏-编辑-删除文件夹列表
    def Kjlb_browseperspace_menu_edit_deletefolder(self):
        self.Kjlb_browseperspace_menu_edit_deletefolderP = self.p.get_elements("id->com.yunlu6.stone:id/editlayout_folder_dele","空间列表-浏览私人空间-菜单栏-编辑-删除文件夹名称")
        return self.Kjlb_browseperspace_menu_edit_deletefolderP

     # 空间列表-浏览私人空间-菜单栏-编辑-修改文件夹图标
    def Kjlb_browseperspace_menu_edit_editfolder(self):
        self.Kjlb_browseperspace_menu_edit_editfolderP = self.p.get_elements("id->com.yunlu6.stone:id/editlayout_folder_edite","空间列表-浏览私人空间-菜单栏-编辑-修改文件夹名称")
        return self.Kjlb_browseperspace_menu_edit_editfolderP

    # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称
    def Kjlb_browseperspace_menu_edit_editfolder_fname(self):
        self.Kjlb_browseperspace_menu_edit_editfolder_fnameP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_name","空间列表-浏览私人空间-菜单栏-编辑-修改文件夹名称-名称列表")
        return self.Kjlb_browseperspace_menu_edit_editfolder_fnameP

     # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-是
    def Kjlb_browseperspace_menu_edit_editfolder_fname_OK(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEditOKP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_ok","空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-是")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEditOKP

    # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-否
    def Kjlb_browseperspace_menu_edit_editfolder_fname_NO(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NOP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_no","空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-否")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NOP

    # 空间列表-浏览私人空间-菜单栏-编辑-+数据
    def Kjlb_browseperspace_menu_edit_adddata(self):
        self.Kjlb_browseperspace_menu_edit_adddataP = self.p.get_elements("name->＋ 数据","空间列表-浏览私人空间-菜单栏-编辑-+数据")
        return self.Kjlb_browseperspace_menu_edit_adddataP

     # 空间列表-浏览私人空间-菜单栏-编辑-空间类型
    def Kjlb_browseperspace_menu_edit_spacetype(self):
        self.Kjlb_browseperspace_menu_edit_spacetypeP = self.p.get_element("id->com.yunlu6.stone:id/create_img_type","空间列表-浏览私人空间-菜单栏-编辑-空间类型")
        return self.Kjlb_browseperspace_menu_edit_spacetypeP

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间
    def Kjlb_browseperspace_menu_edit_deletespace(self):
        self.Kjlb_browseperspace_menu_edit_deletespaceP = self.p.get_element("id->com.yunlu6.stone:id/space_dele_icon","空间列表-浏览私人空间-菜单栏-编辑-删除空间")
        return self.Kjlb_browseperspace_menu_edit_deletespaceP

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-是
    def Kjlb_browseperspace_menu_edit_deletespace_OK(self):
        self.Kjlb_browseperspace_menu_edit_deletespace_OKP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_ok","空间列表-浏览私人空间-菜单栏-编辑-删除空间-是")
        return self.Kjlb_browseperspace_menu_edit_deletespace_OKP

     # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-否
    def Kjlb_browseperspace_menu_edit_deletespace_NO(self):
        self.Kjlb_browseperspace_menu_edit_deletespace_NOP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_no","空间列表-浏览私人空间-菜单栏-编辑-删除空间-否")
        return self.Kjlb_browseperspace_menu_edit_deletespaceP


     # 空间列表-浏览私人空间-菜单栏-编辑-返回
    def Kjlb_browseperspace_menu_edit_back(self):
        self.Kjlb_browseperspace_menu_edit_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览私人空间-菜单栏-编辑-返回")
        return self.Kjlb_browseperspace_menu_edit_backP

     # 空间列表-浏览私人空间-菜单栏-编辑-空间名
    def Kjlb_browseperspace_menu_edit_spacename(self):
        self.Kjlb_browseperspace_menu_edit_spacenameP = self.p.get_element("id->com.yunlu6.stone:id/space_name_edit","空间列表-浏览私人空间-菜单栏-编辑-空间名")
        return self.Kjlb_browseperspace_menu_edit_spacenameP

     # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称列表(0)
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEditP = self.p.get_elements("id->com.yunlu6.stone:id/edit_folder_name","空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEditP

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-是
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_OK(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEditOKP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_ok","空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-是")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEditOKP

     # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-否
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NO(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NOP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_no","空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-否")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NOP

#***************************************【PAGE2】菜单栏-客户Kjlb_browseperspace_menu_customer***************************************
    # 空间列表-浏览私人空间-菜单栏-客户-返回
    def Kjlb_browseperspace_menu_customer_back(self):
        self.Kjlb_browseperspace_menu_customer_backP = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览私人空间-菜单栏-客户-返回")
        return self.Kjlb_browseperspace_menu_customer_backP

    # 空间列表-浏览私人空间-菜单栏-客户-搜索栏
    def Kjlb_browseperspace_menu_customer_search(self):
        self.Kjlb_browseperspace_menu_customer_searchP = self.p.get_element("id->com.yunlu6.stone:id/et_search","空间列表-浏览私人空间-菜单栏-客户-搜索栏")
        return self.Kjlb_browseperspace_menu_customer_searchP

    # 空间列表-浏览私人空间-菜单栏-客户-搜索按钮
    def Kjlb_browseperspace_menu_customer_searchbtn(self):
        self.Kjlb_browseperspace_menu_customer_searchbtnP = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览私人空间-菜单栏-客户-搜索栏")
        return self.Kjlb_browseperspace_menu_customer_searchbtnP

    # 空间列表-浏览私人空间-菜单栏-客户-菜单
    def Kjlb_browseperspace_menu_customer_menu(self):
        self.Kjlb_browseperspace_menu_customer_menuP = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览私人空间-菜单栏-客户-菜单")
        return self.Kjlb_browseperspace_menu_customer_menuP

    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户
    def Kjlb_browseperspace_menu_customer_menu_addcus(self):
        self.Kjlb_browseperspace_menu_customer_menu_addcusP = self.p.get_element("id->com.yunlu6.stone:id/btn_new_space","空间列表-浏览私人空间-菜单栏-客户-菜单-+客户")
        return self.Kjlb_browseperspace_menu_customer_menu_addcusP

    # 空间列表-浏览私人空间-菜单栏-客户-客户列表
    def Kjlb_browseperspace_menu_customer_clist(self):
        self.Kjlb_browseperspace_menu_customer_clistP = self.p.get_elements("id->com.yunlu6.stone:id/rl_out","空间列表-浏览私人空间-菜单栏-客户-客户列表")
        return self.Kjlb_browseperspace_menu_customer_clistP

    # 空间列表-浏览私人空间-菜单栏-客户-群聊
    def Kjlb_browseperspace_menu_customer_gchat(self):
        self.Kjlb_browseperspace_menu_customer_gchatP = self.p.get_element("id->com.yunlu6.stone:id/rl_bottom","空间列表-浏览私人空间-菜单栏-客户-群聊")
        return self.Kjlb_browseperspace_menu_customer_gchatP

    # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称-确定
    def Kjlb_browseperspace_menu_addfolder_confirm(self):
        self.Kjlb_browseperspace_menu_addfolder_confirmP = self.p.get_element("id->com.yunlu6.stone:id/zone_add_commit","空间列表-浏览私人空间-菜单栏-+文件夹-确定")
        return self.Kjlb_browseperspace_menu_addfolder_confirmP

     # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称
    def Kjlb_browseperspace_menu_addfolder_foldername(self):
        self.Kjlb_browseperspace_menu_addfolder_foldernameP = self.p.get_element("id->com.yunlu6.stone:id/zone_add_gallery_et","空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称")
        return self.Kjlb_browseperspace_menu_addfolder_foldernameP

    # 空间列表-浏览私人空间-菜单栏-+文件夹-返回
    def Kjlb_browseperspace_menu_addfolder_back(self):
        self.Kjlb_browseperspace_menu_addfolder_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览私人空间-菜单栏-+文件夹-返回")
        return self.Kjlb_browseperspace_menu_addfolder_backP

#***************************************【PAGE2】+数据Kjlb_browseperspace_adata***************************************
    # 空间列表-浏览私人空间-加数据-相册
    def Kjlb_browseperspace_adata_ByAlbum(self):
        self.Kjlb_browseperspace_adata_ByAlbumP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_album","空间列表-浏览私人空间-加数据-相册")
        return self.Kjlb_browseperspace_adata_ByAlbumP

    # 空间列表-浏览私人空间-加数据-拍照
    def Kjlb_browseperspace_adata_ByTakepic(self):
        self.Kjlb_browseperspace_adata_ByTakepicP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_take_pictures","空间列表-浏览私人空间-加数据-拍照")
        return self.Kjlb_browseperspace_adata_ByTakepicP

    # 空间列表-浏览私人空间-加数据-取消
    def Kjlb_browseperspace_adata_cancel(self):
        self.Kjlb_browseperspace_adata_cancelP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_cancel","空间列表-浏览私人空间-加数据-取消")
        return self.Kjlb_browseperspace_adata_cancelP

#***************************************【PAGE2】更多Kjlb_browseperspace_more***************************************
     # 空间列表-浏览私人空间-更多-照片列表
    def Kjlb_browseperspace_more_piclist(self):
        self.Kjlb_browseperspace_more_piclistP = self.p.get_elements("id->com.yunlu6.stone:id/presonzone_gridview_iv","空间列表-浏览私人空间-更多-照片列表")
        return self.Kjlb_browseperspace_more_piclistP

    # 空间列表-浏览私人空间-更多-返回
    def Kjlb_browseperspace_more_back(self):
        self.Kjlb_browseperspace_more_backP = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览私人空间-更多-照片列表-照片本身")
        return self.Kjlb_browseperspace_more_backP

    # 空间列表-浏览私人空间-更多-菜单栏
    def Kjlb_browseperspace_more_menu(self):
        self.Kjlb_browseperspace_more_menuP = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览私人空间-更多-菜单栏")
        return self.Kjlb_browseperspace_more_menuP

    # 空间列表-浏览私人空间-更多-菜单栏-上传
    def Kjlb_browseperspace_more_menu_upload(self):
        self.Kjlb_browseperspace_more_menu_uploadP = self.p.get_element("id->com.yunlu6.stone:id/pop_gallery_photoes_btn_uploade","空间列表-浏览私人空间-更多-菜单栏-上传")
        return self.Kjlb_browseperspace_more_menu_uploadP

    # 空间列表-浏览私人空间-更多-菜单栏-上传-相册
    def Kjlb_browseperspace_more_menu_upload_ByAlbum(self):
        self.Kjlb_browseperspace_more_menu_upload_ByAlbumP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_album","空间列表-浏览私人空间-更多-菜单栏-上传-相册")
        return self.Kjlb_browseperspace_more_menu_upload_ByAlbumP

    # 空间列表-浏览私人空间-更多-菜单栏-上传-拍照
    def Kjlb_browseperspace_more_menu_upload_ByTakepic(self):
        self.Kjlb_browseperspace_more_menu_upload_ByTakepicP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_take_pictures","空间列表-浏览私人空间-更多-菜单栏-上传-拍照")
        return self.Kjlb_browseperspace_more_menu_upload_ByTakepicP

    # 空间列表-浏览私人空间-更多-菜单栏-上传-取消
    def Kjlb_browseperspace_more_menu_upload_cancel(self):
        self.Kjlb_browseperspace_more_menu_upload_cancelP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_cancel","空间列表-浏览私人空间-更多-菜单栏-上传-取消")
        return self.Kjlb_browseperspace_more_menu_upload_cancelP

     # 空间列表-浏览私人空间-更多-菜单栏-编辑
    def Kjlb_browseperspace_more_menu_edit(self):
        self.Kjlb_browseperspace_more_menu_editP = self.p.get_element("id->com.yunlu6.stone:id/pop_gallery_photoes_btn_edit","空间列表-浏览私人空间-更多-菜单栏-编辑")
        return self.Kjlb_browseperspace_more_menu_editP

    # 空间列表-浏览私人空间-更多-菜单栏-排序
    def Kjlb_browseperspace_more_menu_sort(self):
        self.Kjlb_browseperspace_more_menu_sortP = self.p.get_element("id->com.yunlu6.stone:id/pop_gallery_photoes_btn_sort","空间列表-浏览私人空间-更多-菜单栏-排序")
        return self.Kjlb_browseperspace_more_menu_sortP