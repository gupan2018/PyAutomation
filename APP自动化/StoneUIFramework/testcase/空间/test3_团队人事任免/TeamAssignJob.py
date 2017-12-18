__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo

#团队人事任免
class TeamAssignJob:
    def __init__(self):#初始化测试数据
        d = DataInfo()#创建DataInfo()对象
        self.spacename = d.cell("test003",2,1)#测试空间123
        self.AdministratorLoc = int(d.cell("test003",2,2))#管理员编辑
        self.SalespersonLoc = int(d.cell("test003",2,2))#销售员编辑
        self.AssistantLoc = int( d.cell("test003",2,4))#行政助理编辑
        self.AdmNum = int(d.cell("test003",2,5))#管理员人数
        self.SalNum = int(d.cell("test003",2,6))#销售员人数
        self.AssNum = int(d.cell("test003",2,7))#行政助理人数
        self.Name = d.cell("test003",2,8)#肖静远
        self.Director =  int(d.cell("test003",2,9))#董事会
        self.Marketing =  int(d.cell("test003",2,10))#营销部
        self.HR =  int(d.cell("test003",2,11))#人事部
    def teamAssignJob(self,driver):
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_OrgSpaceTeamHandle公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
        #1.空间首页
            # handle.Kjlb_click()
            # tools.getScreenShot(screen_path,"空间首页")
        #2.选择空间:测试空间123
            # handle.Kjlb_browseorgspaceByName_click(self.spacename)
        #3.右上角:菜单栏选择团队
            handle.Kjlb_browseorgspace_menu_click()#右上角菜单
            handle.Kjlb_browseorgspace_menu_team_click()#点击团队
        #4.团队编辑，编辑各职位人数
            #4.1 管理员人数:2人
            handle.Kjlb_browseorgspace_menu_team_teamedit_click()#点击编辑
            # handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.AdministratorLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[0].click()

            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit().clear()#清空
            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self.AdmNum)#2人
            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm_click()#点击是
            #4.2 销售员人数:3人
            # handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.SalespersonLoc)#编辑销售员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[1].click()

            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit().clear()#清空
            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self.SalNum)#3人
            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm_click()#点击是
            #4.3 行政助理人数:4人
            # handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.AssistantLoc)#编辑助理人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[3].click()

            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit().clear()#清空
            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self.AssNum)#4人
            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm_click()#点击是
        #5.检查各职位人数是否保存生效
            #5.1 检查管理员人数编辑是否生效
            # handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.AdministratorLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[0].click()

            AdmNumm = int(handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit().text)
            assert self.AdmNum == AdmNumm,"编辑管理员人数保存后未生效"
            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel_click()#点击否
            #5.2 检查销售员人数编辑是否生效
            # handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.SalespersonLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[1].click()

            SalNum = int(handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit().text)
            assert self.SalNum == SalNum,"编辑销售员人数保存后未生效"
            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel_click()#点击否
            #5.3 检查行政助理人数编辑是否生效
            # handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.AssistantLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[3].click()

            AssNum = int(handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit().text)
            assert self.AssNum == AssNum,"编辑管理员人数后未生效"
            handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel_click()#点击否
        #6.关闭编辑
            handle.Kjlb_browseorgspace_menu_team_teamedit_click()#点击编辑按钮
        #7.菜单栏-人事任免
            handle.Kjlb_browseorgspace_menu_team_menu_click()#点击菜单栏
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_click()#点击人事任免
            if driver.find_elements_by_id("com.yunlu6.stone:id/removaljobs_name") != []:#列表是否为空
                listT = handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact()
                for i in range(len(listT)):#遍历列表
                    if handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact()[i].text == self.Name:#再判断是否该人已被任免
                        handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_click(0)#待任免联系人
                        handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_delete_click()#点击移除
                    else :
                        pass
            else:
                pass
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_click()#点击人事任免新增按钮
        #8.搜索姓名:肖静远
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_search_sendkeys(self.Name)#搜索关键字
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_searchbtn_click()#点击搜索
        #9.点击搜索的结果,添加
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_choose_click(0)#勾选
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_confirm_click()#添加
        #10.待任免列表点击联系人-任免职位-勾选-返回
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_click(0)#待任免联系人
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_department_click(self.Director)#董事会
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_jobname_click(0)#董事长
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_confrim_click()#勾选
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_back_click()#返回
            name = driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_name")[0].text#获取董事长姓名
            assert self.Name == name,"董事长任免失败"
        #11.移除任免,还原
            handle.Kjlb_browseorgspace_menu_team_menu_click()#点击菜单栏
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_click()#点击人事任免
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_click(0)#待任免联系人
            handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_delete_click()#点击移除
        except Exception as err:
            logging.error("Error Information TeamAssignJob Inside : %s"%err)
            raise err