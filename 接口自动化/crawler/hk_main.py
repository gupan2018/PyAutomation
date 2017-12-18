__author__ = 'Administrator'
from crawler.excel_op import Excel_write
from crawler.http_request import Http
from crawler.grep_match import Grep_match
import xlwt3
'''
1. 到智联招聘网站上，搜索软件测试工程师职位
2. 匹配到所有招聘软件测试工程师的公司名称
3. 将搜索结果存储到Excel中

要求：
封装成类，最大程度提高复用性
'''
path_excel_save = 'company_name.xls'
path_http_msg = 'msg.conf'
url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&sm=0&'
grep_str = r'.htm" target="_blank">(.*)</a></td>'

if __name__ == "__main__":
    #创建一个excel表单对象
    wb_wirte = Excel_write(path_excel_save, "company_name")
    sheet = wb_wirte.getSheet()

    #创建一个Http对象用以访问浏览器
    http = Http(path_http_msg)

    for page in range(0, 13):
        #组装get请求url
        page_str = 'p=%s'%(page,)
        url_req = url + page_str

        result = http.get_result(url_req)

        #创建一个用以匹配的正则表达式对象
        grep_instance = Grep_match(grep_str, result)

        #将匹配结果以列表形式返回
        res_list = grep_instance.exec_grep()

        #将匹配结果写入Excel表格
        for i in range(0, len(res_list)):
            sheet.write(page, i, res_list[i])

    #存储excel表格
    wb_wirte.saveSheet()