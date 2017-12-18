__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索._Search import _Search

class _SearchSearch(_Search):
    #定位：人脉首页-搜索-搜索输入框
    def RMSY_search_searchinput(self):
        self.RMSY_search_searchinput = self.p.get_element("id->com.yunlu6.stone:id/img_btn_search", "人脉首页-搜索-搜索输入框")
        return self.RMSY_search_searchinput

    #定位：人脉首页-搜索-搜索按钮
    def RMST_search_searchbtn(self):
        self.RMST_search_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv", "人脉首页-搜索-搜索按钮")
        return self.RMST_search_searchbtn

    #定位：人脉首页-搜索-搜索按钮-匹配联系人列表
    def RMST_search_searchbtn_matchcontacts(self):
        self.RMST_search_searchbtn_matchcontacts = self.p.get_elements("id->com.yunlu6.stone:id/iv", "人脉首页-搜索-搜索按钮-匹配联系人列表")
        return self.RMST_search_searchbtn_matchcontacts