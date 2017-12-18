__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表._SearchLabel import _SearchLabel

class _SearchLabelBack(_SearchLabel):
    #定位：人脉首页-搜索-标签列表-返回
    def RMSY_search_label_back(self):
        self.RMSY_search_label_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-搜索-标签列表-返回")
        return self.RMSY_search_label_back