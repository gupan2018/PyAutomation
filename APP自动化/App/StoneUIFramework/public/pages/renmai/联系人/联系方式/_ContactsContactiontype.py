__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人._Contacts import _Contacts

class _ContactsContactiontype(_Contacts):
    #定位;人脉首页-点击联系人-联系方式列表
    def RMSY_contacts_contactiontype(self):
        self.RMSY_contacts_contactiontype = self.p.get_elements("id->com.yunlu6.stone:id/iv_contact", "人脉首页-点击联系人-选择联系方式")
        return self.RMSY_contacts_contactiontype