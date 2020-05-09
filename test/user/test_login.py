import unittest
import requests
from lib.read_excel import *
import json
import os
from lib.case_log import *
import sys
sys.path.append("../..")
from config.config import *
from lib.read_excel import *
from lib.case_log import *
from test.case.basecase import BaseCase

class Testlogin(unittest.TestCase):
    '''url = 'http://192.168.9.212:8620/gateway/login'''

    # def test_login_normal(self, ky):
    #     param = {"key": "{}".format(ky)}
    #
    #     res = requests.get(url=self.url, params=param)
    #     self.assertIn("成功", res.text)
    #     # text = res.text
    #     # return text
    #
    # def test_login_errorkey(self, ky):
    #     param = {"key": "{}".format(ky)}
    #
    #     res = requests.get(url=self.url, params=param)
    #     self.assertIn("用户名或密码错误", res.text)


#  登录模块测试用例

    # def setUp(self):
    #     print("登录测试用例开始")
    #
    # def tearDown(self):
    #     print("登录测试用例完成")
    #
    # def test_login_normal(self):
    #     param = {"key": "1IEuD18Z1ug=|k6NQq3efZgg="}
    #
    #     res = requests.get(url=self.url, params=param)
    #     self.assertIn("成功", res.text)
    #     text = res.text
    #     return text
    #
    # def test_login_errorkey(self):
    #     param = {"key": "1IEuD18Z1ug=|43uuS2GwxAtAfhWo8r1NzA=="}
    #
    #     res = requests.get(url=self.url, params=param)
    #     self.assertIn("用户名或密码错误", res.text)
    #
    # def test_login_null(self):
    #     param = {"key": ""}
    #
    #     res = requests.get(url=self.url, params=param)
    #     self.assertIn("参数不能为空", res.text)
    #
    # def test_login_cha(self):
    #     param = {"key": "密码"}
    #     res = requests.get(url=self.url, params=param)
    #     self.assertIn("参数错误", res.text)
    #
    # if __name__ == '__main__':
    #     unittest.main(verbosity=2)

# 调用封装的方法运行用例
#     @classmethod
#     def setUpClass(cls):
#         cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserLogin")
#
#     def test_login_normal(self):
#         case_data = get_test_data(self.data_list, 'test_login_normal')
#         if not case_data:
#             logging.error("用例数据不存在")
#         else:
#             url = case_data.get('url')
#             params = case_data.get('params')
#             expect_res = case_data.get('expect_res')
#             res = requests.get(url=url, params=json.loads(params))
#             self.assertIn(expect_res, res.text)
#             log_case_info(case_data.get('case_name'), url, params, expect_res, res.text)
#
#
#
#     def test_login_errorkey(self):
#         case_data = get_test_data(self.data_list, 'test_login_errorkey')
#         if not case_data:
#             logging.error("用例数据不存在")
#         else:
#             url = case_data.get('url')
#             params = case_data.get('params')
#             expect_res = case_data.get('expect_res')
#             res = requests.get(url=url, params=json.loads(params))
#             self.assertIn(expect_res, res.text)
#             log_case_info(case_data.get('case_name'), url, params, expect_res, res.text)
#
#     def test_login_null(self):
#         case_data = get_test_data(self.data_list, 'test_login_null')
#         if not case_data:
#             logging.error("用例数据不存在")
#         else:
#             url = case_data.get('url')
#             params = case_data.get('params')
#             expect_res = case_data.get('expect_res')
#             res = requests.get(url=url, params=json.loads(params))
#             self.assertIn(expect_res, res.text)
#             log_case_info(case_data.get('case_name'), url, params, expect_res, res.text)
#
#     def test_login_cha(self):
#         case_data = get_test_data(self.data_list, 'test_login_cha')
#         if not case_data:
#             logging.error("用例数据不存在")
#         else:
#             url = case_data.get('url')
#             params = case_data.get('params')
#             expect_res = case_data.get('expect_res')
#             res = requests.get(url=url, params=json.loads(params))
#             self.assertIn(expect_res, res.text)
#             log_case_info(case_data.get('case_name'), url, params, expect_res, res.text)

class TestUserLogin(BaseCase):
    def test_login_normal(self):
        case_data = self.get_case_data("test_login_normal")
        self.send_request(case_data)
    def test_login_errorkey(self):
        case_data = self.get_case_data("test_login_errorkey")
        self.send_request(case_data)
    def test_login_null(self):
        case_data = self.get_case_data("test_login_null")
        self.send_request(case_data)
    def test_login_cha(self):
        case_data = self.get_case_data("test_login_cha")
        self.send_request(case_data)





if __name__ == '__main__':
    unittest.main(verbosity=2)