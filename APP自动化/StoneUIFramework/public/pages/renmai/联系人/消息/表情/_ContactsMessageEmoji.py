__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息._ContactsMessage import _ContactsMessage

class _ContactsMsgEmoji(_ContactsMessage):
    #定位：人脉首页-点击联系人-消息-表情按钮
    def RMSY_contacts_msg_emoji(self):
        self.RMSY_contacts_msg_emoji = self.p.get_element("id->com.yunlu6.stone:id/iv_emoji", "人脉首页-点击联系人-消息-表情按钮")
        return self.RMSY_contacts_msg_emoji

    #定位：人脉首页-点击联系人-消息-表情按钮-表情列表
    def RMSY_contacts_msg_emoji_emojilist(self):
        self.RMSY_contacts_msg_emoji_emojilist = self.p.get_elements("id->com.yunlu6.stone:id/item_iv_face", "人脉首页-点击联系人-消息-表情按钮-表情列表")
        return self.RMSY_contacts_msg_emoji_emojilist