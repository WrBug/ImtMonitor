import json
import urllib

from Request import get
from account import Account


class FtqqApi:
    @staticmethod
    def send_wechat_msg(title, content):
        return FtqqApi.send_wechat_msg_with_key(Account.FTQQ_SCKEY, title, content)

    @staticmethod
    def send_wechat_msg_with_key(sckey, title, content):
        url = 'https://sc.ftqq.com/' + sckey + '.send?' + urllib.urlencode(
            {'text': title, 'desp': content})
        result = get(url)
        result = json.loads(result)
        if result['errno'] == 0:
            return ''
        return result['errmsg']
