__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()

browser.get("http:\\www.baidu.com")
browser.implicitly_wait(10)
browser.maximize_window()
search_handle = browser.current_window_handle
browser.find_element_by_xpath("html/body/div[2]/div[1]/div/div[3]/a[7]").click()
browser.find_element_by_xpath("html/body/div[5]/div[2]/div[2]/div/div/div/div/div/div[1]/form/p[9]/a[1]").click()
all_handles = browser.window_handles
print(all_handles)
test_handle = browser.current_window_handle
if test_handle != search_handle:
    print("not equal")
else:
    print("equal")

for handle in all_handles:
    if handle != search_handle:
        print("this is not search_handle")
        browser.switch_to_window(handle)
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/form/p[3]/input").send_keys("顾攀")
    elif handle == search_handle:
        print("this is search handle")

sleep(5)
browser.quit()