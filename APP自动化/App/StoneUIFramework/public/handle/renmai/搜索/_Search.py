__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索._Search import _Search
from StoneUIFramework.public.handle.renmai._RenmaiIndex import _RenmaiIndexHandle

class _SearchHandle(_Search, _RenmaiIndexHandle):
    #定位：人脉首页-搜索输入框
    def RMST_searchinput_sendkeys(self, text):
        return self.p.send_keys(self.RMST_searchinput(), text)

    #定位：人脉首页-搜索按钮
    def RMSY_searchbtn_click(self):
        return self.p.click(self.RMSY_searchbtn())