__author__ = 'Administrator'
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http:\\www.qian100.com")
browser.implicitly_wait(10)#隐式等待

locator = (By.XPATH, "html/body/div[1]/div/div[2]/ul/li[6]/a")
try:
    WebDriverWait(browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator))
except TimeoutError as e:
    print(e)
finally:
    browser.close()