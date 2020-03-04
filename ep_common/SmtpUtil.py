# -*- coding : utf-8 -*-
"""
@projectname : Epass
@author : WangJing
@Time : 2019/8/8
@File : SmtpUtil.py
@describe : smtp邮件发送

"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_mail(file_new):
    # smtpserver = 'smtp.qq.com'
    smtpserver = 'xxx'
    # 发送邮箱用户/密码(登录邮箱操作)
    user = 'xxx'
    password = ''
    # 发送邮箱
    sender = "xxx"
    # 接收邮箱
    # receiver = ["xxxxxx"]
    receiver = 'xxx'
    # receiver = 'xxx'
    message = MIMEMultipart()
    message['From'] = Header('xxx', 'utf-8')
    message['to'] = Header('develop', 'utf-8')
    # 发送主题
    subject = 'Api_Test_Report'
    message['Subject'] = Header(subject, 'utf-8')
    mail_body = open(file_new, "rb").read()
    message.attach(MIMEText(mail_body, 'html', 'utf-8'))
    send_file = MIMEText(mail_body, 'base64', 'utf-8')
    # mail_body = send_file.read()
    # msg = MIMEText(mail_body, 'html', 'utf-8')
    send_file["Content-Type"] = 'application/octet-stream'
    send_file["Content-Disposition"] = 'attachment; filename=Epass_api_test_report.html'
    message.attach(send_file)
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver.split(','), message.as_string())
    smtp.quit()
    print("邮件已发出！注意查收。")


# ====================查找测试报告目录，找到最新生成的测试报告文件========
def newReport(test_report):
    print(test_report)
    lists = os.listdir(test_report)
    print(lists)
    lists2 = sorted(lists)
    print(lists2)
    file_new = os.path.join(test_report, lists2[-1])
    print(file_new)
    return file_new