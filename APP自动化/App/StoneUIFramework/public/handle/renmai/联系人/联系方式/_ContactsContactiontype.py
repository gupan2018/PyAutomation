__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.联系方式._ContactsContactiontype import _ContactsContactiontype
from StoneUIFramework.public.handle.renmai.联系人._Contacts import _ContactsHandle

class _ContactsContactiontypeHandle(_ContactsContactiontype, _ContactsHandle):
    #定位;人脉首页-点击联系人-邀请方式
    def RMSY_contacts_contactiontype_click(self, n):
        return self.p.click(self.RMSY_contacts_contactiontype()[n])