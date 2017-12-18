__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai._RenmaiIndex import _RenmaiIndexPage

class _Search(_RenmaiIndexPage):
    #定位：人脉首页搜索输入框
    def RMST_searchinput(self):
        self.RMST_searchinput = self.p.get_element("id->com.yunlu6.stone:id/img_btn_search", "人脉首页-搜索输入框")
        return self.RMST_searchinput

    def RMSY_searchbtn(self):
        self.RMSY_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv", "人脉首页-搜索输入框")