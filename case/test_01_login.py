# -*- coding: UTF-8 -*-
"""
@Project ：TouTiao_Interface_Test 
@File    ：test_01_login.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/6/1 2:08
"""

import unittest

import allure
from ddt import ddt, data, unpack

from api.api_login import ApiLogin
from tools.logger import logger
from tools.json_util import JsonUtil


def get_data():
    json_data = JsonUtil('login.json').read_json()
    args = (json_data.get('url'), json_data.get('mobile'), json_data.get('code'), json_data.get('except_code'),
            json_data.get('status_code'))
    return args


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户登录")
@ddt
class TestLogin(unittest.TestCase):

    @allure.story("用例--登录--预期成功")
    @allure.description("该用例是针对 登录 场景的测试")
    @allure.issue("https://github.com/xiaorui16888", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://github.com/xiaorui16888", name="点击，跳转到对应用例的链接地址")
    @allure.title("用户登录-预期成功")
    @data(get_data())
    @unpack
    def test_login(self, url, mobile, code, except_code, status_code):
        # 调用登录方法
        resp = ApiLogin().api_post_login(url, mobile, code)
        print('查看响应结果：', resp.json())
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, resp.json()["message"]))
        # 断言响应信息及状态码
        self.assertEqual(except_code, resp.json()['message'])
        self.assertEqual(status_code, resp.status_code)

        # 记录token
        JsonUtil('token.json').write_json({"Authorization": resp.json()['data']['token']})


if __name__ == '__main__':
    unittest.main()
