__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息._ContactsMessage import _ContactsMessage

class _ContactsMsgHumanbtn(_ContactsMessage):
    #定位：人脉首页-点击联系人-消息-人形按钮
    def RMSY_contacts_msg_humanbtn(self):
        self.RMSY_contacts_msg_humanbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_to_message", "人脉首页-点击联系人-消息-人形按钮")
        return self.RMSY_contacts_msg_humanbtn