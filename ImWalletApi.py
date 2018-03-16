import json

from Request import post
from utils import get_devices_list


class ImWalletApi:
    def __init__(self):
        pass

    @staticmethod
    def login(username, password):
        params = [
            {
                'loginName': str(username),
                'password': str(password)
            }
        ]

        response = post('user', 'login', params)
        return json.loads(response)

    @staticmethod
    def get_devices_id(sign_login):
        params = [sign_login]
        response = post('clouds', 'getDrviceid', params)
        data = json.loads(response)
        if data['result']['status'] != '1':
            return None
        data = data['result']['data']
        devices = {}
        for device in data:
            if device['cloudCode'] != 'hdMohe':
                continue
            devices[device['sn']] = device
        return devices

    @staticmethod
    def get_my_cloud(sign_login):
        params = [sign_login]
        response = post('clouds', 'myCloud', params)
        data = json.loads(response)
        if data['result']['status'] != '1':
            return None
        data = data['result']['data']
        device_list_str = get_devices_list()
        device_list=json.loads(device_list_str)
        devices = []
        for device in data:
            if device['cloudCode'] != 'hdMohe':
                continue
            ip = device_list[str(device['cloudUserIdId'])]
            device['localIp'] = ip['intranetIp']
            device['remoteIp'] = ip['extranetIp']
            devices.append(device)
        return devices
