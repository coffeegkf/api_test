import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(prj_path, 'data')
test_path1 = os.path.join(prj_path, 'test')
test_path = os.path.join(test_path1, 'user')


log_file = os.path.join(prj_path, 'log',  'log.txt')
report_file = os.path.join(prj_path, 'report',  'report.html')
data_file = os.path.join(data_path, "test_user_data.xlsx")
testlist_file = os.path.join(test_path1, "testlist.txt")
# log配置
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]%(levelname)s [%(funcName)s: %(filename)s, '
                                                '%(lineno)d] %(message)s',
                    datefmt='%Y-%m_%d %H:%M:%S',
                    filename=log_file,
                    filemode='a')

# 数据库配置
db_host = '114.116.210.74'
db_port = 3306
db_user = 'shield'
db_password = '!BShield520'
db = 'blueshield'

# 邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '565097150@qq.com'
smtp_password = 'dnkxchyfsxnzbbhb'

sender = smtp_user
receiver = '565097150@qq.com'
subject = '接口测试报告'