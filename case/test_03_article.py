# -*- coding: UTF-8 -*-
"""
@Project ：TouTiao_Interface_Test 
@File    ：test_03_article.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/6/1 23:16
"""

import unittest

from ddt import ddt, data, unpack

from api.api_article import ApiArticle
import time

from tools.json_util import JsonUtil
from tools.logger import logger


def get_data(filename):
    json_data = JsonUtil(filename).read_json()
    print('json_data===', json_data)
    args = (json_data.get('url'), json_data.get('headers'), json_data.get('status_code'),
            json_data.get('except_code'))
    # print(args)
    return args


# @unittest.skip("")
@ddt
class TestArticle(unittest.TestCase):
    article_id = None
    article_json = {
        "title": str(time.time()) + "test_title_guo",
        "content": "i am content~~~",
        "cover": {
            "type": 0,
            "images": []
        },
        "channel_id": 2
    }

    # 发布文章
    @unittest.skip('')
    @data(get_data('get_article.json'))
    @unpack
    def test_01_post_article(self, url, headers, status_code, except_code):
        headers['Authorization'] = JsonUtil('token.json').read_json()['Authorization']
        resp = ApiArticle().post_article(url=url, headers=headers, json=TestArticle.article_json)
        TestArticle.article_id = resp.json()['data']['id']
        print(resp.json())
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(status_code, resp.json()["message"]))
        # 响应码断言
        self.assertEqual(status_code, resp.status_code)
        # 业务断言
        self.assertEqual(except_code, resp.json()['message'])

    # 获取文章详情
    @unittest.skip('')
    @data(get_data('get_article.json'))
    @unpack
    def test_02_get_article_detail(self, url, headers, status_code, except_code):
        headers['Authorization'] = JsonUtil('token.json').read_json()['Authorization']
        resp = ApiArticle().get_article_detail(url=url, headers=headers, target_id=TestArticle.article_id)
        print(resp.json())
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(status_code, resp.json()["message"]))
        del resp['data']['id']
        del resp['data']['pub_date']

        self.assertEqual(status_code, resp.status_code)
        # 业务断言
        self.assertEqual(except_code, resp.json()['message'])
        self.assertDictEqual(TestArticle.article_json, resp['data'])

    # 修改文章为草稿状态
    @unittest.skip('')
    @data(get_data('get_article.json'))
    @unpack
    def test_03_update_draft_article(self, url, headers, status_code, except_code):
        headers['Authorization'] = JsonUtil('token.json').read_json()['Authorization']
        resp = ApiArticle().update_draft_article(url=url, headers=headers, target_id=TestArticle.article_id,
                                                 json=TestArticle.article_json)
        print(resp.json())
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(status_code, resp.json()["message"]))

        self.assertEqual(status_code, resp.status_code)
        # 业务断言
        self.assertEqual(except_code, resp.json()['message'])
        self.assertDictEqual(TestArticle.article_json, resp['data'])

    # 删除文章
    @unittest.skip('')
    @data(get_data('get_article.json'))
    @unpack
    def test_04_delete_article(self, url, headers, status_code, except_code):
        headers['Authorization'] = JsonUtil('token.json').read_json()['Authorization']
        resp = ApiArticle().delete_article(url=url, headers=headers, target_id=TestArticle.article_id)
        print(resp.json())
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(status_code, resp.json()["message"]))
        self.assertEqual(status_code, resp.status_code)
        # 业务断言
        self.assertEqual(except_code, resp.json()['message'])
        self.assertDictEqual(TestArticle.article_json, resp['data'])

    # 获取文章详情
    @data(get_data('get_article.json'))
    @unpack
    def test_05_get_articles(self, url, headers, status_code, except_code):
        headers['Authorization'] = JsonUtil('token.json').read_json()['Authorization']
        print('headers==', headers)
        resp = ApiArticle().get_articles(url=url, headers=headers)
        print(resp.json())

        self.assertEqual(status_code, resp.status_code)
        # 业务断言
        self.assertEqual(except_code, resp.json()['message'])


if __name__ == '__main__':
    unittest.main()
