__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表._SearchLabel import _SearchLabel
from StoneUIFramework.public.handle.renmai.搜索._Search import _SearchHandle

class _SearchLabelHandle(_SearchLabel, _SearchHandle):
    #定位：人脉首页-搜索-标签列表
    def RMSY_search_label_click(self, n):
        return self.p.click(self.RMSY_search_label()[n])



