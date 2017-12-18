__author__ = 'Administrator'
import json
import urllib.parse
import urllib.request
from suds.client import Client
import configparser

class HttpGet:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read(path)
        self.url = conf.get("url", "Http_url")
        key = conf.get("HttpData", "key")
        date = conf.get("HttpData", "date")
        self.data = {"key":key, "date":date}

    def Req(self):
        self.data = urllib.parse.urlencode(self.data)
        url = self.url + "?" + self.data
        try:
            response = urllib.request.urlopen(url)
            response = response.read().decode("utf-8")
            print(response)
        except Exception:
            print("HttpGet请求错误")