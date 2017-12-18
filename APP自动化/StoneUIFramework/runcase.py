__author__ = 'xiaoj'
import unittest
import time
from StoneUIFramework.public.common.HTMLTestRunner import HTMLTestRunner
from StoneUIFramework.config.globalparam import GlobalParam

#以下导入各模块测试用例
from StoneUIFramework.testcase.空间.test1_创建机构空间.CreateOrgSpace001 import space_Create
from StoneUIFramework.testcase.空间.test2_上下架产品.CreateProduct002 import space_Product
from StoneUIFramework.testcase.空间.test3_团队人事任免.TeamAssignJob003 import team_Assign
from StoneUIFramework.testcase.空间.test4_资讯.Archivies004 import space_Archivies
from StoneUIFramework.testcase.空间.test5_企业名片.BusinessCard005 import space_BusinessCard
from StoneUIFramework.testcase.空间.test6_创建私人空间.CreatePersongSpace006 import perspace_Create
from StoneUIFramework.testcase.空间.test6_1私人空间加文件夹.CreatePerSFolder006_1 import perspace_NewFloder
#控制用例跑的次数，死循环，可人工干预退出
if __name__ == '__main__':
    a = 1
    while a != 5:
        # a = a + 1
        suite = unittest.TestSuite()#创建一个测试集，把所有要跑的测试用例跑动起来

        #----------------------------------【云库-测试用例】----------------------------------
        # suite.addTest(yunku_ShangChuan("test_shangchuan"))#云库上传
        # suite.addTest(yunku_ShangChuan("test_shangchuan"))#云库上传

        # suite.addTest(yunku_FenLei("test_fenlei"))#云库分类到产品库
        # suite.addTest(yunku_GongSi("test_gongsi"))#云库分类到公司档
        # suite.addTest(yunku_Edit("test_edit"))#云库编辑图片信息

        #----------------------------------【人脉-测试用例】----------------------------------
        # suite.addTest(contact_Add("test_addContact"))#人脉添加
        # suite.addTest(contact_Browse("test_borwseContact"))#人脉浏览
        # suite.addTest(contact_Del("test_delContact"))#人脉删除——— 需要手动从黑名单中删除
        # suite.addTest(contact_Exc("test_excContact"))#人脉换名片
        # suite.addTest(contact_Label("test_labelContact"))#打标签

        #----------------------------------【空间-测试用例】----------------------------------
        suite.addTest(space_Create("test_spacecreate"))#创建机构空间
        suite.addTest(space_Product("test_spaceproduct"))#上下架产品
        suite.addTest(team_Assign("test_teamassign"))#团队人事任免
        suite.addTest(space_Archivies("test_archivies"))#资讯发布
        suite.addTest(space_BusinessCard("test_businesscard"))#编辑企业名片
        suite.addTest(perspace_Create("test_perspacecreate"))#创建私人空间
        suite.addTest(perspace_NewFloder("test_pernewfolder"))#创建私人空间文件夹


        #------------------------------测试报告----------------------------------
        cf = GlobalParam("config","report.conf")
        path = cf.getParam("report","path")#报告存储路径
        timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))#获取时间戳
        filename = path + timestr + ".html"#测试报告命名
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(
                    stream=fp,
                    title='测试结果',
                    description='测试报告'
                    )
        runner.run(suite)
        fp.close() #测试报告关闭
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        break




