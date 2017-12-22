# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from common.iniParser import IniParser
import json



conf_path = BASE_DIR + '\\conf\\testInfo.ini'
# print(BASE_DIR, conf_path)

# 获取测试链接主页
cf = IniParser(conf_path)
base_url = cf.get_item('url', 'baseUrl')

# 判断发送测试报告使用哪一种邮箱
email_type = cf.get_item('emails', 'email_type')
email_server = json.loads(cf.get_item('emails', 'email_dic'))[email_type]

# 获取邮箱发件人账号密码
email_sender = cf.get_item('emails', 'sender')
email_sender_pwd = cf.get_item('emails', 'sender_pwd')

# 获取邮件收件人账号
email_receivers = json.loads(cf.get_item('emails', 'receivers'))