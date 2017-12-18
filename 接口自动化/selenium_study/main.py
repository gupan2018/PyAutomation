__author__ = 'Administrator'
'''
1. 登录网址：www.qian100.com
    登录用户名：18813989449
    密码：nick1234
2. 要求完成我的账户下的四个下拉框的循环点击操作
3. 利用selenium ide录制登录点击自动化代码，并且进行一定的优化
'''
from selenium import webdriver
from qian100 import Qian100

if __name__ == "__main__":
    browser = webdriver.Chrome()
    browser.maximize_window()

    op = Qian100(browser, "http:\\www.qian100.com")
    op.openWeb()
    op.login()
    op.traverseAccount()

    browser.quit()