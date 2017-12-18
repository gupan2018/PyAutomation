__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表.返回按钮._SearchLabelBack import _SearchLabelBack
from StoneUIFramework.public.handle.renmai.搜索.标签列表._SearchLabel import _SearchLabelHandle

class _SearchLabelBackHandle(_SearchLabelBack, _SearchLabelHandle):
    #定位：人脉首页-搜索-标签列表-返回
    def RMSY_search_label_back_click(self):
        return self.p.click(self.RMSY_search_label_back())