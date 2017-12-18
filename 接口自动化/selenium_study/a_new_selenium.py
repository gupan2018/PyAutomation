__author__ = 'Administrator'
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.126.com/")
driver.maximize_window()
driver.implicitly_wait(20)
print("Before login=============")

#打印当前页面title
title = driver.title
print(title)

#打印当前页面URL
now_url = driver.current_url
print(now_url)

frame = driver.find_element_by_id("x-URS-iframe")
driver.switch_to.frame(frame)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").clear()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").send_keys("yuangunguntest")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").clear()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").send_keys("free930923")

driver.find_element_by_id("dologin").click()
#driver.switch_to.default_content()
time.sleep(5)

#driver.implicitly_wait(20)

print("After login=======================")

#再次打印当前页面title
print(driver)
title_after = driver.title

print(title_after)

#打印当前页面URL
now_url_update = driver.current_url
print(now_url_update)

#获得登陆的用户名
user = driver.find_element_by_xpath("/html/body/header/div[1]/ul[1]/li[1]/a/span[1]").text
print(user)

driver.quit()
