# -*- coding: UTF-8 -*-
"""
@Project ：TouTiao_Interface_Test 
@File    ：api_article.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/6/1 23:12
"""

import requests


class ApiArticle:

    # 发布文章
    def post_article(self, url, headers, json):
        return requests.post(url=url, headers=headers, json=json)

    # 获取文章详情
    def get_article_detail(self, url, headers, target_id):
        return requests.get(url=url + '/' + target_id, headers=headers)

    # 删除文章
    def delete_article(self, url, headers, target_id):
        return requests.delete(url=url + '/' + target_id, headers=headers)

    # 修改文章为草稿状态
    def update_draft_article(self, url, headers, target_id, json):
        return requests.put(url=url + '/' + target_id, headers=headers, json=json, params={"draft": "true"})

    # 获取文章列表
    def get_articles(self, url, headers):
        return requests.get(url=url, headers=headers)
