__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.联系人.主菜单.热度设置._HeatSetting import _HeatSetting
from StoneUIFramework.public.handle.renmai.联系人.主菜单._ContactsMenu import _ContactsMenuHandle

class _HeatSettingHandle(_HeatSetting, _ContactsMenuHandle):
    #定位：人脉首页-点击联系人-打开主菜单-热度设置
    def RMSY_contacts_menu_heatsetting_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-全部打开
    def RMSY_contacts_menu_heatsetting_openall_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_openall())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-响铃图形
    def RMSY_contacts_menu_heatsetting_bellgraph_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_bellgraph())

    #begin_level_1---------------------------------------------------一对一会话所有元素定位------------------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话
    def RMSY_contacts_menu_heatsetting_p2pconversation_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-返回
    def RMSY_contacts_menu_heatsetting_p2pconversation_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_back())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-消息
    def RMSY_contacts_menu_heatsetting_p2pconversation_msg_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_msg())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-飘泡
    def RMSY_contacts_menu_heatsetting_p2pconversation_bubble_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_bubble())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-震动
    def RMSY_contacts_menu_heatsetting_p2pconversation_shock_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_shock())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-铃声
    def RMSY_contacts_menu_heatsetting_p2pconversation_bell_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_bell())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-确定
    def RMSY_contacts_menu_heatsetting_p2pconversation_confirm_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_confirm())

    #begin_level_2-------------------------------------------周期所有元素定位------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-返回
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_back())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-每天
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_everyday_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_everyday())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-工昨日
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_workday_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_workday())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-节假日
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_holiday_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_holiday())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-择日
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_selectday_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_selectday)

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-保存
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_save_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_save())

    #end_level_2------------------------------------------周期所有元素定位完毕------------------------------------------

    #begin_level_2-------------------------------------------时段所有元素定位------------------------------------------
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_time)

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-确定
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-取消
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel())
    #end_level_2-------------------------------------------时段所有元素定位完毕------------------------------------------
    #end_level_1---------------------------------------------------一对一会话所有元素定位完毕------------------------------------------------------