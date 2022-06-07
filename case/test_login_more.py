# -*- coding: UTF-8 -*-
"""
@Project ：TouTiao_Interface_Test 
@File    ：test_01_login.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/6/1 2:08
"""

import unittest

from ddt import ddt, data, unpack

from api.api_login import ApiLogin
from tools.json_util import JsonUtil


def get_data():
    json_datas = JsonUtil('login_more.json').read_json()
    arrs = []
    for json_data in json_datas.values():
        arrs.append((json_data.get('url'), json_data.get('mobile'), json_data.get('code'), json_data.get('expect_code'),
                     json_data.get('status_code')))
    # print(arrs)
    return arrs


@unittest.skip("跳过")
@ddt
class TestLoginMore(unittest.TestCase):

    @data(*get_data())
    @unpack
    def test_login_more(self, url, mobile, code, expect_code, status_code):
        # 调用登录方法
        resp = ApiLogin().api_post_login(url, mobile, code)
        print('查看响应结果：', resp.json())
        #
        # 断言响应信息及状态码
        self.assertEqual(expect_code, resp.json()['message'])
        self.assertEqual(status_code, resp.status_code)


# if __name__ == '__main__':
#     unittest.main()
