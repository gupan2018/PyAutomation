__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.主菜单._ContactsMenu import _ContactsMenu

class _Tag(_ContactsMenu):
    #定位：人脉首页-点击联系人-打开主菜单-标签
    def RMSY_contacts_menu_tag(self):
        self.RMSY_contacts_menu_tag = self.p.get_element("id->com.yunlu6.stone:id/label", "人脉首页-点击联系人-打开主菜单-标签")
        return self.RMSY_contacts_menu_tag

    #定位：人脉首页-点击联系人-打开主菜单-标签-返回
    def RMSY_contacts_menu_tag_back(self):
        self.RMSY_contacts_menu_tag_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-标签-返回")
        return self.RMSY_contacts_menu_tag_back

    #定位：人脉首页-点击联系人-打开主菜单-标签-保存
    def RMSY_contacts_menu_tag_save(self):
        self.RMSY_contacts_menu_tag_save = self.p.get_element("id->com.yunlu6.stone:id/iv_confirm", "人脉首页-点击联系人-打开主菜单-标签-返回")
        return self.RMSY_contacts_menu_tag_save

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签类型
    def RMSY_contacts_menu_tag_tagtype(self):
        self.RMSY_contacts_menu_tag_tags = self.p.get_elements("id->com.yunlu6.stone:id/tv_name", "人脉首页-点击联系人-打开主菜单-标签-选择标签类型")
        return self.RMSY_contacts_menu_tag_tagtype

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签
    def RMSY_contacts_menu_tag_tags(self):
        self.RMSY_contacts_menu_tag_tags = self.p.get_elements("id->com.yunlu6.stone:id/tag_id", "人脉首页-点击联系人-打开主菜单-标签-选择标签")
        return self.RMSY_contacts_menu_tag_tags

    #begin---------------------------------------------------自定义所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签
    def RMSY_contacts_menu_tag_customtag(self):
        self.RMSY_contacts_menu_tag_customtag = self.p.get_element("id->com.yunlu6.stone:id/iv_add", "人脉首页-点击联系人-打开主菜单-标签-自定义标签")
        return self.RMSY_contacts_menu_tag_customtag

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-返回
    def RMSY_contacts_menu_tag_customtag_back(self):
        self.RMSY_contacts_menu_tag_customtag_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-标签-自定义标签-返回")
        return self.RMSY_contacts_menu_tag_customtag_back

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-输入标签名
    def RMSY_contacts_menu_tag_customtag_taginput(self):
        self.RMSY_contacts_menu_tag_customtag_taginput = self.p.get_element("id->com.yunlu6.stone:id/edit_text", "人脉首页-点击联系人-打开主菜单-标签-自定义标签-输入标签名")
        return self.RMSY_contacts_menu_tag_customtag_taginput

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-添加
    def RMSY_contacts_menu_tag_customtag_add(self):
        self.RMSY_contacts_menu_tag_customtag_add = self.p.get_element("id->com.yunlu6.stone:id/btn_add", "人脉首页-点击联系人-打开主菜单-标签-自定义标签-输入标签名")
        return self.RMSY_contacts_menu_tag_customtag_add
    #begin---------------------------------------------------自定义所有元素定位完毕------------------------------------------------------
