import json
import os

USER_SIGN_DIR = 'sign'


def save_to_file(path, file_name, contents):
    file_path = file_name
    if path is not None:
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = path + '/' + file_path
    fh = open(file_path, 'w')
    fh.write(contents)
    fh.close()


def save_user_sign(user, sign):
    isExists = os.path.exists(USER_SIGN_DIR)
    if not isExists:
        os.makedirs(USER_SIGN_DIR)
    save_to_file(USER_SIGN_DIR, user + '_signLogin', sign)


def get_user_sign(user):
    path = USER_SIGN_DIR + '/' + user + '_signLogin'
    if not os.path.exists(path):
        return None
    fh = open(path, 'r')
    str = fh.read()
    return str


def save_devices_list(data):
    save_to_file(None, 'devices_list', data)


def get_devices_list():
    if not os.path.exists('devices_list'):
        return {}
    fh = open('devices_list', 'r')
    str = fh.read()
    return str


def save_offline_list(list):
    save_to_file(None, 'offline_list', json.dumps(list))


def get_offline_list():
    if not os.path.exists('offline_list'):
        return []
    fh = open('offline_list', 'r')
    str = fh.read()
    if str == '':
        return []
    return json.loads(str)
