__author__ = 'Administrator'
'''
1. HTTP的get和post请求，封装成HttpRequest类
2. HttpRequest类里面有一个初始化函数，引入参数host,url,port,data
3. 所有的参数host,url,port,data等都放到配置文件http.conf的[HTTP]标签里面
4. 代码完成后，创建两个对象，分别调用get与post方法
'''
import configparser
import urllib.request
import json
import urllib.parse

class HttpRequest:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read(path)
        self.reg_host = conf.get("register", "host")
        self.reg_port = conf.get("register", "port")
        self.reg_url = conf.get("register", "url")
        self.reg_data = conf.get("register", "data")
        self.reg_data = eval(self.reg_data)

    def get_req(self):
        data = urllib.parse.urlencode(self.reg_data)
        url = self.reg_host + ":" + self.reg_port + self.reg_url + "?" + data
        try:
            response_get = urllib.request.urlopen(url)
        except Exception as e:
            print(e)
        print("返回码是：", response_get.getcode())
        result = response_get.read()
        result = result.decode("utf-8")
        print(result)

    def post_req(self):
        data = urllib.parse.urlencode(self.reg_data)
        data = data.encode("utf-8")
        url = self.reg_host + ":" + self.reg_port + self.reg_url
        request = urllib.request.Request(url, data)
        try:
            response_post = urllib.request.urlopen(request)
        except Exception as e:
            print(e)
        print("Post方法返回码是：", response_post.getcode())
        result = response_post.read()
        result = result.decode("utf-8")
        result = json.loads(result)
        print(result)