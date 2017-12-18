__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.RENMAIPAGE1 import _RENMAIPAGE1

class _RENMAIPAGE2(_RENMAIPAGE1):
#*********************************【PAGE1】+同步通讯录：RMSY_syscontacts*********************************
    #定位：人脉首页-同步通讯录-返回
    def RMSY_syncContacts_back(self):
        self.RMSY_syscontacts_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-同步通讯录-返回")
        return self.RMSY_syscontacts_back

    #定位：人脉首页-同步通讯录-立即同步
    def RMSY_syncContacts_confirm(self):
        self.RMSY_syncContacts_confirm = self.p.get_element("id->com.yunlu6.stone:id/btn_synchro", "人脉首页-同步通讯录-立即同步")
        return self.RMSY_syncContacts_confirm

#*********************************【PAGE1】+主菜单++人脉：RMSY_menu_add*********************************
    #定位：人脉首页-主菜单-+人脉-返回
    def RMSY_menu_add_back(self):
        self.RMSY_menu_add_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-主菜单-+人脉-返回")
        return self.RMSY_menu_add_back

    #定位：人脉首页-主菜单-+人脉-清空
    def RMSY_menu_add_clear(self):
        self.RMSY_menu_add_clear = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv", "人脉首页-主菜单-+人脉-清空")
        return self.RMSY_menu_add_clear

    #定位：人脉首页-主菜单-+人脉-输入姓名
    def RMSY_menu_add_nameinput(self):
        self.RMSY_menu_add_nameinput = self.p.get_element("id->com.yunlu6.stone:id/contact_name", "人脉首页-主菜单-+人脉-输入姓名")
        return self.RMSY_menu_add_nameinput

    #定位：人脉首页-主菜单-+人脉-输入手机号
    def RMSY_menu_add_telinput(self):
        self.RMSY_menu_add_telinput = self.p.get_element("id->com.yunlu6.stone:id/contact_mobile", "人脉首页-主菜单-+人脉-输入手机号")
        return self.RMSY_menu_add_telinput

    #定位：人脉首页-主菜单-+人脉-同步手机通讯录
    def RMSY_menu_add_syscontacts(self):
        self.RMSY_menu_add_syscontacts = self.p.get_element("id->com.yunlu6.stone:id/btn_top", "人脉首页-主菜单-+人脉-同步手机通讯录")
        return self.RMSY_menu_add_syscontacts

    #定位：人脉首页-主菜单-+人脉-名片夹选择加入
    def RMSY_menu_add_addbycard(self):
        self.RMSY_menu_add_addbycard = self.p.get_element("id->com.yunlu6.stone:id/btn_card_add", "人脉首页-主菜单-+人脉-名片夹选择加入")
        return self.RMSY_menu_add_addbycard

    #定位：人脉首页-主菜单-+人脉-添加
    def RMSY_menu_add_add(self):
        self.RMSY_menu_add_add = self.p.get_element("id->com.yunlu6.stone:id/btn_add", "人脉首页-主菜单-+人脉-添加")
        return self.RMSY_menu_add_add

#*********************************【PAGE1】点击联系人：RMSY_clickcontacts*********************************
    #定位：人脉首页-点击联系人-返回
    def RMSY_contacts_back(self):
        self.RMSY_contacts_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-返回")
        return self.RMSY_contacts_back

    #定位：人脉首页-点击联系人-打开主菜单
    def RMSY_contacts_menu(self):
        self.RMSY_contacts_menu = self.p.get_element("id->com.yunlu6.stone:id/iv_more", "人脉首页-点击联系人-打开主菜单")
        return self.RMSY_contacts_menu

    #定位：人脉首页-点击联系人-打开主菜单-名片设置
    def RMSY_contacts_menu_cardsetting(self):
        self.RMSY_contacts_menu_cardsetting = self.p.get_element("id->com.yunlu6.stone:id/card_exchange", "人脉首页-点击联系人-打开主菜单-名片设置")
        return self.RMSY_contacts_menu_cardsetting

    #定位：人脉首页-点击联系人-打开主菜单-热度设置
    def RMSY_contacts_menu_heatsetting(self):
        self.RMSY_contacts_menu_heatsetting = self.p.get_element("id->com.yunlu6.stone:id/anti", "人脉首页-点击联系人-打开主菜单-热度设置")
        return self.RMSY_contacts_menu_heatsetting

    #定位：人脉首页-点击联系人-打开主菜单-标签
    def RMSY_contacts_menu_tag(self):
        self.RMSY_contacts_menu_tag = self.p.get_element("id->com.yunlu6.stone:id/label", "人脉首页-点击联系人-打开主菜单-标签")
        return self.RMSY_contacts_menu_tag

    #定位：人脉首页-点击联系人-打开主菜单-备忘
    def RMSY_contacts_menu_memo(self):
        self.RMSY_contacts_menu_memo = self.p.get_element("id->com.yunlu6.stone:id/memorandum", "人脉首页-点击联系人-打开主菜单-备忘")
        return self.RMSY_contacts_menu_memo

    #定位;人脉首页-点击联系人-联系方式列表
    def RMSY_contacts_contactiontype(self):
        self.RMSY_contacts_contactiontype = self.p.get_elements("id->com.yunlu6.stone:id/iv_contact", "人脉首页-点击联系人-选择联系方式")
        return self.RMSY_contacts_contactiontype

    #定位;人脉首页-点击联系人-消息按钮
    def RMSY_contacts_messagebtn(self):
        self.RMSY_contacts_messagebtn = self.p.get_element("id->com.yunlu6.stone:id/iv_to_message", "人脉首页-点击联系人-消息按钮")
        return self.RMSY_contacts_messagebtn

    #定位;人脉首页-点击联系人-消息输入框
    def RMSY_contacts_message(self):
        self.RMSY_contacts_message = self.p.get_element("id->com.yunlu6.stone:id/iv_to_message", "人脉首页-点击联系人-消息按钮")
        return self.RMSY_contacts_message

    #定位;人脉首页-点击联系人-删除
    def RMSY_Contacts_delete(self):
        self.RMSY_Contacts_delete = self.p.get_element("id->com.yunlu6.stone:id/ll_blacklist", "人脉首页-点击联系人-删除")
        return  self.RMSY_Contacts_delete

    #定位;人脉首页-点击联系人-邀请方式
    def RMSY_contacts_invatationtype(self):
        self.RMSY_contacts_invatationtype = self.p.get_elements("id->com.yunlu6.stone:id/iv_item_share", "人脉首页-点击联系人-邀请方式")
        return self.RMSY_contacts_invatationtype

#*********************************【PAGE1】+搜索输入框：RMST_searchinput*********************************
    #定位：人脉首页-搜索-返回按钮
    def RMSY_search_back(self):
        self.RMSY_search_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-搜索-返回")
        return self.RMSY_search_back

    #定位：人脉首页-搜索-搜索输入框
    def RMSY_search_searchinput(self):
        self.RMSY_search_searchinput = self.p.get_element("id->com.yunlu6.stone:id/img_btn_search", "人脉首页-搜索-搜索输入框")
        return self.RMSY_search_searchinput

    #定位：人脉首页-搜索-搜索按钮
    def RMSY_search_searchbtn(self):
        self.RMSY_search_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv", "人脉首页-搜索-搜索按钮")
        return self.RMSY_search_searchbtn

    #定位：人脉首页-搜索-标签列表
    def RMSY_search_label(self):
        self.RMSY_search_label = self.p.get_elements("id->com.yunlu6.stone:id/tag_id", "人脉首页-搜索-标签列表")
        return self.RMSY_search_label

    #定位：人脉首页-搜索-集合列表
    def RMSY_search_list(self):
        self.RMSY_search_list = self.p.get_elements("id->com.yunlu6.stone:id/iv_arrow", "人脉首页-搜索-集合列表")
        return self.RMSY_search_list