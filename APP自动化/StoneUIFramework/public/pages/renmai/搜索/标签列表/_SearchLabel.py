__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索._Search import _Search

class _SearchLabel(_Search):
    #定位：人脉首页-搜索-标签列表
    def RMSY_search_label(self):
        self.RMSY_search_label = self.p.get_elements("id->com.yunlu6.stone:id/tag_id", "人脉首页-搜索-标签列表")
        return self.RMSY_search_label



