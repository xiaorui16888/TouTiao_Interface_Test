# -*- coding: UTF-8 -*-
"""
@Project ：TouTiao_Interface_Test 
@File    ：yaml_util.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/6/3 0:27
"""

# -*- coding: UTF-8 -*-
from config import base_path
import yaml


class YamlUtil:
    def __init__(self, yaml_file):
        self.yaml_file = base_path + '/' + yaml_file

    def read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            file_dict = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            print(file_dict)

    def write_yaml(self, data):
        with open(self.yaml_file, encoding='utf-8', mode='w') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
