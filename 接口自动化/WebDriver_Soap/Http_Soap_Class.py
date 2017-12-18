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

class HttpPost:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read(path)
        self.url = conf.get("url", "Http_url")
        key = conf.get("HttpData", "key")
        date = conf.get("HttpData", "date")
        self.data = {"key":key, "date":date}

    def Req(self):
        data = urllib.parse.urlencode(self.data)
        data = data.encode('utf-8')
        try:
            req = urllib.request.Request(self.url, data)
            response = urllib.request.urlopen(req)
            response = response.read()
            response = response.decode('utf-8')

            response = json.loads(response)#将response数据类型由str类型转换为dic类型
            print(type(response), response)
            response = json.dumps(response)#将response数据类型由dic类型转换为str类型
            print(type(response), response)
        except Exception:
            print("HttpPost请求错误")

class Soap:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read(path)
        self.url = conf.get("url", "Soap_url")
        client_ip = conf.get("SoapData", "client_ip")
        mobile = conf.get("SoapData", "mobile")
        tmpl_id = conf.get("SoapData", "tmpl_id")
        self.data = {"client_ip":client_ip, "mobile":mobile, "tmpl_id":tmpl_id}

    def Req(self):
        client = Client(self.url)
        try:
            res = client.service.sendMCode(self.data)
            print(res)
        except Exception:
            print("Soap接口调用错误")