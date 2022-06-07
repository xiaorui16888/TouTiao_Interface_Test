# -*- coding: UTF-8 -*-
"""
@Project ：TouTiao_Interface_Test 
@File    ：api_login.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/6/1 2:05
"""

import requests


class ApiLogin:

    def api_post_login(self, url, mobile, code):
        headers = {'content-type': 'application/json'}
        data = {'mobile': mobile, 'code': code}
        return requests.post(url, headers=headers, json=data)
