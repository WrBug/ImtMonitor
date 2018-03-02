# coding:utf-8
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from account import Account
from email.header import Header

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def send_exception(msg):
    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['From'] = _format_addr(Account.FROM_EMAIL)
    msg['To'] = _format_addr(Account.EMAIL)
    msg['Subject'] = Header(u'星际魔盒设备异常提醒', 'utf-8').encode()
    send_mail(msg)


def send_mail(msg):
    server = smtplib.SMTP_SSL(Account.SMTP_SERVER)
    try:
        server.login(Account.FROM_EMAIL, Account.EMAIL_PASSWORD)
    except:
        return False
    server.sendmail(Account.FROM_EMAIL, [Account.EMAIL], msg.as_string())
    server.quit()
    return True


if __name__ == '__main__':
    msg = MIMEText('测试成功', 'plain', 'utf-8')
    msg['From'] = _format_addr(Account.FROM_EMAIL)
    msg['To'] = _format_addr(Account.EMAIL)
    msg['Subject'] = Header(u'邮箱测试', 'utf-8').encode()
    if send_mail(msg):
        print '发送成功'
    else:
        print '邮箱配置有误'
