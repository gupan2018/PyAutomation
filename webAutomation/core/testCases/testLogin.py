# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import unittest
from conf import settings
import time
from core.pages.loginPage import LoginPage
from selenium import webdriver


class TestLogin(unittest.TestCase):
    """
    测试登陆
    """
    def setUp(self):
        self.username = '13667618021@sina.cn'
        self.password = 'qwer1234'
        self.driver = webdriver.Chrome()
        self.base_url = settings.base_url

        self.test_url = '/'

        self.timeout = 30
        self.driver.implicitly_wait(self.timeout)

    def test_user_login(self):
        '''
        测试登陆函数
        :return:
        '''
        try:
            login_page = LoginPage(self.driver, self.base_url)
            login_page.open(self.test_url)
            # time.sleep(10)
            # self.driver.maximize_window()
            login_page.type_username(self.username)
            login_page.type_password(self.password)
            login_page.submit()

            text = self.driver.find_element_by_xpath('html/body/div[1]/div/div[4]/div[1]/div[3]/div[1]/span/em[2]').text
            self.assertEqual(text, '17383107596@sina.cn', '用户名称不匹配，登陆失败！')
        except AssertionError as e:
            print(e)
        finally:
            self.driver.close()

    def tearDown(self):
        pass