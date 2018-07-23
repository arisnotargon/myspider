#!/usr/bin/python

# 发邮件脚本
import smtplib
from email.header import Header
from email.mime.text import MIMEText

def send(mail_from,mail_to,mail_content,mail_subject,mail_account,mail_pwd):
    msg = MIMEText(mail_content,'plain','utf-8')
    msg['Subject'] = mail_subject
    msg['From'] = Header(mail_from)
    msg['To'] = Header('receiver', 'utf-8')
    mail_to = ','.join(mail_to)
    mail_host = 'smtp.exmail.qq.com'
    server = smtplib.SMTP_SSL(mail_host,465)
    print('开始登陆')
    server.login(mail_account, mail_pwd)
    print('登陆成功')
    server.sendmail(mail_account, mail_to, msg.as_string())
    server.quit()
    print('发送成功')

if __name__ == '__main__':
    with open("emailContent", 'r', encoding = 'utf-8')as t:
        mail_content = t.read()

    mail_subject = '邮件主题'
    mail_from = 'bd@nobot.tech'
    mail_to = ['jiajun.wang@nobot.tech']
    mail_account = 'system@nobot.tech'
    mail_pwd = 'faBUdao?!23'
    send(mail_from,mail_to,mail_content,mail_subject,mail_account,mail_pwd)
