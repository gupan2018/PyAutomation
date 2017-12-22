# -*- coding:utf-8 -*-
# __author__ = 'gupan'


class BasePage(object):
    '''
    基本类，所有页面父类
    __init__(self, selenium_driver, base_url):
        初始化函数，传入driver, base_url，做初始化操作

    on_page(self, target_url):
        判断是否在当前页面

    _open(self, url):
        打开页面

    open(self, url):
        封装了打开页面的操作

    find_element(self, *loc):
        封装定位元素操作（单个元素）

    find_elements(self, *loc):
        封装定位元素操作（多个元素）
    '''
    def __init__(self, selenium_driver, base_url):
        super(BasePage, self).__init__()
        self.driver = selenium_driver
        self.base_url = base_url

    def on_page(self, target_url):
        return self.driver.current_url == target_url

    def _open(self, url):
        target_url = self.base_url + url
        self.driver.get(target_url)
        assert self.on_page(target_url), 'Did not land on %s' % target_url

    def open(self, url):
        self._open(url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)