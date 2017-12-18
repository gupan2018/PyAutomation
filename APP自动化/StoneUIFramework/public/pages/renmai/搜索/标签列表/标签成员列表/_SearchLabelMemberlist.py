__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表._SearchLabel import _SearchLabel

class _SearchLabelMemberlist(_SearchLabel):
    #定位：人脉首页-搜索-标签列表-标签成员列表
    def RMSY_search_label_memberlist(self):
        self.RMSY_search_label_memberlist = self.p.get_elements("id->com.yunlu6.stone:id/item_name", "人脉首页-搜索-标签列表-标签成员列表")
        return self.RMSY_search_label_memberlist