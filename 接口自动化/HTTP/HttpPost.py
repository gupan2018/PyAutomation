__author__ = 'Administrator'
import urllib.request
import urllib.parse

url = "http://v.juhe.cn/laohuangli/d"
data = {
    "key":"a8f2732319cf0ad3cce8ec6ef7aa4f33",
        "date":"2017-09-23"
}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')#区别于Get请求的地方，不加会报错
req = urllib.request.Request(url, data)

response = urllib.request.urlopen(req)
result = response.read()
result = result.decode('utf-8')

import json
print(type(result)) #判断response数据类型

result = json.loads(result)#将response数据类型由str类型转换为dic类型
print(type(result))

result = json.dumps(result)#将response数据类型由dic类型转换为str类型
print(type(result))