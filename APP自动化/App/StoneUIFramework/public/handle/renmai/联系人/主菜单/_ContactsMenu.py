__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.主菜单._ContactsMenu import _ContactsMenu
from StoneUIFramework.public.handle.renmai.联系人._Contacts import _ContactsHandle

class _ContactsMenuHandle(_ContactsHandle, _ContactsMenu):
    #定位：人脉首页-点击联系人-打开主菜单
    def RMSY_contacts_menu_click(self):
        return self.p.click(self.RMSY_contacts_menu())