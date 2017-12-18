__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表._SearchLabel import _SearchLabel

class _SearchLabelSearch(_SearchLabel):
    #定位：人脉首页-搜索-标签列表-搜索框
    def RMSY_search_label_searchinput(self):
        self.RMSY_search_label_searchinput = self.p.get_element("id->com.yunlu6.stone:id/edit_text", "人脉首页-搜索-标签列表-搜索框")
        return self.RMSY_search_label_searchinput

    #定位：人脉首页-搜索-标签列表-搜索按钮
    def RMSY_search_label_searchbtn(self):
        self.RMSY_search_label_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_search", "人脉首页-搜索-标签列表-搜索按钮")
        return self.RMSY_search_label_searchbtn
