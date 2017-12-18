__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人._Contacts import _Contacts

class _ContactsMessage(_Contacts):
    def RMSY_contacts_message(self):
        self.RMSY_contacts_message = self.p.get_element("id->com.yunlu6.stone:id/edit_text", "人脉首页-点击联系人-进入聊天界面")
        return self.RMSY_contacts_message
