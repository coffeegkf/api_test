# db = pymysql.Connect(
#     host='114.116.210.74',
#     port=3306,
#     user='shield',
#     passwd='!BShield520',
#     db='blueshield',
#     charset='utf8')
# # 获取游标
# cursor = db.cursor()
#
# # 查询语句
# sql = "select * from sys_user"
# # 执行游标
# cursor.execute(sql)
# # 返回结果列表第一条数据
# print(cursor.fetchone())
# # 返回结果列表所有数据
# print(cursor.fetchall())
# # 逐条打印查询结果
# for row in cursor.fetchall():
#     print(row)
# print('条数', cursor.rowcount)
# cursor.close()
# db.close()
#
# # 插入语句
# sql = "insert into sys_user (id,username, password, name, real_name, phone, email) " \
#     "values ('323245039824016','13645614561', '112233', '测试','测试', '13645614561','142@163.com')"
# cursor.execute(sql)
# db.commit()
# print('成功插入', cursor.rowcount, '数据')
#
# # 删除数据
# sql = "delete from sys_user where id = '323245039824016'"
# cursor.execute(sql)
# db.commit()
# print('删除成功', cursor.rowcount, '条数')
#
# # try...except的使用
# sql = "select * from sys_user where id like '%423%'"
# try:
#     cursor.execute(sql)
#     result = cursor.fetchall()
#
#     # 如果查询结果不为空，返回结果，如果为空，返回无数据
#     if result:
#         for row in result:
#             print(row)
#     else:
#         print("无数据")
# except:
#     print('查询失败')

# cur = db.cursor()
# sql1 = "insert into sys_user (id,username, password, name, real_name, phone, email) " \
#     "values ('323245039824016','13645614561', '112233', '测试1','测试1', '13645614561','142@163.com')"
#
# sql2 = "insert into sys_user (id,username, password, name, real_name, phone, email) " \
#     "values ('323245039824016','13645614561', '112233', '测试1','测试1')"
#
# try:
#     cur.execute(sql1)
#     cur.execute(sql2)
#     db.cursor()
# except Exception as e:
#     db.rollback()
#     print(str(e))

# result = dbfuction.query_db("select * from sys_user where name like '%张%'")


# dbfuction.change_db("update sys_user set name='郭康芬' where name='郭康芬测试'")
# dbfuction.change_db("insert into sys_user (id,username, password, name, real_name, phone, email) "
#                     "values ('323245039824016','13645614561', '112233', '测试1','测试1', '13645614561','142@163.com')")

# result = dbfuction.check_user("测试1")
# if result:
#     dbfuction.del_user("测试1")
# else:
#     print("无查询数据")

'''第二种封装方法，先实例化类'''
from lib.dbfuction import DB

db = DB()
# result = db.query("select * from sys_user where name like '%张%'")
# for row in result[0]:
#     print(row)
# print(result[1])

db.exec("insert into sys_user (id,username, password, name, real_name, phone, email) "
        "values ('323245039824016','13645614561', '112233', '测试1','测试1', '13645614561','142@163.com')")

if db.check_user("测试1"):
    db.del_user("测试1")


