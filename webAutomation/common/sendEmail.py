# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)
import time
import smtplib
import sys
from conf import settings
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

class SendEmail(object):
    """
    发送邮件
    __init__(self, subject):
        subject：str类型，邮件主题

    def add_text(self, text):
        text：邮件内容
        添加邮件文本内容

    add_att(self, report_path):
        report_path：测试报告所在路径
        添加邮件附件

    """
    def __init__(self, subject):
        self.server = settings.email_server
        self.sender = settings.email_sender
        self.sender_pwd = settings.email_sender_pwd
        self.receivers = settings.email_receivers
        if type(subject) is not str:
            sys.stderr.write('error, Usage str type for sendEmail object init\n')
            sys.exit(1)
        self.subject = subject
        self.msgs = []

    def add_text(self, text):
        msg = MIMEText('<html><h1>%s</h1></html>' % text, 'html', 'utf-8')
        self.msgs.append(msg)

    def add_file_content(self, report_path):
        if not os.path.isfile(report_path):
            sys.stderr.write('error, report %s not exists\n' % report_path)
            sys.exit(1)
        with open(report_path, 'rb') as report_obj:
            content = report_obj.read()
        msg = MIMEText(_text=content, _subtype='html', _charset='utf-8')
        self.msgs.append(msg)

    def add_att(self, report_path):
        if not os.path.isfile(report_path):
            sys.stderr.write('error, report %s not exists\n' % report_path)
            sys.exit(1)
        with open(report_path, 'rb') as report_obj:
            sendfile = report_obj.read()

        att = MIMEText(sendfile, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        report_name = os.path.basename(report_path)
        att['Content-Disposition'] = "attachment; filename=%s" % report_name
        self.msgs.append(att)

    def send_email(self):
        print('开始发送邮件')
        smtp = smtplib.SMTP()
        smtp.connect(self.server)
        smtp.login(self.sender, self.sender_pwd)

        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = Header(self.subject, "utf-8")
        msgRoot['From'] = self.sender
        if not self.receivers:
            print("email receivers empty")
        for msg_obj in self.msgs:
            msgRoot.attach(msg_obj)

        # print(type(self.receivers), self.receivers)
        for receiver in self.receivers:
            # print(receiver)
            msgRoot['To'] = receiver
            smtp.sendmail(self.sender, receiver, msgRoot.as_string())

        self.msgs.clear()
        smtp.quit()
        print("发送邮件成功")


# if __name__ == "__main__":
#     server = settings.email_server
#     sender = settings.email_sender
#     sender_pwd = settings.email_sender_pwd
#     receivers = settings.email_receivers
#     subject = "test for file to html content"
#     report_path = settings.BASE_DIR + '\\report\\test_sinaemail.html'
#     if not os.path.isfile(report_path):
#         sys.stderr.write('error, report %s not exists\n' % report_path)
#         sys.exit(1)
#     with open(report_path, 'r', encoding='utf-8') as report_obj:
#         content = report_obj.read()
#     msg = MIMEText(_text=content, _subtype='html', _charset='utf-8')
#     # print(content)
#     smtp = smtplib.SMTP()
#     smtp.set_debuglevel(1)
#     smtp.connect(server)
#     print(sender, sender_pwd)
#     smtp.login(sender, sender_pwd)
#     msg['From'] = sender
#     for receiver in receivers:
#         msg['To'] = receiver
#         smtp.sendmail(sender, receiver, msg.as_string())
#         receivers.remove(receiver)