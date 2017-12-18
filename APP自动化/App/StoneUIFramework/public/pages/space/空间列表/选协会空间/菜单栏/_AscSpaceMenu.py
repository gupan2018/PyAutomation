__author__ = 'xiaoj'
from StoneUIFramework.public.pages.space.空间列表.选协会空间._BrowseAscSpace import _BrowseAscSpacePage

class _AscSpaceMenuPage(_BrowseAscSpacePage):
    #定位:空间列表-浏览协会空间-菜单栏
    def Kjlb_browseascspace_menu(self):
        self.Kjlb_browseascspace_menu = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览协会空间-菜单栏")
        return self.Kjlb_browseascspace_menu