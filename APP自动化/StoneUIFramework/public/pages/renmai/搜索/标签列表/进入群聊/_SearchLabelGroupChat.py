__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.搜索.标签列表._SearchLabel import _SearchLabel

class _SearchLabelGroupChat(_SearchLabel):
    #定位：人脉首页-搜索-标签列表-点击进入群聊
    def RMSY_search_label_groupchat(self):
        row_x = self.p.get_window_size()["width"]
        row_y = self.p.get_window_size()["height"]

        scale_x = float(720 / 1080)
        scale_y = float(1825 / 1920)

        adjust_x = int(row_x * scale_x)
        adjust_y = int(row_y * scale_y)

        self.RMSY_search_label_groupchat_click = self.p.tap([adjust_x, adjust_y], 2)
        return self.RMSY_search_label_groupchat_click

    #定位：人脉首页-搜索-标签列表-点击进入群聊-返回
    def RMSY_search_label_groupchat_back(self):
        self.RMSY_search_label_groupchat_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-搜索-标签列表-点击进入群聊-返回")
        return self.RMSY_search_label_groupchat_back

    #定位：人脉首页-搜索-标签列表-点击进入群聊-消息输入框
    def RMSY_search_label_groupchat_msginput(self):
        self.RMSY_search_label_groupchat_msginput = self.p.get_element("id->com.yunlu6.stone:id/message_content_msgcontent", "人脉首页-搜索-标签列表-点击进入群聊-消息输入框")
        return self.RMSY_search_label_groupchat_msginput

    #定位：人脉首页-搜索-标签列表-点击进入群聊-发送
    def RMSY_search_label_groupchat_send(self):
        self.RMSY_search_label_groupchat_send = self.p.get_element("id->com.yunlu6.stone:id/message_content_send", "人脉首页-搜索-标签列表-点击进入群聊-发送")
        return self.RMSY_search_label_groupchat_send

    #定位：人脉首页-搜索-标签列表-点击进入群聊-表情
    def RMSY_search_label_groupchat_emoji(self):
        self.RMSY_search_label_groupchat_emoji = self.p.get_element("id->com.yunlu6.stone:id/iv_emoji", "人脉首页-搜索-标签列表-点击进入群聊-表情")
        return self.RMSY_search_label_groupchat_emoji
    
    #定位：人脉首页-搜索-标签列表-点击进入群聊-表情-表情列表
    def RMSY_search_label_groupchat_emoji_emojilist(self):
        self.RMSY_search_label_groupchat_emoji_emojilist = self.p.get_elements("id->com.yunlu6.stone:id/item_iv_face", "人脉首页-搜索-标签列表-点击进入群聊-表情-表情列表")
        return self.RMSY_search_label_groupchat_emoji_emojilist
    
    #定位：人脉首页-搜索-标签列表-点击进入群聊-功能按钮
    def RMSY_search_label_groupchat_func(self):
        self.RMSY_search_label_groupchat_func = self.p.get_element("id->com.yunlu6.stone:id/iv_send", "人脉首页-搜索-标签列表-点击进入群聊-功能按钮")
        return self.RMSY_search_label_groupchat_func

    #定位：人脉首页-搜索-标签列表-点击进入群聊-功能按钮-功能列表
    def RMSY_search_label_groupchat_func_funclist(self):
        self.RMSY_search_label_groupchat_func_funclist = self.p.get_elements("id->com.yunlu6.stone:id/iv", "人脉首页-搜索-标签列表-点击进入群聊-功能按钮-功能列表")
        return self.RMSY_search_label_groupchat_func_funclist

    #begin_level_1---------------------------------------------------主菜单所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单
    def RMSY_search_label_groupchat_menu(self):
        self.RMSY_search_label_groupchat_menu = self.p.get_element("id->com.yunlu6.stone:id/title_main_fl_more_menu", "人脉首页-搜索-标签列表-点击进入群聊-主菜单")
        return self.RMSY_search_label_groupchat_menu

    #begin_level_2-------------------------------------------设置所有元素定位------------------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置
    def RMSY_search_label_groupchat_menu_setting(self):
        self.RMSY_search_label_groupchat_menu_setting = self.p.get_element("id->com.yunlu6.stone:id/anti", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置")
        return self.RMSY_search_label_groupchat_menu_setting

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-返回
    def RMSY_search_label_groupchat_menu_setting_back(self):
        self.RMSY_search_label_groupchat_menu_setting_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-返回")
        return self.RMSY_search_label_groupchat_menu_setting_back

    #begin_level_3--------------------------群头像所有元素定位-----------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像
    def RMSY_search_label_groupchat_menu_setting_grouphead(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead = self.p.get_element("id->com.yunlu6.stone:id/rl_img", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-返回
    def RMSY_search_label_groupchat_menu_setting_grouphead_back(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-返回")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_back

    #begin_level_3-------------头像所有元素定位-----------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像
    def RMSY_search_label_groupchat_menu_setting_grouphead_head(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_head = self.p.get_element("id->com.yunlu6.stone:id/iv_logo", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_head

    def RMSY_search_label_groupchat_menu_setting_grouphead_head_takephoto(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_head_takephoto = self.p.get_element("com.yunlu6.stone:id/tv_cloundlibrary_camera", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像-拍照")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_head_takephoto

    def RMSY_search_label_groupchat_menu_setting_grouphead_head_album(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_head_album = self.p.get_element("id->com.yunlu6.stone:id/tv_cloundlibrary_alumm", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像-相册")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_head_album

    def RMSY_search_label_groupchat_menu_setting_grouphead_head_cancel(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_head_cancel = self.p.get_element("id->com.yunlu6.stone:id/bt_commen_cancel", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像-取消")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_head_cancel

    #end_level_3--------------------------群名称所有元素定位-----------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称
    def RMSY_search_label_groupchat_menu_setting_groupname(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname = self.p.get_element("id->com.yunlu6.stone:id/rl_group_name", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称")
        return self.RMSY_search_label_groupchat_menu_setting_groupname

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-返回
    def RMSY_search_label_groupchat_menu_setting_groupname_back(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-返回")
        return self.RMSY_search_label_groupchat_menu_setting_groupname_back

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-名称输入框
    def RMSY_search_label_groupchat_menu_setting_groupname_nameinput(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname_nameinput = self.p.get_element("id->com.yunlu6.stone:id/et_name", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-名称输入框")
        return self.RMSY_search_label_groupchat_menu_setting_groupname_nameinput

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-备注名输入框
    def RMSY_search_label_groupchat_menu_setting_groupname_remarknameinput(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname_remarknameinput = self.p.get_element("id->com.yunlu6.stone:id/rl_group_name", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-备注名输入框")
        return self.RMSY_search_label_groupchat_menu_setting_groupname_remarknameinput

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-保存
    def RMSY_search_label_groupchat_menu_setting_groupname_save(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname_save = self.p.get_element("id->com.yunlu6.stone:id/btn_save", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-保存")
        return self.RMSY_search_label_groupchat_menu_setting_groupname_save
    #begin_level_3--------------------------群名称所有元素定位-----------------------------------
    #end_level_3--------------------------群名称所有元素定位-----------------------------------
    #end_level_2-------------------------------------------设置所有元素定位完毕------------------------------------------


    #begin_level_2-------------------------------------------热度设置所有元素定位--------------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置
    def RMSY_search_label_groupchat_menu_heatsetting(self):
        self.RMSY_search_label_groupchat_menu_heatsetting = self.p.get_element("id->com.yunlu6.stone:id/rl_msgsetting", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置")
        return self.RMSY_search_label_groupchat_menu_heatsetting

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-返回
    def RMSY_search_label_groupchat_menu__heatsetting_back(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-返回")
        return self.RMSY_search_label_groupchat_menu__heatsetting_back

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-消息
    def RMSY_search_label_groupchat_menu__heatsetting_msg(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_msg = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_msg", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-消息")
        return self.RMSY_search_label_groupchat_menu__heatsetting_msg

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-飘泡
    def RMSY_search_label_groupchat_menu__heatsetting_bubble(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_bubble = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_pop", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-飘泡")
        return self.RMSY_search_label_groupchat_menu__heatsetting_bubble

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-震动
    def RMSY_search_label_groupchat_menu__heatsetting_shock(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_shock = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_shock", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-震动")
        return self.RMSY_search_label_groupchat_menu__heatsetting_shock

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-铃声
    def RMSY_search_label_groupchat_menu__heatsetting_bell(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_bell = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_bell", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-铃声")
        return self.RMSY_search_label_groupchat_menu__heatsetting_bell

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-确定
    def RMSY_search_label_groupchat_menu__heatsetting_confirm(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_confirm = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_ok", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-确定")
        return self.RMSY_search_label_groupchat_menu__heatsetting_confirm

    #begin_level_3--------------------------周期所有元素定位-----------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期
    def RMSY_search_label_groupchat_menu__heatsetting_period(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period = self.p.get_element("id->android.widget.ImageView", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-返回
    def RMSY_search_label_groupchat_menu__heatsetting_period_back(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-返回")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_back

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-每天
    def RMSY_search_label_groupchat_menu__heatsetting_period_everyday(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_everyday = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_allday", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-每天")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_everyday

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-工昨日
    def RMSY_search_label_groupchat_menu__heatsetting_period_workday(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_workday = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_workday", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-工昨日")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_workday

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-节假日
    def RMSY_search_label_groupchat_menu__heatsetting_period_holiday(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_holiday = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_holiday", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-节假日")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_holiday

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-择日
    def RMSY_search_label_groupchat_menu__heatsetting_period_selectday(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_selectday = self.p.get_element("id->com.yunlu6.stone:id/im_add_days", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-择日")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_selectday

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-保存
    def RMSY_search_label_groupchat_menu__heatsetting_period_save(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_save = self.p.get_element("id->com.yunlu6.stone:id/btn_messagetime_save", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-保存")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_save

    #end_level_3--------------------------周期所有元素定位完毕-----------------------------------

    #begin_level_3--------------------------时段所有元素定位-----------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段
    def RMSY_search_label_groupchat_menu__heatsetting_time(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_time = self.p.get_element("id->com.yunlu6.stone:id/im_add_time", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段")
        return self.RMSY_search_label_groupchat_menu__heatsetting_time

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-确定
    def RMSY_search_label_groupchat_menu__heatsetting_time_confirm(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_time_confirm = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_ok", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-确定")
        return self.RMSY_search_label_groupchat_menu__heatsetting_time_confirm

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-取消
    def RMSY_search_label_groupchat_menu__heatsetting_time_cancel(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_time_cancel = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_cancel", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-确定")
        return self.RMSY_search_label_groupchat_menu__heatsetting_time_cancel
    #end_level_3--------------------------时段所有元素定位完毕-----------------------------------

    #end_level_2------------------------------------------热度设置所有元素定位完毕--------------------------------------
    #end_level_1---------------------------------------------------主菜单所有元素定位完毕------------------------------------------------------


    #begin_level_1---------------------------------------------------人群按钮所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮
    def RMSY_search_label_groupchat_groupbtn(self):
        self.RMSY_search_label_groupchat_memberbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_to_message", "人脉首页-搜索-标签列表-点击进入群聊-人群按钮")
        return self.RMSY_search_label_groupchat_memberbtn

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-返回
    def RMSY_search_label_groupchat_groupbtn_back(self):
        self.RMSY_search_label_groupchat_groupbtn_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-搜索-标签列表-点击进入群聊-人群按钮-返回")
        return self.RMSY_search_label_groupchat_groupbtn_back

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-联系人列表
    def RMSY_search_label_groupchat_groupbtn_Contacts(self):
        self.RMSY_search_label_groupchat_groupbtn_Contacts = self.p.get_elements("id->com.yunlu6.stone:id/tv_name", "人脉首页-搜索-标签列表-点击进入群聊-人群按钮-联系人列表")
        return self.RMSY_search_label_groupchat_groupbtn_Contacts

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-消息输入框
    def RMSY_search_label_groupchat_groupbtn_msginput(self):
        self.RMSY_search_label_groupchat_groupbtn_msginput = self.p.get_element("id->com.yunlu6.stone:id/message_content_msgcontent", "人脉首页-搜索-标签列表-点击进入群聊-人群按钮-消息输入框")
        return self.RMSY_search_label_groupchat_groupbtn_msginput

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-消息按钮
    def RMSY_search_label_groupchat_groupbtn_msgbtn(self):
        self.RMSY_search_label_groupchat_groupbtn_msgbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_to_message", "人脉首页-搜索-标签列表-点击进入群聊-人群按钮-消息按钮")
        return self.RMSY_search_label_groupchat_groupbtn_msgbtn
    #end_level_1---------------------------------------------------人群按钮所有元素定位完毕------------------------------------------------------








