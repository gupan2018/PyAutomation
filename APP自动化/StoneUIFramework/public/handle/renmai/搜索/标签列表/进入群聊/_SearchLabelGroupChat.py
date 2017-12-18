__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表.进入群聊._SearchLabelGroupChat import _SearchLabelGroupChat
from StoneUIFramework.public.handle.renmai.搜索.标签列表._SearchLabel import _SearchLabelHandle

class _SearchLabelGroupChatHandle(_SearchLabelGroupChat, _SearchLabelHandle):
    #定位：人脉首页-搜索-标签列表-点击进入群聊
    def RMSY_search_label_groupchat_click(self):
        return self.RMSY_search_label_groupchat()

    #定位：人脉首页-搜索-标签列表-点击进入群聊-返回
    def RMSY_search_label_groupchat_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-消息输入框
    def RMSY_search_label_groupchat_msginput_sendkeys(self, text):
        return self.p.send_keys(self.RMSY_search_label_groupchat_msginput(), text)

    #定位：人脉首页-搜索-标签列表-点击进入群聊-发送
    def RMSY_search_label_groupchat_send_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_send())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-表情
    def RMSY_search_label_groupchat_emoji_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_emoji())
    
    #定位：人脉首页-搜索-标签列表-点击进入群聊-表情-表情列表
    def RMSY_search_label_groupchat_emoji_emojilist_click(self, n):
        return self.p.click(self.RMSY_search_label_groupchat_emoji_emojilist()[n])
    
    #定位：人脉首页-搜索-标签列表-点击进入群聊-功能按钮
    def RMSY_search_label_groupchat_func_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_func())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-功能按钮-功能列表
    def RMSY_search_label_groupchat_func_funclist_click(self, n):
        return self.p.click(self.RMSY_search_label_groupchat_func_funclist()[n])

    #begin_level_1---------------------------------------------------主菜单所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单
    def RMSY_search_label_groupchat_menu_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu())

    #begin_level_2-------------------------------------------设置所有元素定位------------------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置
    def RMSY_search_label_groupchat_menu_setting_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-返回
    def RMSY_search_label_groupchat_menu_setting_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_back())

    #begin_level_3--------------------------群头像所有元素定位-----------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像
    def RMSY_search_label_groupchat_menu_setting_grouphead_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-返回
    def RMSY_search_label_groupchat_menu_setting_grouphead_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_back())

    #begin_level_3-------------头像所有元素定位-----------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像
    def RMSY_search_label_groupchat_menu_setting_grouphead_head_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_head())

    def RMSY_search_label_groupchat_menu_setting_grouphead_head_takephoto_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_head_takephoto())

    def RMSY_search_label_groupchat_menu_setting_grouphead_head_album_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_head_album())

    def RMSY_search_label_groupchat_menu_setting_grouphead_head_cancel_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_head_cancel())

    #end_level_3--------------------------群头像所有元素定位-----------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称
    def RMSY_search_label_groupchat_menu_setting_groupname_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_groupname())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-返回
    def RMSY_search_label_groupchat_menu_setting_groupname_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_groupname_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-名称输入框
    def RMSY_search_label_groupchat_menu_setting_groupname_nameinput_sendkeys(self, text):
        return self.p.send_keys(self.RMSY_search_label_groupchat_menu_setting_groupname_nameinput(), text)

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-备注名输入框
    def RMSY_search_label_groupchat_menu_setting_groupname_remarknameinput_sendkeys(self, text):
        return self.p.send_keys(self.RMSY_search_label_groupchat_menu_setting_groupname_remarknameinput(), text)

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-保存
    def RMSY_search_label_groupchat_menu_setting_groupname_save_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_groupname_save())
    #begin_level_3--------------------------群名称所有元素定位-----------------------------------
    #end_level_3--------------------------群名称所有元素定位-----------------------------------
    #end_level_2-------------------------------------------设置所有元素定位完毕------------------------------------------


    #begin_level_2-------------------------------------------热度设置所有元素定位--------------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置
    def RMSY_search_label_groupchat_menu_heatsetting_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_heatsetting())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-返回
    def RMSY_search_label_groupchat_menu__heatsetting_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-消息
    def RMSY_search_label_groupchat_menu__heatsetting_msg_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_msg())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-飘泡
    def RMSY_search_label_groupchat_menu__heatsetting_bubble_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_bubble())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-震动
    def RMSY_search_label_groupchat_menu__heatsetting_shock_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_shock())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-铃声
    def RMSY_search_label_groupchat_menu__heatsetting_bell_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_bell())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-确定
    def RMSY_search_label_groupchat_menu__heatsetting_confirm_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_confirm())

    #begin_level_3--------------------------周期所有元素定位-----------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期
    def RMSY_search_label_groupchat_menu__heatsetting_period_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-返回
    def RMSY_search_label_groupchat_menu__heatsetting_period_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-每天
    def RMSY_search_label_groupchat_menu__heatsetting_period_everyday_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_everyday())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-工昨日
    def RMSY_search_label_groupchat_menu__heatsetting_period_workday_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_workday())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-节假日
    def RMSY_search_label_groupchat_menu__heatsetting_period_holiday_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_holiday())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-择日
    def RMSY_search_label_groupchat_menu__heatsetting_period_selectday_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_selectday())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-保存
    def RMSY_search_label_groupchat_menu__heatsetting_period_save_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_save())

    #end_level_3--------------------------周期所有元素定位完毕-----------------------------------

    #begin_level_3--------------------------时段所有元素定位-----------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段
    def RMSY_search_label_groupchat_menu__heatsetting_time_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_time())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-确定
    def RMSY_search_label_groupchat_menu__heatsetting_time_confirm_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_time_confirm())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-取消
    def RMSY_search_label_groupchat_menu__heatsetting_time_cancel_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_time_cancel())
    #end_level_3--------------------------时段所有元素定位完毕-----------------------------------

    #end_level_2------------------------------------------热度设置所有元素定位完毕--------------------------------------
    #end_level_1---------------------------------------------------主菜单所有元素定位完毕------------------------------------------------------


    #begin_level_1---------------------------------------------------人群按钮所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮
    def RMSY_search_label_groupchat_groupbtn_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_memberbtn())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-返回
    def RMSY_search_label_groupchat_groupbtn_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_groupbtn_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-联系人列表
    def RMSY_search_label_groupchat_groupbtn_Contacts_click(self, n):
        return self.p.click(self.RMSY_search_label_groupchat_groupbtn_Contacts()[n])

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-消息输入框
    def RMSY_search_label_groupchat_groupbtn_msginput_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_groupbtn_msginput())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-消息按钮
    def RMSY_search_label_groupchat_groupbtn_msgbtn_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_groupbtn_msgbtn())
    #end_level_1---------------------------------------------------人群按钮所有元素定位完毕------------------------------------------------------








