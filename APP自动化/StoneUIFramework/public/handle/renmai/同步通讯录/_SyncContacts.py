__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.同步通讯录._SyncContacts import _SyncContacts
from StoneUIFramework.public.handle.renmai._RenmaiIndex import _RenmaiIndexHandle

class _SyncContactsHandle(_SyncContacts, _RenmaiIndexHandle):
    #定位：人脉首页-同步通讯录
    def RMSY_syscontacts_click(self):
        return self.p.click(self.RMSY_syscontacts())

    #定位：人脉首页-同步通讯录-返回
    def RMSY_syncContacts_back_click(self):
        return self.p.click(self.RMSY_syncContacts_back())

    #定位：人脉首页-同步通讯录-立即同步
    def RMSY_syncContacts_confirm_click(self):
        return self.p.click(self.RMSY_syncContacts_confirm())