__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.主菜单._ContactsMenu import _ContactsMenu

class _HeatSetting(_ContactsMenu):
    #定位：人脉首页-点击联系人-打开主菜单-热度设置
    def RMSY_contacts_menu_heatsetting(self):
        self.RMSY_contacts_menu_heatsetting = self.p.get_element("id->com.yunlu6.stone:id/anti", "人脉首页-点击联系人-打开主菜单-热度设置")
        return self.RMSY_contacts_menu_heatsetting

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-全部打开
    def RMSY_contacts_menu_heatsetting_openall(self):
        self.RMSY_contacts_menu_heatsetting_openall = self.p.get_element("id->com.yunlu6.stone:id/sb_all", "人脉首页-点击联系人-打开主菜单-热度设置-全部打开")
        return self.RMSY_contacts_menu_heatsetting_openall

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-响铃图形
    def RMSY_contacts_menu_heatsetting_bellgraph(self):
        self.RMSY_contacts_menu_heatsetting_bellgraph = self.p.get_element("id->com.yunlu6.stone:id/sb_conversation", "人脉首页-点击联系人-打开主菜单-热度设置-响铃图形")
        return self.RMSY_contacts_menu_heatsetting_bellgraph

    #begin_level_1---------------------------------------------------一对一会话所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话
    def RMSY_contacts_menu_heatsetting_p2pconversation(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation = self.p.get_element("id->com.yunlu6.stone:id/rl_conversation", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-返回
    def RMSY_contacts_menu_heatsetting_p2pconversation_back(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-返回")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_back

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-消息
    def RMSY_contacts_menu_heatsetting_p2pconversation_msg(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_msg = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_msg", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-消息")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_msg

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-飘泡
    def RMSY_contacts_menu_heatsetting_p2pconversation_bubble(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_bubble = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_pop", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-飘泡")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_bubble

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-震动
    def RMSY_contacts_menu_heatsetting_p2pconversation_shock(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_shock = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_shock", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-震动")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_shock

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-铃声
    def RMSY_contacts_menu_heatsetting_p2pconversation_bell(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_bell = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_bell", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-铃声")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_bell

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-确定
    def RMSY_contacts_menu_heatsetting_p2pconversation_confirm(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_confirm = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_ok", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-确定")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_confirm

    #begin_level_2-------------------------------------------周期所有元素定位------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期
    def RMSY_contacts_menu_heatsetting_p2pconversation_period(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_period = self.p.get_element("id->android.widget.ImageView", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_period

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

    #end_level_2------------------------------------------周期所有元素定位完毕------------------------------------------

    #begin_level_2-------------------------------------------时段所有元素定位------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段
    def RMSY_contacts_menu_heatsetting_p2pconversation_time(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_time = self.p.get_element("id->com.yunlu6.stone:id/im_add_time", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_time

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-确定
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_ok", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-确定")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-取消
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_cancel", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-确定")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel
    #end_level_2-------------------------------------------时段所有元素定位完毕------------------------------------------
    #end_level_1---------------------------------------------------一对一会话所有元素定位完毕------------------------------------------------------