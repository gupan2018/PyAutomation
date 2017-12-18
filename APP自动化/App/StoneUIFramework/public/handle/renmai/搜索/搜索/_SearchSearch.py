__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.搜索._SearchSearch import _SearchSearch
from StoneUIFramework.public.handle.renmai.搜索._Search import _SearchHandle

class _SearchSearchHandle(_SearchSearch, _SearchHandle):
    #定位：人脉首页-搜索-搜索输入框
    def RMSY_search_searchinput_sendkeys(self, text):
        return self.p.send_keys(self.RMSY_search_searchinput(), text)

    #定位：人脉首页-搜索-搜索按钮
    def RMST_search_searchbtn_click(self):
        return self.p.click(self.RMST_search_searchbtn())

    #定位：人脉首页-搜索-搜索按钮-匹配联系人列表
    def RMST_search_searchbtn_matchcontacts_click(self, n):
        return self.p.click(self.RMST_search_searchbtn_matchcontacts()[n])