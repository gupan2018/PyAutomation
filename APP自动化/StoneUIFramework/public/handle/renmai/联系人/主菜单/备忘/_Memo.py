__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.主菜单.备忘._Memo import _Memo
from StoneUIFramework.public.handle.renmai.联系人.主菜单._ContactsMenu import _ContactsMenuHandle

class _MemoHandle(_Memo, _ContactsMenuHandle):
    #定位：人脉首页-点击联系人-打开主菜单-备忘
    def RMSY_contacts_menu_memo_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo())

    #定位：人脉首页-点击联系人-打开主菜单-备忘-返回
    def RMSY_contacts_menu_memo_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo_back())

    #begin---------------------------------------------------修改备注所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注
    def RMSY_contacts_menu_memo_changenotename_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo_changenotename())

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-输入备注名
    def RMSY_contacts_menu_memo_changenotename_notenameinput_sendkeys(self, text):
        return self.p.send_keys(self.RMSY_contacts_menu_memo_changenotename_notenameinput(), text)

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-确定
    def RMSY_contacts_menu_memo_changenotename_confirm_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo_changenotename_confirm())

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-取消
    def RMSY_contacts_menu_memo_changenotename_cancel_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo_changenotename_cancel())
    #end--------------------------------------------------修改备注所有元素定位完毕------------------------------------------------------

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容
    def RMSY_contacts_menu_memo_memocontent_sendkeys(self, text):
        return self.p.click(self.RMSY_contacts_menu_memo_memocontent, text)

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容-确定
    def RMSY_contacts_menu_memo_memocontent_confirm_click(self):
        self.p.click(self.RMSY_contacts_menu_memo_memocontent_confirm())