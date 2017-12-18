__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.主菜单._Menu import _Menu
from StoneUIFramework.public.handle.renmai._RenmaiIndex import _RenmaiIndexHandle

class _MenuHandle(_Menu, _RenmaiIndexHandle):
    #人脉首页-主菜单
    def RMSY_menu_click(self):
        return self.p.click(self.RMSY_menu())