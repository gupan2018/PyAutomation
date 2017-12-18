__author__ = 'Administrator'
from selenium import webdriver
'''
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["--ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)
'''
browser = webdriver.Chrome()
browser.get("http:\\www.baidu.com")

