__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索._Search import _Search

class _SearchBack(_Search):
    def RMSY_search_back(self):
        self.RMSY_search_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-搜索-返回")
        return self.RMSY_search_back