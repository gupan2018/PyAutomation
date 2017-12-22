# -*- coding:utf-8 -*-
# __author__ = 'gupan'
from core.pages.basePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, selenium_driver, base_url):
        super(LoginPage, self).__init__(selenium_driver, base_url)

        self.username_loc = (By.XPATH, "html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[2]/input")
        self.password_loc = (By.XPATH, "html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[3]/input")
        self.submit_loc = (By.XPATH, "html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[7]/div[1]/a[1]")

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()