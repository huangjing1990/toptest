# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午5:22
# @Author  : maxiang
# @File    : Request.py

"""
封装request

"""
from Common import Assert
import requests
import Common.Consts
from Common.log_Common import *
import json

s = requests.Session()
test = Assert.Assertions()


class Request:

    @logger('get_request')
    def get_request(self, url, data=None, header=None):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)

        try:
            if data is None:
                LOG.info('请求地址：%s' % (url))
                LOG.info('请求入参：%s' % (data))
                response = requests.get(url=url, headers=header)
                assert test.assert_code(response.status_code, 200)
            else:
                LOG.info('请求地址：%s' % (url))
                LOG.info('请求入参：%s' % (data))
                response = requests.get(url=url, params=data, headers=header)
                assert test.assert_code(response.status_code, 200)
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

        Common.Consts.STRESS_LIST.append(time_consuming)

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
        response_dicts['history'] = response.history
        LOG.info(url + ': 返回结果：%s' % (response.json()))
        return response_dicts

    @logger('post_request')
    def post_request(self, url, params, header, token=None):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:a
        """
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)
        ContentType = header.get("Content-Type")
        if (token is not None):
            s.headers.update(token)
        try:
            if params is None:
                response = requests.post(url, data=None, headers=header)
            else:
                if (ContentType == "application/json"):
                    data_str = json.dumps(params)
                else:
                    data_str = params
                LOG.info('请求地址：%s' % (url))
                LOG.info('请求入参：%s' % (data_str))
                LOG.info('请求header：%s' % (header))
                response = requests.post(url, data=data_str, headers=header)
                assert test.assert_code(response.status_code, 200)
                LOG.info('response.status_code：%s' % (response.status_code))
                s.close()

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return e

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return e

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

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
        LOG.info(url + ': 返回结果：%s' % (response.json()))
        return response_dicts

    @logger('post_request_multipart')
    def post_request_multipart(self, url, header, file):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            LOG.info('请求地址：%s' % (url))
            files = open(file, 'rb')
            files = {
                'excelFile': files
            }
            LOG.info('请求地址files：%s' % (files))
            response = requests.post(url, files=files, headers=header)

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

        Common.Consts.STRESS_LIST.append(time_consuming)

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
                response = requests.put(url=url, headers=header)
            else:
                response = requests.put(url=url, params=data, headers=header)

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

        Common.Consts.STRESS_LIST.append(time_consuming)

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
