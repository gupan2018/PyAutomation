__author__ = 'xiaoj'
import unittest
import time
from StoneUIFramework.public.common.HTMLTestRunner import HTMLTestRunner
from StoneUIFramework.config.globalparam import GlobalParam

#以下导入各模块测试用例
from StoneUIFramework.testcase.空间.test1_创建机构空间.创建机构空间001 import space_Create

#控制用例跑的次数，死循环，可人工干预退出
if __name__ == '__main__':
    a = 1
    while a == 1:
        suite = unittest.TestSuite()#创建一个测试集，把所有要跑的测试用例跑动起来

        #----------------------------------云库----------------------------------
        # suite.addTest(yunku_ShangChuan("test_shangchuan"))#云库上传
        # suite.addTest(yunku_ShangChuan("test_shangchuan"))#云库上传

        # suite.addTest(yunku_FenLei("test_fenlei"))#云库分类到产品库
        # suite.addTest(yunku_GongSi("test_gongsi"))#云库分类到公司档
        # suite.addTest(yunku_Edit("test_edit"))#云库编辑图片信息

        #----------------------------------人脉----------------------------------
        # suite.addTest(contact_Add("test_addContact"))#人脉添加
        # suite.addTest(contact_Browse("test_borwseContact"))#人脉浏览
        # suite.addTest(contact_Del("test_delContact"))#人脉删除——— 需要手动从黑名单中删除
        # suite.addTest(contact_Exc("test_excContact"))#人脉换名片
        # suite.addTest(contact_Label("test_labelContact"))#打标签

        # runner = unittest.TextTestRunner()
        # runner.run(suite)

        #----------------------------------空间----------------------------------
        suite.addTest(space_Create("test_spacecreate"))#创建机构空间

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
        break




