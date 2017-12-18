__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人._Contacts import _Contacts

class _ContactsInvatationtype(_Contacts):
    #定位;人脉首页-点击联系人-邀请方式
    def RMSY_contacts_invatationtype(self):
        self.RMSY_contacts_invatationtype = self.p.get_elements("id->com.yunlu6.stone:id/iv_item_share", "人脉首页-点击联系人-邀请方式")
        return self.RMSY_contacts_invatationtype