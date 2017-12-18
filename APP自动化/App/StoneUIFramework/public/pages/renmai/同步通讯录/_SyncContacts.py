__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai._RenmaiIndex import _RenmaiIndexPage

class _SyncContacts(_RenmaiIndexPage):
    #定位：人脉首页-同步通讯录
    def RMSY_syscontacts(self):
        self.RMSY_syscontacts = self.p.get_element("id->com.yunlu6.stone:id/bt_start_mailer", "人脉首页-同步通讯录")
        return self.RMSY_syscontacts

    #定位：人脉首页-同步通讯录-返回
    def RMSY_syncContacts_back(self):
        self.RMSY_syscontacts_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-同步通讯录-返回")
        return self.RMSY_syscontacts_back

    #定位：人脉首页-同步通讯录-立即同步
    def RMSY_syncContacts_confirm(self):
        self.RMSY_syncContacts_confirm = self.p.get_element("id->com.yunlu6.stone:id/btn_synchro", "人脉首页-同步通讯录-立即同步")
        return self.RMSY_syncContacts_confirm