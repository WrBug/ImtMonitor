# coding:utf-8
import json
from account import Account
from ImWalletApi import ImWalletApi
from ftqqApi import FtqqApi
from mail import send_mail, send_exception
from utils import save_user_sign, get_user_sign, save_devices_list, get_offline_list, save_offline_list, \
    get_unsend_offline_list, save_unsend_offline_list


def login(user, pswd):
    result = ImWalletApi.login(username=user, password=pswd)
    status = result['result']['status']
    if status == '1':
        print '登录成功'
        save_user_sign(user, result['result']['data']['signLogin'])
        return check_sign(user)
    else:
        print result['result']['message']
        return False


def check_sign(user):
    signLogin = get_user_sign(user)
    if signLogin is None:
        return False
    devices = ImWalletApi.get_devices_id(signLogin)
    if devices is None:
        print '身份已过期'
        return False
    save_devices_list(json.dumps(devices))
    print '设备获取成功'
    return True


def get_devices(user):
    signLogin = get_user_sign(user)
    if signLogin is None:
        print '身份已过期'
    devices = ImWalletApi.get_my_cloud(signLogin)
    if devices is None:
        print '身份已过期'
    print '-----------设备状态-----------'
    online_num = 0
    offline_num = 0
    offline_devices_name = []
    for device in devices:
        online = device['onOrOffLine'] == '1'
        if online:
            online_num += 1
        else:
            offline_num += 1
            offline_devices_name.append(str(device['cloudUserId']))
        print '设备名:\t' + str(device['cloudUserId'])
        print '是否在线:\t' + str(online)
        print '设备IP:\t' + str(device['remoteIp'])
        print '本地IP:\t' + str(device['localIp'])
        print '磁盘总计:\t' + str(device['quotaTotal'])
        print '\n'
    print '在线：' + str(online_num) + '台，离线：' + str(offline_num)
    unsend_offline_list = get_unsend_offline_list()
    if offline_num > 0:
        print '发现离线设备'
        title = '异常设备列表'
        msg = ''
        un_send_cache = {}
        new_devices = False
        for name in offline_devices_name:
            if unsend_offline_list.has_key(name):
                if not unsend_offline_list[name]:
                    new_devices = True
                    msg += name + '\n'
                un_send_cache[name] = True
            else:
                un_send_cache[name] = False
        if new_devices:
            if Account.SEND_TYPE == '1':
                msg = title + '\n' + msg
                send_exception(msg)
            else:
                msg.replace('\n', '  |  ')
                data = FtqqApi.send_wechat_msg('IMT监工，发现异常设备', msg)
                if data == '':
                    print '发送成功'
                else:
                    return

        save_unsend_offline_list(un_send_cache)


if __name__ == '__main__':
    user = Account.IMT_USER
    if not check_sign(user):
        pswd = Account.IMT_PASS
        if not login(user, pswd):
            exit(0)
    get_devices(user)
