# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

class Qian100(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.base_url = "https://www.qian100.com/"
    
    def test_qian100(self):
        driver = self.driver
        driver.get(self.base_url + "/Home/Index")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("PhoneNum").send_keys("18813989449")
        driver.find_element_by_id("PassWord").send_keys("nick1234")
        driver.find_element_by_css_selector("dd.login_input > div").click()
        #time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    unittest.main()
