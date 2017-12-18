__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息.表情._ContactsMessageEmoji import _ContactsMsgEmoji
from StoneUIFramework.public.handle.renmai.联系人.消息._ContactsMessage import _ContactsMessageHandle

class _ContactsMsgEmojiHandle(_ContactsMsgEmoji, _ContactsMessageHandle):
    #定位：人脉首页-点击联系人-消息-表情按钮
    def RMSY_contacts_msg_emoji_click(self):
        return self.p.click(self.RMSY_contacts_msg_emoji())

    #定位：人脉首页-点击联系人-消息-表情按钮-表情列表
    def RMSY_contacts_msg_emoji_emojilist_click(self, n):
        return self.p.click(self.RMSY_contacts_msg_emoji_emojilist()[n])