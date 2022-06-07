# -*- coding: UTF-8 -*-
"""
@Project ：TouTiao_Interface_Test 
@File    ：api_channels.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/6/1 12:57
"""

import requests


class ApiChannels:

    def api_get_channels(self, url, headers):
        return requests.get(url, headers=headers)
