"""
封装request

"""

import os
import random
import requests
from common import session
from requests_toolbelt import MultipartEncoder


class Request:

    def __init__(self):

        self.session = session.Session()
        self.get_session = self.session.get_session()
        self.get_token = self.session.get_token()

    def get_request(self, url, data, login_state):
        """
        Get请求
        :param login_state:
        :param url:
        :param data:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        print(data)
        if data:
            param = eval(data)
            if 'token' in param.keys():
                param['token'] = self.get_token['token']
            elif 'userid' in param.keys():
                param['userid'] = self.get_token['userid']
        else:
            param = None

        try:
            if login_state == 'N' and not param:
                response = requests.get(url=url)  # 构造无cookie无参数get请求
            elif login_state == 'N' and param:
                response = requests.get(url=url, params=param)  # 构造无cookie带参数get请求
            elif login_state == 'Y' and not param:
                response = requests.get(url=url, cookies=self.get_session)  # 构造带cookie无参数get请求
            else:
                response = requests.get(url=url, params=param, cookies=self.get_session)  # 构造带cookie带参数get请求

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()
        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            print('接口参数异常，无返回值')
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        print(response_dicts['body'])
        return response_dicts

    def post_request(self, url, data, login_state):
        """
        Post请求
        :param login_state:
        :param url:
        :param data:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        print(data)
        if not data:
            param = None
        else:
            param = eval(data)
            if 'token' in param.keys():
                param['token'] = self.get_token['token']
            elif 'userid' in param.keys():
                param['userid'] = self.get_token['userid']

        try:
            if login_state == 'N' and not param:
                response = requests.post(url=url)  # 构造无cookie无参数post请求
            elif login_state == 'N' and param:
                response = requests.post(url=url, params=param)  # 构造无cookie带参数post请求
            elif login_state == 'Y' and not param:
                response = requests.post(url=url, cookies=self.get_session)  # 构造带cookie无参数post请求
            else:
                response = requests.post(url=url, params=param, cookies=self.get_session)  # 构造带cookie带参数post请求
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        print(response.status_code)
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            print('接口参数异常，无返回值')
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_request_multipart(self, url, data, header, file_parm, file, f_type):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param f_type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header, cookies=self.get_session)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_request(self, url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.put(url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
