__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息.返回按钮._ContactsMessageBack import _ContactsMsgBack
from StoneUIFramework.public.handle.renmai.联系人.消息._ContactsMessage import _ContactsMessageHandle

class _ContactsMsgBackHandle(_ContactsMsgBack, _ContactsMessageHandle):
    #定位：人脉首页-点击联系人-消息-返回
    def RMSY_contacts_msg_back_click(self):
        return self.p.click(self.RMSY_contacts_msg_back())