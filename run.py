import unittest
from lib.HTMLTestReportCN import  HTMLTestRunner
from lib.send_email import *
from config.config import *
import logging
from test.suite.test_suite import *
import time
import pydoc_data
logging.info("=====测试开始=======")
#  运行目录下所有test_开头的文件下的用例
# suite = unittest.defaultTestLoader.discover("./")
#  运行test文件夹下的test_开头的用例
suite = unittest.defaultTestLoader.discover(test_path)
unittest.TextTestRunner(verbosity=2).run(suite)

# 生产report下HTML的测试报告
with open(report_file, 'wb') as f:
    HTMLTestRunner(stream=f, title="api test", description="测试描述", tester="test01").run(suite)
# 发送邮件
send_email(report_file)
logging.info("============测试结束=======")

# f = open("report.html", 'wb')
# HTMLTestRunner(stream=f, title="api test", description="测试描述", tester="test01").run(suite)


# # 更灵活的运行方式
# def discover():
#     return unittest.defaultTestLoader.discover(test_path)
#
# def run(suite):
#     logging.info("。。。。。。。。测试开始。。。。。。。。。。")
#     with open(report_file, 'wb') as f:
#         HTMLTestRunner(stream=f, title="API Test", description="测试描述", tester="test01").run(suite)
#     logging.info("。。。。。。。。测试完成。。。。。。。。。")
#
# def run_all():
#     run(discover())
#
# def run_suite(suite_name):
#     suite = get_suite(suite_name)
#     if suite:
#         run(suite)
#     else:
#         print("TestSuite不存在")
#
#
# def collect():
#     suite = unittest.TestSuite()
#
#     def _collect(tests):
#         if isinstance(tests, unittest.TestSuite):
#             if tests.countTestCases() != 0:
#                 for i in tests:
#                     _collect(i)
#         else:
#             suite.addTest(tests)
#
#     _collect(discover())
#     return suite
#
# def collect_only():
#     t0 = time.time()
#     i = 0
#     for case in collect():
#         i += 1
#         print("{}.{}".format(str(i), case.id()))
#     print("-----------------------")
#     print("collect {} tests is {:.3f}s ".format(str(i), time.time()-t0))
#
# # 按testlist用例列表运行
# def makesuite_by_testlist(testlist_file):
#     with open(testlist_file) as f:
#         testlist = f.readlines()
#
#     testlist = [i.strip() for i in testlist if not i.startswith("#")]  # 去掉每行结尾的"/n"和 #号开头的行
#
#     suite = unittest.TestSuite()
#     all_cases = collect()
#     for case in all_cases:
#         if case._testMethodName in testlist:
#             suite.addTest(case)
#     return suite
#
# # 标记用例
# def makesuite_by_tag(tag):
#     suite = unittest.TestSuite()
#     for case in collect():
#         if case._testMethodName and tag in case._testMethodName:
#             suite.addTest(case)
#     return suite
