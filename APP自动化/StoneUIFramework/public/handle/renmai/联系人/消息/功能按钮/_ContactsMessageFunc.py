__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息.功能按钮._ContactsMessageFunc import _ContactsMsgFunc
from StoneUIFramework.public.handle.renmai.联系人.消息._ContactsMessage import _ContactsMessageHandle

class _ContactsMsgFuncHandle(_ContactsMsgFunc, _ContactsMessageHandle):
    #定位：人脉首页-点击联系人-消息-功能按钮
    def RMSY_contacts_msg_func_click(self):
        return self.p.click(self.RMSY_contacts_msg_func())

    #定位：人脉首页-点击联系人-消息-功能按钮-功能列表
    def RMSY_contacts_msg_func_funclist_click(self, n):
        return self.p.click(self.RMSY_contacts_msg_func_funclist()[n])