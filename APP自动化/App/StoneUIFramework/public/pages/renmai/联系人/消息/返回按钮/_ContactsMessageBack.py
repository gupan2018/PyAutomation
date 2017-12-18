__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息._ContactsMessage import _ContactsMessage

class _ContactsMsgBack(_ContactsMessage):
    #定位：人脉首页-点击联系人-消息-返回
    def RMSY_contacts_msg_back(self):
        self.RMSY_contacts_msg_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-点击联系人-消息-返回")
        return self.RMSY_contacts_msg_back