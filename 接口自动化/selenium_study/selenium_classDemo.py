__author__ = 'Administrator'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
action_kw = browser.find_element_by_xpath(".//*[@id='kw']")

action_kw.send_keys("柠檬班")
action_kw.send_keys(Keys.ENTER)
time.sleep(5)
browser.quit()
