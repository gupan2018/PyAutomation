__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai._RenmaiIndex import _RenmaiIndexPage

class _Menu(_RenmaiIndexPage):
    #人脉首页-主菜单
    def RMSY_menu(self):
        self.RMSY_menu = self.p.get_elements("id->com.yunlu6.stone:id/iv_right", "人脉首页-主菜单")
        return self.RMSY_menu