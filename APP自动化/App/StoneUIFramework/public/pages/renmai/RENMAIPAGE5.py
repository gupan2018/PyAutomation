__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.RENMAIPAGE4 import _RENMAIPAGE4

class _RENMAIPAGE5(_RENMAIPAGE4):
#*********************************【PAGE3】人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置：RMSY_search_label_groupchat_menu_setting*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像
    def RMSY_search_label_groupchat_menu_setting_grouphead(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead = self.p.get_element("id->com.yunlu6.stone:id/rl_img", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-返回
    def RMSY_search_label_groupchat_menu_setting_back(self):
        self.RMSY_search_label_groupchat_menu_setting_back = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-返回")
        return self.RMSY_search_label_groupchat_menu_setting_back

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称
    def RMSY_search_label_groupchat_menu_setting_groupname(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname = self.p.get_element("id->com.yunlu6.stone:id/rl_group_name", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称")
        return self.RMSY_search_label_groupchat_menu_setting_groupname

#*********************************【PAGE3】人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置：RMSY_search_label_groupchat_menu_heatsetting*********************************
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

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期
    def RMSY_search_label_groupchat_menu__heatsetting_period(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period = self.p.get_element("id->android.widget.ImageView", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段
    def RMSY_search_label_groupchat_menu__heatsetting_time(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_time = self.p.get_element("id->com.yunlu6.stone:id/im_add_time", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段")
        return self.RMSY_search_label_groupchat_menu__heatsetting_time

#*********************************【PAGE3】人脉首页-搜索-标签列表-点击进入群聊-人群按钮：RMSY_search_label_groupchat_groupbtn*********************************
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

#*********************************【PAGE3】人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期：RMSY_contacts_menu_heatsetting_p2pconversation_period*********************************
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-返回
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_back(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_period_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-返回")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_period_back

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-每天
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_everyday(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_period_everyday = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_allday", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-每天")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_period_everyday

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-工昨日
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_workday(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_period_workday = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_workday", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-工昨日")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_period_workday

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-节假日
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_holiday(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_period_holiday = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_holiday", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-节假日")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_period_holiday

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-择日
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_selectday(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_period_selectday = self.p.get_element("id->com.yunlu6.stone:id/im_add_days", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-择日")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_period_selectday

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-保存
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_save(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_period_save = self.p.get_element("id->com.yunlu6.stone:id/btn_messagetime_save", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-保存")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_period_save

#*********************************【PAGE3】人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段：RMSY_contacts_menu_heatsetting_p2pconversation_time*********************************
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-确定
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_ok", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-确定")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-取消
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_cancel", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-确定")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel

#*********************************【PAGE3】人脉首页-点击联系人-消息-主菜单-热度设置-周期：RMSY_contacts_msg_menu_heatsetting_period*********************************
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-返回
    def RMSY_contacts_msg_menu_heatsetting_period_back(self):
        self.RMSY_contacts_msg_menu_heatsetting_period_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-点击联系人-消息-主菜单-热度设置-周期-返回")
        return self.RMSY_contacts_msg_menu_heatsetting_period_back

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-每天
    def RMSY_contacts_msg_menu_heatsetting_period_everyday(self):
        self.RMSY_contacts_msg_menu_heatsetting_period_everyday = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_allday", "人脉首页-点击联系人-消息-主菜单-热度设置-周期-每天")
        return self.RMSY_contacts_msg_menu_heatsetting_period_everyday

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-工昨日
    def RMSY_contacts_msg_menu_heatsetting_period_workday(self):
        self.RMSY_contacts_msg_menu_heatsetting_period_workday = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_workday", "人脉首页-点击联系人-消息-主菜单-热度设置-周期-工昨日")
        return self.RMSY_contacts_msg_menu_heatsetting_period_workday

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-节假日
    def RMSY_contacts_msg_menu_heatsetting_period_holiday(self):
        self.RMSY_contacts_msg_menu_heatsetting_period_holiday = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_holiday", "人脉首页-点击联系人-消息-主菜单-热度设置-周期-节假日")
        return self.RMSY_contacts_msg_menu_heatsetting_period_holiday

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-择日
    def RMSY_contacts_msg_menu_heatsetting_period_selectday(self):
        self.RMSY_contacts_msg_menu_heatsetting_period_selectday = self.p.get_element("id->com.yunlu6.stone:id/im_add_days", "人脉首页-点击联系人-消息-主菜单-热度设置-周期-择日")
        return self.RMSY_contacts_msg_menu_heatsetting_period_selectday

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-保存
    def RMSY_contacts_msg_menu_heatsetting_period_save(self):
        self.RMSY_contacts_msg_menu_heatsetting_period_save = self.p.get_element("id->com.yunlu6.stone:id/btn_messagetime_save", "人脉首页-点击联系人-消息-主菜单-热度设置-周期-保存")
        return self.RMSY_contacts_msg_menu_heatsetting_period_save

#*********************************【PAGE4】人脉首页-点击联系人-消息-主菜单-热度设置-时段：RMSY_contacts_msg_menu_heatsetting_time*********************************
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段-确定
    def RMSY_contacts_msg_menu_heatsetting_time_confirm(self):
        self.RMSY_contacts_msg_menu_heatsetting_time_confirm = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_ok", "人脉首页-点击联系人-消息-主菜单-热度设置-时段-确定")
        return self.RMSY_contacts_msg_menu_heatsetting_time_confirm

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段-取消
    def RMSY_contacts_msg_menu_heatsetting_time_cancel(self):
        self.RMSY_contacts_msg_menu_heatsetting_time_cancel = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_cancel", "人脉首页-点击联系人-消息-主菜单-热度设置-时段-确定")
        return self.RMSY_contacts_msg_menu_heatsetting_time_cancel