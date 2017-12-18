__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.集合列表._SearchList import _SearchList
from StoneUIFramework.public.handle.renmai.搜索._Search import _SearchHandle

class _SearchListHandle(_SearchList, _SearchHandle):
    #定位：人脉首页-搜索-集合列表
    def RMSY_search_list_click(self, n):
        return self.p.click(self.RMSY_search_list()[n])

    #定位：人脉首页-搜索-集合列表-返回
    def RMSY_search_list_back_click(self):
        return self.p.click(self.RMSY_search_list_back())

    #定位：人脉首页-搜索-集合列表-搜索输入框
    def RMSY_search_list_searchinput_sendkeys(self, text):
        return self.p.send_keys(self.RMSY_search_list_searchinput(), text)

    #定位：人脉首页-搜索-集合列表-搜索按钮
    def RMSY_search_list_searchbtn_click(self):
        return self.p.click(self.RMSY_search_list_searchbtn())

    #---------------------------------------------------编辑所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-编辑
    def RMSY_search_list_edit_click(self):
        return self.p.click(self.RMSY_search_list_edit())

    #定位：人脉首页-搜索-集合列表-编辑-返回
    def RMSY_search_list_edit_back_click(self):
        return self.p.click(self.RMSY_search_list_edit_back())

    #定位：人脉首页-搜索-集合列表-编辑-全选
    def RMSY_search_list_edit_all_click(self):
        return self.p.click(self.RMSY_search_list_edit_all())

    #定位：人脉首页-搜索-集合列表-编辑-选择成员
    def RMSY_search_list_edit_selectmember_click(self, n):
        return self.p.click(self.RMSY_search_list_edit_selectmember()[n])

    #定位：人脉首页-搜索-集合列表-编辑-删除和还原

    #---------------------------------------------------成员列表所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-成员列表
    def RMSY_search_list_memberlist_click(self, n):
        return self.p.click(self.RMSY_search_list_memberlist()[n])