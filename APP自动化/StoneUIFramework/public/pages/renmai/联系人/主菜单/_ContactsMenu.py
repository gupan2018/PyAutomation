__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人._Contacts import _Contacts

class _ContactsMenu(_Contacts):
    #定位：人脉首页-点击联系人-打开主菜单
    def RMSY_contacts_menu(self):
        self.RMSY_contacts_menu = self.p.get_element("id->com.yunlu6.stone:id/iv_more", "人脉首页-点击联系人-打开主菜单")
        return self.RMSY_contacts_menu