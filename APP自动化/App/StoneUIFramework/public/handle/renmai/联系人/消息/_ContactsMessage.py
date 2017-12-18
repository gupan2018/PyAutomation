__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息._ContactsMessage import _ContactsMessage
from StoneUIFramework.public.handle.renmai.联系人._Contacts import _ContactsHandle

class _ContactsMessageHandle(_ContactsMessage, _ContactsHandle):
    def RMSY_contacts_message_click(self):
        return self.p.click(self.RMSY_contacts_message())
