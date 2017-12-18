__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息.人形按钮._ContactsMsgHumanbtn import _ContactsMsgHumanbtn
from StoneUIFramework.public.handle.renmai.联系人.消息._ContactsMessage import _ContactsMessageHandle

class _ContactsMsgHumanbtnHandle(_ContactsMsgHumanbtn, _ContactsMessageHandle):
    #定位：人脉首页-点击联系人-消息-人形按钮
    def RMSY_contacts_msg_humanbtn_click(self):
        return self.p.click(self.RMSY_contacts_msg_humanbtn())