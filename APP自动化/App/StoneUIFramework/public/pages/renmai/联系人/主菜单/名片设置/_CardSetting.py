__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.主菜单._ContactsMenu import _ContactsMenu

class _CardSetting(_ContactsMenu):
    #定位：人脉首页-点击联系人-打开主菜单-名片设置
    def RMSY_contacts_menu_cardsetting(self):
        self.RMSY_contacts_menu_cardsetting = self.p.get_element("id->com.yunlu6.stone:id/card_exchange", "人脉首页-点击联系人-打开主菜单-名片设置")
        return self.RMSY_contacts_menu_cardsetting

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-返回
    def RMSY_contacts_menu_cardsetting_back(self):
        self.RMSY_contacts_menu_cardsetting = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-名片设置-返回")
        return self.RMSY_contacts_menu_cardsetting_back

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-全部屏蔽
    def RMSY_contacts_menu_cardsetting_sheildall(self):
        self.RMSY_contacts_menu_cardsetting_sheildall = self.p.get_element("id->com.yunlu6.stone:id/vsb_link", "人脉首页-点击联系人-打开主菜单-名片设置-全部屏蔽")
        return self.RMSY_contacts_menu_cardsetting_sheildall

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-姓名
    def RMSY_contacts_menu_cardsetting_name(self):
        self.RMSY_contacts_menu_cardsetting_name = self.p.get_element("id->com.yunlu6.stone:id/sb_name_bt", "人脉首页-点击联系人-打开主菜单-名片设置-姓名")
        return self.RMSY_contacts_menu_cardsetting_name

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-手机
    def RMSY_contacts_menu_cardsetting_tel(self):
        self.RMSY_contacts_menu_cardsetting_tel = self.p.get_element("id->com.yunlu6.stone:id/sb_nub_bt", "人脉首页-点击联系人-打开主菜单-名片设置-手机")
        return self.RMSY_contacts_menu_cardsetting_tel

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-邮箱
    def RMSY_contacts_menu_cardsetting_mail(self):
        self.RMSY_contacts_menu_cardsetting_mail = self.p.get_element("id->com.yunlu6.stone:id/sb_em_bt", "人脉首页-点击联系人-打开主菜单-名片设置-邮箱")
        return self.RMSY_contacts_menu_cardsetting_mail

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-QQ
    def RMSY_contacts_menu_cardsetting_qq(self):
        self.RMSY_contacts_menu_cardsetting_qq = self.p.get_element("id->com.yunlu6.stone:id/sb_qq_bt", "人脉首页-点击联系人-打开主菜单-名片设置-QQ")
        return self.RMSY_contacts_menu_cardsetting_qq

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-开放名片列表
    def RMSY_contacts_menu_cardsetting_cardlist(self):
        self.RMSY_contacts_menu_cardsetting_cardlist = self.p.get_elements("id->com.yunlu6.stone:id/toggle_button", "人脉首页-点击联系人-打开主菜单-名片设置-开放名片列表")
        return self.RMSY_contacts_menu_cardsetting_cardlist

    #begin_level_1---------------------------------------------------预览所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览
    def RMSY_contacts_menu_cardsetting_preview(self):
        self.RMSY_contacts_menu_cardsetting_preview = self.p.get_element("id->com.yunlu6.stone:id/btn_exchange", "人脉首页-点击联系人-打开主菜单-名片设置-预览")
        return self.RMSY_contacts_menu_cardsetting_preview

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-返回
    def RMSY_contacts_menu_cardsetting_preview_back(self):
        self.RMSY_contacts_menu_cardsetting_preview_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-名片设置-预览-返回")
        return self.RMSY_contacts_menu_cardsetting_preview_back

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-电话
    def RMSY_contacts_menu_cardsetting_preview_tel(self):
        self.RMSY_contacts_menu_cardsetting_preview_tel = self.p.get_element("id->com.yunlu6.stone:id/iv_top_call", "人脉首页-点击联系人-打开主菜单-名片设置-预览-电话")
        return self.RMSY_contacts_menu_cardsetting_preview_tel

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-联系方式列表
    def RMSY_contacts_menu_cardsetting_preview_contacttypes(self):
        self.RMSY_contacts_menu_cardsetting_preview_contacttypes = self.p.get_elements("id->com.yunlu6.stone:id/iv_contact", "人脉首页-点击联系人-打开主菜单-名片设置-预览-联系方式列表")
        return self.RMSY_contacts_menu_cardsetting_preview_contacttypes

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-发送名片
    def RMSY_contacts_menu_cardsetting_preview_sendcard(self):
        self.RMSY_contacts_menu_cardsetting_preview_sendcard = self.p.get_element("id->com.yunlu6.stone:id/btn_exchange", "人脉首页-点击联系人-打开主菜单-名片设置-预览-发送名片")
        return self.RMSY_contacts_menu_cardsetting_preview_sendcard
    #end_level_1---------------------------------------------------热度设置所有元素定位完毕------------------------------------------------------