__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人._Contacts import _Contacts
from StoneUIFramework.public.handle.renmai._RenmaiIndex import _RenmaiIndexHandle

class _ContactsHandle(_Contacts, _RenmaiIndexHandle):
    #人脉首页-点击联系人
    def RMSY_clickcontacts_click(self, n):
        return self.p.click(self.RMSY_clickcontacts()[n])