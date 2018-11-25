from django.test import TestCase

# Create your tests here.
from email.mime.text import MIMEText
msg = MIMEText('--------------在 pycharm li account/test.py 写发邮件的代码', 'plain', 'utf-8')
# 输入Email地址和口令:
# from_addr = input('From: ')
from_addr = '42967148@qq.com'
# password = input('Password: ')
password = 'zpvdczodqubrbijf'
# 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
smtp_server = 'smtp.qq.com'
# 输入收件人地址:
# to_addr = input('To: ')
to_addr = 'c5t4v@163.com'

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()