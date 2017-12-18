__author__ = 'Administrator'
from StoneUIFramework.public.common.LoginApp import LoginApp
from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.handle.renmai.RENMAIHANDLE3 import _RENMAIHANDLE3
from StoneUIFramework.public.common.basepage import Page
from time import sleep

if __name__ == "__main__":
    cnn = Connect()
    driver = cnn.connect()
    LoginApp().loginapp(driver, "space")

    sleep(2)
    handle = _RENMAIHANDLE3(driver)
    handle.RMSY_click()
    sleep(2)
    handle.RMST_searchinput_click()
    sleep(2)
    handle.RMSY_search_label_click(0)
    sleep(2)
    handle.RMSY_search_label_groupchat_click()
    sleep(2)






