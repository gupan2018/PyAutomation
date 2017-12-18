__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.删除._ContactsDelete import _ContactsDelete
from StoneUIFramework.public.handle.renmai.联系人._Contacts import _ContactsHandle

class _ContactsDeleteHandle(_ContactsDelete, _ContactsHandle):
    def RMSY_Contacts_delete_click(self):
        return self.p.click(self.RMSY_Contacts_delete())

    #---------------------------------------------------点击删除操作后所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-删除-取消
    def RMSY_Contacts_delete_cancel_click(self):
        return self.p.click(self.RMSY_Contacts_delete_cancel())

    #定位：人脉首页-点击联系人-删除-确认
    def RMSY_Contacts_delete_confirm_click(self):
        return self.p.click(self.RMSY_Contacts_delete_confirm())