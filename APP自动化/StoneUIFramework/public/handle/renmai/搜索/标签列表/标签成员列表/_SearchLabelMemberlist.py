__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表.标签成员列表._SearchLabelMemberlist import _SearchLabelMemberlist
from StoneUIFramework.public.handle.renmai.搜索.标签列表._SearchLabel import _SearchLabelHandle

class _SearchLabelMemberlistHandle(_SearchLabelMemberlist, _SearchLabelHandle):
    #定位：人脉首页-搜索-标签列表-标签成员列表
    def RMSY_search_label_memberlist_click(self, n):
        return self.p.click(self.RMSY_search_label_memberlist()[n])