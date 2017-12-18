__author__ = 'Administrator'
import time
from selenium.webdriver.common.action_chains import ActionChains

class Qian100:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def openWeb(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(30)

    def login(self):
        self.browser.find_element_by_xpath("html/body/div[1]/div/div[2]/ul/li[6]/a").click()

        telphone = self.browser.find_element_by_id("PhoneNum")
        telphone.send_keys("18813989449")

        pwd = self.browser.find_element_by_id("PassWord")
        pwd.send_keys("nick1234")

        submit = self.browser.find_element_by_xpath(".//*[@id='FastLoginDiv']/table/tbody/tr[8]/td/dl/dd/div")
        submit.click()
        time.sleep(5)

    def adFree(self):
        ad = self.browser.find_element_by_xpath(".//*[@id='DialogDiv']/div/div[1]")
        ad.click()
        time.sleep(5)

    def performAccount(self):
        myAaccount = self.browser.find_element_by_link_text("我的账户")
        ActionChains(self.browser).move_to_element(myAaccount).perform()
        time.sleep(5)

    def aquireAccountList(self):
        return self.browser.find_elements_by_xpath("html/body/div[2]/div[2]/div/div[2]/div/ul/li")

    def traverseAccount(self):
        accountList = self.aquireAccountList()
        len_list = len(accountList)
        for i in range(0, len_list):
            #self.adFree()
            self.performAccount()
            accountList = self.aquireAccountList()
            accountList[i].click()
            time.sleep(5)
            self.browser.back()
            time.sleep(5)