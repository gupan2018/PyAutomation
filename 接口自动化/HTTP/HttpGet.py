__author__ = 'Administrator'

#第一种引入模块的方式
import urllib.request
'''
url_1 = "https://www.baidu.com/?tn=98010089_dg&ch=7"
response_1 = urllib.request.urlopen(url_1)
#打印返回的状态码
print("返回的状态码是：", response_1.getcode())

#读取返回报文内容
result = response_1.read()
result = result.decode("utf-8")
print(result)

#读取返回的头部信息
print(response_1.getheaders())
'''

#第二种引入模块的方式
'''
from urllib import request
url_2 = "https://www.baidu.com/?tn=98010089_dg&ch=7"
response_2 = request.urlopen(url_2)
print("返回的状态码是：", response_2.getcode())
'''

'''
url_lhl = "http://v.juhe.cn/laohuangli/d?date=2017-09-11&key=a8f2732319cf0ad3cce8ec6ef7aa4f33"
response = urllib.request.urlopen(url_lhl)
result = response.read() #读取返回的内容
result = result.decode("utf-8") #将返回结果转化为utf-8编码格式
print(result)
'''

import urllib.parse
url = "http://v.juhe.cn/laohuangli/d"
data = {
    "key":"a8f2732319cf0ad3cce8ec6ef7aa4f33",
        "date":"2017-09-23"
}

data = urllib.parse.urlencode(data) #把字典转化为字符串形式
print(data)


url = url + "?" + data

response = urllib.request.urlopen(url)

print(response.getcode())

result = response.read()
result = result.decode("utf-8")
print(result)
