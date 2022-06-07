import unittest

from ddt import ddt, data, unpack

from api.api_channels import ApiChannels
from tools.json_util import JsonUtil
from tools.logger import logger


def get_data():
    json_data = JsonUtil('channel.json').read_json()
    print('json_data===', json_data)
    args = (json_data.get('url'), json_data.get('headers'), json_data.get('status_code'),
            json_data.get('except_code'))
    # print(args)
    return args


# @unittest.skip("跳过")
@ddt
class TestChannel(unittest.TestCase):

    @data(get_data())
    @unpack
    def test_get_channel(self, url, headers, status_code, except_code):
        headers['Authorization'] = JsonUtil('token.json').read_json()['Authorization']
        resp = ApiChannels().api_get_channels(url, headers)
        print(resp.json())
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, resp.json()["message"]))
        # 断言状态码
        self.assertEqual(status_code, resp.status_code)
        # 断言响应信息
        self.assertEqual(except_code, resp.json()['message'])

# if __name__ == '__main__':
#     pass
