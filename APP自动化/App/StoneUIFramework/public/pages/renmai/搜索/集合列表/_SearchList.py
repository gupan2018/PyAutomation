__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索._Search import _Search

class _SearchList(_Search):
    #定位：人脉首页-搜索-集合列表
    def RMSY_search_list(self):
        self.RMSY_search_list = self.p.get_elements("id->com.yunlu6.stone:id/iv_arrow", "人脉首页-搜索-集合列表")
        return self.RMSY_search_list

    #定位：人脉首页-搜索-集合列表-返回
    def RMSY_search_list_back(self):
        self.RMSY_search_list_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-搜索-集合列表-返回")
        return self.RMSY_search_list_back

    #定位：人脉首页-搜索-集合列表-搜索输入框
    def RMSY_search_list_searchinput(self):
        self.RMSY_search_list_searchinput = self.p.get_element("id->com.yunlu6.stone:id/edit_text", "人脉首页-搜索-集合列表-搜索输入框")
        return self.RMSY_search_list_searchinput

    #定位：人脉首页-搜索-集合列表-搜索按钮
    def RMSY_search_list_searchbtn(self):
        self.RMSY_search_list_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_search", "人脉首页-搜索-集合列表-搜索按钮")
        return self.RMSY_search_list_searchbtn

    #---------------------------------------------------编辑所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-编辑
    def RMSY_search_list_edit(self):
        self.RMSY_search_list_edit = self.p.get_element("id->com.yunlu6.stone:id/tv_edit", "人脉首页-搜索-集合列表-编辑")
        return self.RMSY_search_list_edit

    #定位：人脉首页-搜索-集合列表-编辑-返回
    def RMSY_search_list_edit_back(self):
        self.RMSY_search_list_edit_back = self.p.get_element("id->com.yunlu6.stone:id/iv_batch_back", "人脉首页-搜索-集合列表-编辑-返回")
        return self.RMSY_search_list_edit_back

    #定位：人脉首页-搜索-集合列表-编辑-全选
    def RMSY_search_list_edit_all(self):
        self.RMSY_search_list_edit_all = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-搜索-集合列表-编辑-全选")
        return self.RMSY_search_list_edit_all

    #定位：人脉首页-搜索-集合列表-编辑-选择成员
    def RMSY_search_list_edit_selectmember(self):
        self.RMSY_search_list_edit_selectmember = self.p.get_elements("id->com.yunlu6.stone:id/iv_select", "人脉首页-搜索-集合列表-编辑-选择成员")
        return self.RMSY_search_list_edit_selectmember

    #定位：人脉首页-搜索-集合列表-编辑-删除和还原

    #---------------------------------------------------成员列表所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-成员列表
    def RMSY_search_list_memberlist(self):
        self.RMSY_search_list_memberlist = self.p.get_elements("id->com.yunlu6.stone:id/iv_arrow", "人脉首页-搜索-集合列表-成员列表")
        return self.RMSY_search_list_memberlist