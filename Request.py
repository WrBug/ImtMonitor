# coding:utf-8
import json, os
from constant import Constant


def get(url):
    cmd = "wget --quiet --method GET --header 'cache-control: no-cache' --output-document - '" + url + "'"
    result = os.popen(cmd)
    result = result.read()
    return result


def post(path, method, params):
    data = create_request(method, params)
    cmd = "wget --header 'Content-Type: application/json' --post-data '" + data + "' --output-document - " + Constant.IMT_LOGIN_URL + "/" + path + " --no-check-certificate -q"
    result = os.popen(cmd)
    result = result.read()
    return result


def create_request(method, params):
    request = {
        'id': Constant.REQUEST_ID,
        'jsonrpc': '2.0',
        'method': method,
        'params': params
    }
    return json.dumps(request)
