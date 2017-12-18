__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.主菜单._ContactsMenu import _ContactsMenu

class _Memo(_ContactsMenu):
    #定位：人脉首页-点击联系人-打开主菜单-备忘
    def RMSY_contacts_menu_memo(self):
        self.RMSY_contacts_menu_memo = self.p.get_element("id->com.yunlu6.stone:id/memorandum", "人脉首页-点击联系人-打开主菜单-备忘")
        return self.RMSY_contacts_menu_memo

    #定位：人脉首页-点击联系人-打开主菜单-备忘-返回
    def RMSY_contacts_menu_memo_back(self):
        self.RMSY_contacts_menu_memo_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-备忘-返回")
        return self.RMSY_contacts_menu_memo_back

    #begin---------------------------------------------------修改备注所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注
    def RMSY_contacts_menu_memo_changenotename(self):
        self.RMSY_contacts_menu_memo_changenotename = self.p.get_element("id->com.yunlu6.stone:id/bt_edit", "人脉首页-点击联系人-打开主菜单-备忘-修改备注")
        return self.RMSY_contacts_menu_memo_changenotename

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-输入备注名
    def RMSY_contacts_menu_memo_changenotename_notenameinput(self):
        self.RMSY_contacts_menu_memo_changenotename_notenameinput = self.p.get_element("id->com.yunlu6.stone:id/et_remark_name", "人脉首页-点击联系人-打开主菜单-备忘--输入备注名")
        return self.RMSY_contacts_menu_memo_changenotename_notenameinput

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-确定
    def RMSY_contacts_menu_memo_changenotename_confirm(self):
        self.RMSY_contacts_menu_memo_changenotename_confirm = self.p.get_element("id->com.yunlu6.stone:id/dialog_remark_sure", "人脉首页-点击联系人-打开主菜单-备忘-修改备注-确定")
        return self.RMSY_contacts_menu_memo_changenotename_confirm

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-取消
    def RMSY_contacts_menu_memo_changenotename_cancel(self):
        self.RMSY_contacts_menu_memo_changenotename_cancel = self.p.get_element("id->com.yunlu6.stone:id/dialog_remark_no", "人脉首页-点击联系人-打开主菜单-备忘-修改备注-取消")
        return self.RMSY_contacts_menu_memo_changenotename_cancel
    #end--------------------------------------------------修改备注所有元素定位完毕------------------------------------------------------

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容
    def RMSY_contacts_menu_memo_memocontent(self):
        self.RMSY_contacts_menu_memo_memocontent = self.p.get_element("id->com.yunlu6.stone:id/et_memo_info", "人脉首页-点击联系人-打开主菜单-备忘-备忘内容")
        return self.RMSY_contacts_menu_memo_memocontent

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容-确定
    def RMSY_contacts_menu_memo_memocontent_confirm(self):
        self.RMSY_contacts_menu_memo_memocontent_confirm = self.p.get_element("id->com.yunlu6.stone:id/bt_confirm", "人脉首页-点击联系人-打开主菜单-备忘-备忘内容-确定")
        return self.RMSY_contacts_menu_memo_memocontent_confirm


