__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.主菜单.标签._Tag import _Tag
from StoneUIFramework.public.handle.renmai.联系人.主菜单._ContactsMenu import _ContactsMenuHandle

class _TagHandle(_Tag, _ContactsMenuHandle):
    #定位：人脉首页-点击联系人-打开主菜单-标签
    def RMSY_contacts_menu_tag_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag())

    #定位：人脉首页-点击联系人-打开主菜单-标签-返回
    def RMSY_contacts_menu_tag_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_back())

    #定位：人脉首页-点击联系人-打开主菜单-标签-保存
    def RMSY_contacts_menu_tag_save_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_save())

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签类型
    def RMSY_contacts_menu_tag_tagtype_click(self, n):
        return self.p.click(self.RMSY_contacts_menu_tag_tags()[n])

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签
    def RMSY_contacts_menu_tag_tags_click(self, n):
        return self.p.click(self.RMSY_contacts_menu_tag_tags()[n])

    #begin---------------------------------------------------自定义所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签
    def RMSY_contacts_menu_tag_customtag_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_customtag())

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-返回
    def RMSY_contacts_menu_tag_customtag_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_customtag_back())

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-输入标签名
    def RMSY_contacts_menu_tag_customtag_taginput_sendkeys(self, text):
        self.p.send_keys(self.RMSY_contacts_menu_tag_customtag_taginput(), text)

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-添加
    def RMSY_contacts_menu_tag_customtag_add_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_customtag_add())
    #begin---------------------------------------------------自定义所有元素定位完毕------------------------------------------------------
