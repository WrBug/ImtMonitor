# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
from ImWalletApi import ImWalletApi


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def init_imt_account():
    imt_user = raw_input('输入云搬家账号：')
    imt_pass = raw_input('输入云搬家密码：')
    print '正在验证'
    result = ImWalletApi.login(username=imt_user, password=imt_pass)
    status = result['result']['status']
    if status == '1':
        print '验证成功'
        return True, imt_user, imt_pass
    return False, '', ''


def init_mail():
    mail = raw_input('输入收信邮箱：')
    from_mail = raw_input('输入smtp邮箱：')
    pswd = raw_input('输入smtp邮箱密码（部分邮箱需要申请授权码，如qq邮箱）：')
    smtp_server = raw_input('输入smtp服务器(QQ邮箱为：smtp.qq.com)：')
    msg = MIMEText('测试成功', 'plain', 'utf-8')
    msg['From'] = _format_addr(from_mail)
    msg['To'] = _format_addr(mail)
    msg['Subject'] = Header(u'邮箱测试', 'utf-8').encode()
    server = smtplib.SMTP_SSL(smtp_server)
    try:
        server.login(from_mail, pswd)
    except:
        return False, '', '', '', ''
    server.sendmail(from_mail, [mail], msg.as_string())
    server.quit()
    print '发送成功'
    return True, mail, from_mail, pswd, smtp_server


if __name__ == '__main__':
    print '星际魔盒一键安装脚本'
    while True:
        success, imt_user, imt_pass = init_imt_account()
        if not success:
            print '账号密码有误'
        else:
            break
    while True:
        success, mail, from_mail, pswd, smtp_server = init_mail()
        if not success:
            print '邮箱配置有误'
        else:
            break
    print '正在配置账号'
    fh = open('account.py.bak', 'r')
    str = fh.read()
    fh.close()
    str = str.replace('IMT_USER_INPUT', imt_user) \
        .replace('IMT_PASS_INPUT', imt_pass) \
        .replace('EMAIL_INPUT', mail) \
        .replace('FROM_EMAIL__INPUT', from_mail) \
        .replace('EMAIL_PASSWORD_INPUT', pswd).replace('SMTP_SERVER_INPUT', smtp_server)
    fh = open('account.py', 'w')
    fh.write(str)
    fh.close()
    print '账号配置完成'
