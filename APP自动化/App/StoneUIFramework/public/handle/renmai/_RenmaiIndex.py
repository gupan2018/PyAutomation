__author__ = 'Administrator'
#人脉首页
from StoneUIFramework.public.pages.renmai._RenmaiIndex import _RenmaiIndexPage

class _RenmaiIndexHandle(_RenmaiIndexPage):
    #定位：人脉首页
    def RMSY_click(self):
        return self.p.click(self.RMSY())
