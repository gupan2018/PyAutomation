__author__ = 'Administrator'
import re
import urllib.request

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

for page in range(0, 13):
    page_str = 'p=%s'%(page,)
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&sm=0&"
    url = url + page_str
    req = urllib.request.Request(url, headers = headers)#关键步骤

    response = urllib.request.urlopen(req)
    result = response.read()
    result = result.decode("utf-8")

    #.代表匹配任意一个字符，*代表匹配多次，()中为要匹配的字符串
    com_name = r'.htm" target="_blank">(.*)</a></td>'#字符串前面带r，告诉编译器这个字符串不转义
    wordre = re.compile(com_name)
    list = wordre.findall(result)
    print(list)
