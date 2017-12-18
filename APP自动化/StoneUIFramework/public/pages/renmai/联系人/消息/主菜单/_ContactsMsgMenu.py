__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息._ContactsMessage import _ContactsMessage

class _ContactsMsgMenu(_ContactsMessage):
    #定位：人脉首页-点击联系人-消息-主菜单
    def RMSY_contacts_msg_menu(self):
        self.RMSY_contacts_msg_menu = self.p.get_element("id->com.yunlu6.stone:id/title_main_fl_more_menu", "人脉首页-点击联系人-消息-主菜单")
        return self.RMSY_contacts_msg_menu

    #begin_level_1---------------------------------------------------热度设置所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置
    def RMSY_contacts_msg_menu_heatsetting(self):
        self.RMSY_contacts_msg_menu_heatsetting = self.p.get_element("id->com.yunlu6.stone:id/rl_msgsetting", "人脉首页-点击联系人-消息-主菜单-热度设置")
        return self.RMSY_contacts_msg_menu_heatsetting

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-返回
    def RMSY_contacts_msg_menu_heatsetting_back(self):
        self.RMSY_contacts_msg_menu_heatsetting_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-点击联系人-消息-主菜单-热度设置-返回")
        return self.RMSY_contacts_msg_menu_heatsetting_back

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-消息
    def RMSY_contacts_msg_menu_heatsetting_msg(self):
        self.RMSY_contacts_msg_menu_heatsetting_msg = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_msg", "人脉首页-点击联系人-消息-主菜单-热度设置-消息")
        return self.RMSY_contacts_msg_menu_heatsetting_msg

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-飘泡
    def RMSY_contacts_msg_menu_heatsetting_bubble(self):
        self.RMSY_contacts_msg_menu_heatsetting_bubble = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_pop", "人脉首页-点击联系人-消息-主菜单-热度设置-飘泡")
        return self.RMSY_contacts_msg_menu_heatsetting_bubble

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-震动
    def RMSY_contacts_msg_menu_heatsetting_shock(self):
        self.RMSY_contacts_msg_menu_heatsetting_shock = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_shock", "人脉首页-点击联系人-消息-主菜单-热度设置-震动")
        return self.RMSY_contacts_msg_menu_heatsetting_shock

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-铃声
    def RMSY_contacts_msg_menu_heatsetting_bell(self):
        self.RMSY_contacts_msg_menu_heatsetting_bell = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_bell", "人脉首页-点击联系人-消息-主菜单-热度设置-铃声")
        return self.RMSY_contacts_msg_menu_heatsetting_bell

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-确定
    def RMSY_contacts_msg_menu_heatsetting_confirm(self):
        self.RMSY_contacts_msg_menu_heatsetting_confirm = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_ok", "人脉首页-点击联系人-消息-主菜单-热度设置-确定")
        return self.RMSY_contacts_msg_menu_heatsetting_confirm

    #begin_level_2-------------------------------------------周期所有元素定位------------------------------------------
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期
    def RMSY_contacts_msg_menu_heatsetting_period(self):
        self.RMSY_contacts_msg_menu_heatsetting_period = self.p.get_element("id->android.widget.ImageView", "人脉首页-点击联系人-消息-主菜单-热度设置-周期")
        return self.RMSY_contacts_msg_menu_heatsetting_period

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

    #end_level_2------------------------------------------周期所有元素定位完毕------------------------------------------

    #begin_level_2-------------------------------------------时段所有元素定位------------------------------------------
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段
    def RMSY_contacts_msg_menu_heatsetting_time(self):
        self.RMSY_contacts_msg_menu_heatsetting_time = self.p.get_element("id->com.yunlu6.stone:id/im_add_time", "人脉首页-点击联系人-消息-主菜单-热度设置-时段")
        return self.RMSY_contacts_msg_menu_heatsetting_time

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段-确定
    def RMSY_contacts_msg_menu_heatsetting_time_confirm(self):
        self.RMSY_contacts_msg_menu_heatsetting_time_confirm = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_ok", "人脉首页-点击联系人-消息-主菜单-热度设置-时段-确定")
        return self.RMSY_contacts_msg_menu_heatsetting_time_confirm

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段-取消
    def RMSY_contacts_msg_menu_heatsetting_time_cancel(self):
        self.RMSY_contacts_msg_menu_heatsetting_time_cancel = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_cancel", "人脉首页-点击联系人-消息-主菜单-热度设置-时段-确定")
        return self.RMSY_contacts_msg_menu_heatsetting_time_cancel
    #end_level_2-------------------------------------------时段所有元素定位完毕------------------------------------------
    #end_level_1---------------------------------------------------热度设置所有元素定位完毕------------------------------------------------------