__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.主菜单.名片设置._CardSetting import _CardSetting
from StoneUIFramework.public.handle.renmai.联系人.主菜单._ContactsMenu import _ContactsMenuHandle

class _CardSettingHandle(_CardSetting, _ContactsMenuHandle):
    #定位：人脉首页-点击联系人-打开主菜单-名片设置
    def RMSY_contacts_menu_cardsetting_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-返回
    def RMSY_contacts_menu_cardsetting_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-全部屏蔽
    def RMSY_contacts_menu_cardsetting_sheildall_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_sheildall())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-姓名
    def RMSY_contacts_menu_cardsetting_name_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_name())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-手机
    def RMSY_contacts_menu_cardsetting_tel_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_tel())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-邮箱
    def RMSY_contacts_menu_cardsetting_mail_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_mail())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-QQ
    def RMSY_contacts_menu_cardsetting_qq_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_qq())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-开放名片列表
    def RMSY_contacts_menu_cardsetting_cardlist_click(self, n):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_cardlist()[n])

    #begin_level_1---------------------------------------------------预览所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览
    def RMSY_contacts_menu_cardsetting_preview_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-返回
    def RMSY_contacts_menu_cardsetting_preview_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview_back())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-电话
    def RMSY_contacts_menu_cardsetting_preview_tel_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview_tel())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-联系方式列表
    def RMSY_contacts_menu_cardsetting_preview_contacttypes_click(self, n):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview_contacttypes()[n])

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-发送名片
    def RMSY_contacts_menu_cardsetting_preview_sendcard_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview_sendcard())
    #end_level_1---------------------------------------------------热度设置所有元素定位完毕------------------------------------------------------