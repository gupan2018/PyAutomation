__author__ = 'Administrator'
from configparser import ConfigParser
from appium import webdriver
import time

conf = ConfigParser()
conf.read("app.conf")
desired_caps_right = eval(conf.get("app", "desired_caps_right"))

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps_right)
driver.quit()
#time.sleep(10)
#try:
    #res = driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon").is_displayed()
    #print("不存在的元素", res)
    #if res == []:
        #print("不存在的元素")


    #res = driver.find_elements_by_id("com.yunlu6.stone:id/main_login")
    #print("存在的元素", res)
    #time.sleep(2)
#except Exception as err:
    #print(err)
#finally:
    #driver.quit()
    #print(driver)

'''
driver.find_element_by_id("com.yunlu6.stone:id/start_buildstone").click()
time.sleep(2)
driver.find_element_by_class_name("android.widget.RelativeLayout")[1].click()
time.sleep(10)
'''
'''
driver.find_element_by_name("1").click()
driver.find_element_by_name("2").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("1").click()
driver.find_element_by_name("1").click()
#这里需要所有的id，并不是向monkeyrunner一样只去冒号后的值，
driver.find_element_by_id("com.ibox.calculators:id/digit7").click()
driver.find_element_by_name("=").click()
'''
#driver.quit()