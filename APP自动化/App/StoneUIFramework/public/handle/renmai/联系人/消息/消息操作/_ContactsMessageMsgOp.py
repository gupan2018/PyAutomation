__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息.消息操作._ContactsMessageMsgOp import _ContactsMsgMsgOp
from StoneUIFramework.public.handle.renmai.联系人.消息._ContactsMessage import _ContactsMessageHandle

class _ContactsMsgMsgOpHandle(_ContactsMsgMsgOp, _ContactsMessageHandle):
    #定位：人脉首页-点击联系人-消息-消息输入框
    def RMSY_contacts_msg_msginput_sendkeys(self, text):
        return self.p.send_keys(self.RMSY_contacts_msg_msginput(), text)

    #定位：人脉首页-点击联系人-消息-发送消息
    def RMSY_contacts_msg_msgsend_click(self):
        return self.p.click(self.RMSY_contacts_msg_msgsend())