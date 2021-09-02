#-*- coding: UTF-8 -*- 
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def openmail(sender):
    smtpserver = 'smtp.163.com'
    port = 465
    username = 'example@example'
    password = '123456'
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    try:
        smtp.login(username, password)
    except:
        print("login fail")
        return -1
    return smtp

def sendmessage(sender,receiver,mail_title,mail_body,smtp):
    # 创建一个实例
    message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
    message['From'] = sender  # 邮件上显示的发件人
    message['To'] = receiver  # 邮件上显示的收件人
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题
    smtp.sendmail(sender, receiver, message.as_string())

def closemail(smtp):
    smtp.quit()