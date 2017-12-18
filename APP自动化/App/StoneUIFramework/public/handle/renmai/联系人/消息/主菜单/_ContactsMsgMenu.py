__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.消息.主菜单._ContactsMsgMenu import _ContactsMsgMenu
from StoneUIFramework.public.handle.renmai.联系人.消息._ContactsMessage import _ContactsMessageHandle

class _ContactsMsgMenuHandle(_ContactsMsgMenu, _ContactsMessageHandle):
    #定位：人脉首页-点击联系人-消息-主菜单
    def RMSY_contacts_msg_menu_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu())

    #begin_level_1---------------------------------------------------热度设置所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置
    def RMSY_contacts_msg_menu_heatsetting_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-返回
    def RMSY_contacts_msg_menu_heatsetting_back_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_back())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-消息
    def RMSY_contacts_msg_menu_heatsetting_msg_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_msg())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-飘泡
    def RMSY_contacts_msg_menu_heatsetting_bubble_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_bubble())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-震动
    def RMSY_contacts_msg_menu_heatsetting_shock_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_shock())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-铃声
    def RMSY_contacts_msg_menu_heatsetting_bell_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_bell())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-确定
    def RMSY_contacts_msg_menu_heatsetting_confirm_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_confirm())

    #begin_level_2-------------------------------------------周期所有元素定位------------------------------------------
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期
    def RMSY_contacts_msg_menu_heatsetting_period_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-返回
    def RMSY_contacts_msg_menu_heatsetting_period_back_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_back())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-每天
    def RMSY_contacts_msg_menu_heatsetting_period_everyday_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_everyday())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-工昨日
    def RMSY_contacts_msg_menu_heatsetting_period_workday_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_workday())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-节假日
    def RMSY_contacts_msg_menu_heatsetting_period_holiday_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_holiday())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-择日
    def RMSY_contacts_msg_menu_heatsetting_period_selectday_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_selectday())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-保存
    def RMSY_contacts_msg_menu_heatsetting_period_save_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_save())

    #end_level_2------------------------------------------周期所有元素定位完毕------------------------------------------

    #begin_level_2-------------------------------------------时段所有元素定位------------------------------------------
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段
    def RMSY_contacts_msg_menu_heatsetting_time_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_time())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段-确定
    def RMSY_contacts_msg_menu_heatsetting_time_confirm_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_time_confirm())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段-取消
    def RMSY_contacts_msg_menu_heatsetting_time_cancel_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_time_cancel())
    #end_level_2-------------------------------------------时段所有元素定位完毕------------------------------------------
    #end_level_1---------------------------------------------------热度设置所有元素定位完毕------------------------------------------------------