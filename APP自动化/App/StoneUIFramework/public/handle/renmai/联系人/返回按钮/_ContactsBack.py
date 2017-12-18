__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.返回按钮._ContactsBack import _ContactsBack
from StoneUIFramework.public.handle.renmai.联系人._Contacts import _ContactsHandle

class _ContactsBackHandle(_ContactsBack, _ContactsHandle):
    #定位：人脉首页-点击联系人-返回
    def RMSY_contacts_back_click(self):
        return self.p.click(self.RMSY_contacts_back())