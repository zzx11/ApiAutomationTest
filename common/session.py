"""
封装获取cookie方法

"""

import requests
from addict import Dict

from common.logger import Logger
from config import config

my_log = Logger(logger='Session').get_log()


class Session:
    def __init__(self):
        self.config = config.Config()

    def get_session(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)\
                          Chrome/67.0.3396.99 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        print(self.config.loginHost)
        if self.config.login_if != 'No':
            login_url = self.config.host + self.config.loginHost
            parm = self.config.loginInfo
            session = requests.session()
            response = session.post(login_url, eval(parm), headers=headers)
            my_log.info('cookies: %s' % response.cookies.get_dict())
            return response.cookies.get_dict()
        else:
            return None

    def get_token(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)\
                                  Chrome/67.0.3396.99 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        if self.config.login_if != 'No':
            login_url = self.config.host + self.config.loginHost
            parm = self.config.loginInfo
            token = requests.session()
            response = token.post(login_url, eval(parm), headers=headers)
            body = response.json()
            body2 = Dict(body)
            token = body2.data[0].token
            userid = body2.data[0].userid
            token = {'token': token, 'userid': userid}
            my_log.info('token: %s' % token)
            return token
        else:
            return None


if __name__ == '__main__':
    ss = Session()
    ss.get_token()
