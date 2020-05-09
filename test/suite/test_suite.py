import unittest
import sys
sys.path.append("../..")
from test.user.test_login import *

smoke_suite = unittest.TestSuite()
smoke_suite.addTest([TestUserLogin('test_login_normal'), TestUserLogin('test_login_errorkey')])

def get_suite(suite_name):
    return globals().get(suite_name)