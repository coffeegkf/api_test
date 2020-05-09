# def is_ip(ip):
#     num_list = str(ip).split(".")
#     if len(num_list) != 4:
#         return False
#     for num in num_list:
#         print(num)
#         if num.lstrip("0") != num or not num.isdigit() or not 0 <= int(num) <=255:
#             return False
#     return True
#
#
# print(is_ip("101.1.1.201"))

# python发送请求

# 发送get请求
# url = "http://192.168.9.212:8620/gateway/login?key=1IEuD18Z1ug%3D%7Ck6NQq3efZgg%3D"
# res = requests.get(url=url)


# url = "http://192.168.9.212:8620/gateway/login"
# params = {"key": "1IEuD18Z1ug=|k6NQq3efZgg="}
# res = requests.get(url=url, params=params)
# print(res.text)

# 发送post请求
# url = "http://192.168.9.212:8620/gateway/enterprise/"
# data = {
#   "administrative": "511502",
#   "businessLicense": "",
#   "controlClass": "",
#   "dataSources": "录入",
#   "economyType": "",
#   "enterpriseAddress": "",
#   "enterpriseName": "测试测试测试笑",
#   "enterprisePlanUrl": "",
#   "enterpriseStatus": "0",
#   "info": "",
#   "isDischargeAir": "0",
#   "isDischargeWater": "1",
#   "isOpera": "1",
#   "isSpecial": "1",
#   "latitude": "30.994320",
#   "legalPersonName": "测试",
#   "legalPersonTel": "",
#   "longitude": "103.815308",
#   "mainProducts": "",
#   "organizationCode": "",
#   "socialCreditCode": "123456789012345678",
#   "updateTime": 1586846459555,
#   "updateUser": "啊打发",
#   "zipCode": ""
# }
# header = {"Content-Type": "application/json", "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ey"
#                                                              "J1TmFtZSI6IuWViuaJk-WPkSIsImxvZ2luTmFtZSI6InRlc3QwMDIiL"
#                                                              "CJleHAiOjE1ODk0NDA2NDgsInVzZXJJZCI6ImY2MTA4YjBmNWY3NTQy"
#                                                              "ZWQ4NGQxZTY4NGJjNzMyMzAwIiwiaWF0IjoxNTg2ODQ4NjQ4fQ.uCpf"
#                                                              "R1owIci-JMa6FulWKOBPnKcI4-bXLkb5bSETHAU"}
# res = requests.post(url=url, data=json.dumps(data), headers=header)
# res = requests.post(url=url,json=data, headers=header)
# print(res.text)

# m = 0
# while m <41:
#     print("请输入信息：")
#     info = str(input())
#     url = "http://www.tuling123.com/openapi/api"
#     p = {"key": "ec961279f453459b9248f0aeb6600bbe", "info": "info"}
#     req = requests.get(url=url, params=p)
#     print(req.text)
#     m+=1
# print("尝试次数过多！")

# s = requests.session()
# s.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"username":"admin","password":"123456"})
# res = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs")
# print(res.text)
#
# import requests
# import json
#
# app_key = 'kPoFYw85FXsnojsy5bB9hu6x'
# secret_key = 'l7SuGBkDQHkjiTPU3m6NaNddD6SCvDMC'
# img_url = 'http://upload-images.jianshu.io/upload_images/7575721-40c847532432e852.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
# # 获取token
# get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(app_key,secret_key)
# token = requests.get(url=get_token_url).json().get("access_token")  # 从获取token接口的响应中取得token值
# # 识别图片文字
# orc_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}'.format(token)
# data = {"url": img_url}
# res = requests.post(url=orc_url, data=data)
# print(json.dumps(res.json(), indent=2, ensure_ascii=False)) # 格式化输出

# from test_login import Testlogin
# import unittest
#
# lg = Testlogin()
# login1 = lg.test_login_errorkey()

# login1 = Testlogin.test_login_normal()
# print(login1)

# suite = unittest.TestSuite()
# unittest.TextTestRunner(verbosity=2).run(suite)

import unittest
from lib.case_log import log_case_info
# suite = unittest.TestSuite()
# suite = unittest.defaultTestLoader.discover("./")
# suite.addTest(Testlogin('test_login_normal'))
# suite.addTests([Testlogin('test_login_normal'), Testlogin('test_login_errorkey'),
#                Testlogin('test_login_null'), Testlogin('test_login_cha')])
# unittest.TextTestRunner(verbosity=2).run(suite)

log_case_info('test_login_normal', 'http://192.168.9.212:8620/gateway/login', '{"key":"1IEuD18Z1ug=|k6NQq3efZgg="}', '成功', '成功')

