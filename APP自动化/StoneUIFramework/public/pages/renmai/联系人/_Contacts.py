__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai._RenmaiIndex import _RenmaiIndexPage

class _Contacts(_RenmaiIndexPage):
    #人脉首页-点击联系人
    def RMSY_clickcontacts(self):
        self.RMSY_clickcontacts = self.p.get_elements("id->com.yunlu6.stone:id/iv_arrow", "人脉首页-点击联系人")
        return self.RMSY_clickcontacts