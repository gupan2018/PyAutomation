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
    #对象初始化时，获取配置文件中的参数（服务器IP地址、端口号、测试模块url等）
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read(path)
        self.__req_host = conf.get("register", "host")
        self.__req_port = conf.get("register", "port")
        self.__req_url = conf.get("register", "url")
        req_data = conf.get("register", "data")
        self.__req_data = eval(req_data)

    #发送Get请求
    def get_req(self, test_url = "", test_data = {}):
        if test_url != "":
            self.__req_url = test_url

        if test_data != {}:
            self.__req_data = test_data

        data = urllib.parse.urlencode(self.__req_data)
        url = self.__req_host + ":" + self.__req_port + self.__req_url + "?" + data
        #print(url)
        try:
            response_get = urllib.request.urlopen(url)
        except Exception as e:
            print(e)

        result = response_get.read()
        result = result.decode("utf-8")

        #将请求结果转化为Json格式，并将请求结果作为返回参数，便于调用
        result = json.loads(result)
        return result

    #发送POST请求
    def post_req(self, test_url = "", test_data = {}):
        if test_url != "":
            self.__req_url = test_url

        if test_data != {}:
            self.__req_data = test_data

        data = urllib.parse.urlencode(self.__req_data)
        data = data.encode("utf-8")
        url = self.__req_host + ":" + self.__req_port + self.__req_url
        request = urllib.request.Request(url, data)
        try:
            response_post = urllib.request.urlopen(request)
        except Exception as e:
            print(e)

        result = response_post.read()
        result = result.decode("utf-8")
        result = json.loads(result)
        return result