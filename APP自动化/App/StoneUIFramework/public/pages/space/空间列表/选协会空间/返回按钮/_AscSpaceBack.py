__author__ = 'xiaoj'
from StoneUIFramework.public.pages.space.空间列表.选协会空间._BrowseAscSpace import _BrowseAscSpacePage

class _AscSpaceBackPage(_BrowseAscSpacePage):
    # 空间列表-浏览协会空间-返回
    def Kjlb_browseascspace_back(self):
        self.Kjlb_browseascspace_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-返回")
        return self.Kjlb_browseascspace_back