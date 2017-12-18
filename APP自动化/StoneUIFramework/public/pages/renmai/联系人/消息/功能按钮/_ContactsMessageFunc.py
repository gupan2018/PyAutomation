__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息._ContactsMessage import _ContactsMessage

class _ContactsMsgFunc(_ContactsMessage):
    #定位：人脉首页-点击联系人-消息-功能按钮
    def RMSY_contacts_msg_func(self):
        self.RMSY_contacts_msg_func = self.p.get_element("id->com.yunlu6.stone:id/iv_send", "人脉首页-点击联系人-消息-功能按钮")
        return self.RMSY_contacts_msg_func

    #定位：人脉首页-点击联系人-消息-功能按钮-功能列表
    def RMSY_contacts_msg_func_funclist(self):
        self.RMSY_contacts_msg_func_funclist = self.p.get_elements("id->com.yunlu6.stone:id/iv", "人脉首页-点击联系人-消息-功能按钮-功能列表")
        return self.RMSY_contacts_msg_func_funclist