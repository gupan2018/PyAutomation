__author__ = 'Administrator'
import urllib.request
import http.cookiejar

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
#response = opener.open('http://www.baidu.com')
response = urllib.request.urlopen('http://www.baidu.com')
print(cookie)
for i in cookie:
    print(i.name + "=" + i.value)


