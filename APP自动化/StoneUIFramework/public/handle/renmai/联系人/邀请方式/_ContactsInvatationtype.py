__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.邀请方式._ContactsInvatationtype import _ContactsInvatationtype
from StoneUIFramework.public.handle.renmai.联系人._Contacts import _ContactsHandle

class _ContactsInvatationtypeHandle(_ContactsInvatationtype, _ContactsHandle):
    #定位;人脉首页-点击联系人-邀请方式
    def RMSY_contacts_invatationtype_click(self, n):
        return self.p.click(self.RMSY_contacts_invatationtype()[n])