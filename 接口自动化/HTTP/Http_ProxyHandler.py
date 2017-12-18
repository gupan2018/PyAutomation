__author__ = 'Administrator'
#设置代理
#代码有问题，后面有空再看
import urllib.request
import urllib.parse

proxy_handler = urllib.request.ProxyHandler(
    {
        'http':'http://127.0.0.1:9743',
        'https':'http://127.0.0.1:9743'
    }
)

opener = urllib.request.build_opener(proxy_handler)
url = "http://v.juhe.cn/laohuangli/d"
data = {
    "key":"a8f2732319cf0ad3cce8ec6ef7aa4f33",
        "date":"2017-09-23"
}

data = urllib.parse.urlencode(data)
url = url + "?" + data
response = urllib.request.urlopen(url)

print(response.getcode())