import pymysql
import sys
sys.path.append('..')
from config.config import *
'''
# 第一种封装方法（缺点：每次操作都需要连接数据库，效率低）
# 获取数据库连接
def sql_conn():
    conn = pymysql.Connect(
        host='114.116.210.74',
        port=3306,
        user='shield',
        passwd='!BShield520',
        db='blueshield',
        charset='utf8'
       )
    return conn

# 封装查询语句
def query_db(sql):
    conn = sql_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()

    for row in result:
        print(row)
    print("结果数：", cur.rowcount)
    return result


# 封装更改语句
def change_db(sql):
    conn = sql_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        result = cur.rowcount
        print("受影响行数：", result, "行")
    except Exception as e:
        conn.rollback()
        print(str(e))
    finally:
        cur.close()
        conn.close()

# 封装常用数据库操作

def check_user(name):
    sql = "select * from sys_user where name='{}'".format(name)
    result = query_db(sql)
    return True if result else False
def del_user(name):
    sql = "delete from sys_user where name='{}'".format(name)
    result = change_db(sql)
'''

class DB:
    def __init__(self):
        self.conn = pymysql.Connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            db=db,
            charset='utf8')

        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
    #  返回结果中的20个数据，fetchall 返回所有结果，fetchone返回第一个结果
        result = self.cur.fetchmany(20)
    #  返回被影响的行数
        num = self.cur.rowcount
        return result, num

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print(self.cur.rowcount)
        except Exception as e:
            # 发生异常，数据回滚
            self.conn.rollback()
            print(str(e))

    def check_user(self, name):
        result = self.query("select * from sys_user where name='{}'".format(name))
        return True if result else False

    def del_user(self, name):
        self.exec("delete from sys_user where name='{}'".format(name))
