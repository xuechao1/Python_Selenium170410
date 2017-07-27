#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

def send_mail(file_new,to_mail):
    """====发送最新的测试报告到指定邮箱======"""
    f = open(file_new,'rb')
    mail_body = f.read() #读取测试报告正文
    f.close()
    username = 'xue10123456@163.com'
    # 客户端授权密码
    password = '13569941859'

    #通过  模块构造的带附件的邮件如图
    msg = MIMEMultipart()
    #编写html类型的邮件正文，MIMEtext()用于定义邮件正文
    #发送正文
    text = MIMEText(mail_body, 'html', 'utf-8')
    text['Subject'] = Header('自动化测试报告', 'utf-8')
    msg.attach(text)
    #发送附件
    #Header()用于定义邮件标题
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_file)

    msg['from'] = 'xue10123456@163.com'  # 发送邮件的人
    msg['to'] = to_mail
    # smtp = smtplib.SMTP('smtp.163.com', 25)  # 连接服务器
    smtp = smtplib.SMTP()
    print smtp.connect('smtp.163.com')
    print smtp.login(username, password)  # 登录的用户名和密码
    print smtp.sendmail(msg['from'], msg['to'], msg.as_string())  # 发送邮件
    smtp.quit()
    print('sendmail success')

def new_report(testreport):
    """====查找最新的测试报告======"""
    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    return file_new

