__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表.搜索._SearchLabelSearch import _SearchLabelSearch
from StoneUIFramework.public.handle.renmai.搜索.标签列表._SearchLabel import _SearchLabelHandle

class _SearchLabelSearchHandle(_SearchLabelSearch, _SearchLabelHandle):
    #定位：人脉首页-搜索-标签列表-搜索框
    def RMSY_search_label_searchinput_sendkey(self, text):
        return self.p.send_keys(self.RMSY_search_label_searchinput(), text)

    #定位：人脉首页-搜索-标签列表-搜索按钮
    def RMSY_search_label_searchbtn_click(self):
        return self.p.click(self.RMSY_search_label_searchbtn())
