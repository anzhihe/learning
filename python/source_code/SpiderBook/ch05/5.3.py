#coding:utf-8
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
#发件人地址
from_addr = 'xxxxxxxx@163.com'
#邮箱密码
password = 'pass'
#收件人地址
to_addr = 'xxxxxxxx@qq.com'
#163网易邮箱服务器地址
smtp_server = 'smtp.163.com'
#设置邮件信息
msg = MIMEText('Python爬虫运行异常，异常信息为遇到HTTP 403', 'plain', 'utf-8')
msg['From'] = _format_addr('一号爬虫 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('一号爬虫运行状态', 'utf-8').encode()
#发送邮件
server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
