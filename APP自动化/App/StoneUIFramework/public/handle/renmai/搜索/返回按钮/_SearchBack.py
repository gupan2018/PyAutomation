__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.返回按钮._SearchBack import _SearchBack
from StoneUIFramework.public.handle.renmai.搜索._Search import _SearchHandle

class _SearchBackHandle(_SearchBack, _SearchHandle):
    def RMSY_search_back_click(self):
        return self.p.click(self.RMSY_search_back())