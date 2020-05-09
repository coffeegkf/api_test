import xlrd
import os
from config.config import *
# 打开Excel表
wb = xlrd.open_workbook(os.path.join(data_path, "test_user_data.xlsx"))
# 打开第一个页卡
sh = wb.sheet_by_name("TestUserLogin")
# 打印表的行数
print(sh.nrows)
# 打印表的列数
print(sh.ncols)
# 打印第一行第一列的值
print(sh.cell(0, 0).value)
# 打印第一行的值，即列名
print(sh.row_values(0))

# 第一行与第二行值形成字典
print(dict(zip(sh.row_values(0), sh.row_values(1))))

#遍列每行，打印每行的值
for i in range(sh.nrows):
    print(sh.row_values(i))
