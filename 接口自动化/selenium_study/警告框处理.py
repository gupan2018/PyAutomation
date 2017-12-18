__author__ = 'Administrator'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
browser.implicitly_wait(10)
setting_link = browser.find_element_by_link_text(u"设置")
ActionChains(browser).move_to_element(setting_link).perform()
test_list = browser.find_element_by_class_name("setpref").click()
browser.find_element_by_css_selector(".prefpanelgo").click()
browser.switch_to_alert().accept()

browser.quit()