__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人._Contacts import _Contacts

class _ContactsBack(_Contacts):
    #定位：人脉首页-点击联系人-返回
    def RMSY_contacts_back(self):
        self.RMSY_contacts_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-返回")
        return self.RMSY_contacts_back