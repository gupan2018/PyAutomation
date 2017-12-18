__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息._ContactsMessage import _ContactsMessage

class _ContactsMsgMsgOp(_ContactsMessage):
    #定位：人脉首页-点击联系人-消息-消息输入框
    def RMSY_contacts_msg_msginput(self):
        self.RMSY_contacts_msg_msginput = self.p.get_element("id->com.yunlu6.stone:id/message_content_msgcontent", "人脉首页-点击联系人-消息-消息输入框")
        return self.RMSY_contacts_msg_msginput

    #定位：人脉首页-点击联系人-消息-发送消息
    def RMSY_contacts_msg_msgsend(self):
        self.RMSY_contacts_msg_msgsend = self.p.get_element("id->com.yunlu6.stone:id/message_content_send", "人脉首页-点击联系人-消息-发送消息")
        return self.RMSY_contacts_msg_msgsend