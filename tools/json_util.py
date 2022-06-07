# -*- coding: UTF-8 -*-
"""
@Project ：TouTiao_Interface_Test 
@File    ：json_util.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/6/1 2:21
"""

import json

from config import base_path


class JsonUtil:

    def __init__(self, filename):
        self.filepath = base_path + '/data/{}'.format(filename)

    # 读取json
    def read_json(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            # 调用load方法加载文件流
            return json.load(f)

    # 写入Json
    def write_json(self, case):
        with open(self.filepath, "w", encoding="utf-8")as f:
            json.dump(case, f, indent=4, ensure_ascii=False)
