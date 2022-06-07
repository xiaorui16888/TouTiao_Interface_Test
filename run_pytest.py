# -*- coding: UTF-8 -*-
"""
@Project ：TouTiao_Interface_Test 
@File    ：run_pytest.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/6/2 23:45
"""

import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temps -o ./report --clean')
