__author__ = 'Administrator'
import urllib.request
import configparser

class Http:
    def __init__(self, path):
        self.conf = configparser.ConfigParser()
        self.conf.read(path)
        self.__headers = eval(self.conf.get("msg", "headers"))

    def get_result(self, url):
        if (url == ''):
            print("无效的url")
            return False
        req = urllib.request.Request(url, headers=self.__headers)
        response = urllib.request.urlopen(req)
        result = response.read()
        result = result.decode("utf-8")
        return result
