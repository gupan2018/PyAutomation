__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人._Contacts import _Contacts

class _ContactsDelete(_Contacts):
    def RMSY_Contacts_delete(self):
        self.RMSY_Contacts_delete = self.p.get_element("id->com.yunlu6.stone:id/ll_blacklist", "人脉首页-点击联系人-删除")
        return  self.RMSY_Contacts_delete

    #---------------------------------------------------点击删除操作后所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-删除-取消
    def RMSY_Contacts_delete_cancel(self):
        self.RMSY_Contacts_delete_cancel = self.p.get_element("id->com.yunlu6.stone:id/bt_cancel", "人脉首页-点击联系人-删除-取消")
        return self.RMSY_Contacts_delete_cancel

    #定位：人脉首页-点击联系人-删除-确认
    def RMSY_Contacts_delete_confirm(self):
        self.RMSY_Contacts_delete_confirm = self.p.get_element("id->com.yunlu6.stone:id/bt_affirm", "人脉首页-点击联系人-删除-确认")
        return self.RMSY_Contacts_delete_confirm