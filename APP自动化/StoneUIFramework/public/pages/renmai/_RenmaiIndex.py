__author__ = 'Administrator'
#人脉首页
from StoneUIFramework.public.common.basepage import Page

class _RenmaiIndexPage(Page):
    #定位：人脉首页
    def RMSY(self):
        self.RMSY = self.p.get_elements("id->com.yunlu6.stone:id/navi_item_connection", "人脉首页")
        return self.RMSY
