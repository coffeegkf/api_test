# -*- coding: utf-8 -*-
# 列表的增删改查操作
# l = [1, "hello", ("a", "b")]
# a = l[0]
# print(a)
#
# l.append("c")
# print(l)
#
# l.extend(["d", "e"])
# print(l)
#
# l += ["f"]
# print(l)
#
# l.pop()
# print(l)
#
# l.remove("c")
# print(l)
#
# l[1] = "HELLO WORLD"
# print(l)
#
# for i in l:
#     print(i)

#  集合，去重
# ls = [1,2,3,1,4,3,2,5,6,2]
# ls = list(set(ls))
# print(ls)

#  # 字典增删改查操作
# d = {"a": 1, "b": 2}
# a = d['a']
# print(a)
#
# a = d.get('a')
# print(a)
#
# d["c"] = 3
# d.update({"d": 5, "e": 6})
# d.update({"d": 50})
# print(d)
#
# d.pop("d")
# print(d)
#
# # d.clear()
# # print(d)
#
# for key1 in d:
#     print(key1)
#
# for val in d.values():
#     print(val)
#
# for i in d.items():
#     print(i)

# api = { "url": "/api/user/login", "data": {"username": "张三", "password": "123456"}}
# print(api)
# api["data"]["username"] = "王二麻子"
# print(api)

# 三元表达式
# a = 1
# b = 2
# max = a if a > b else b
# print(max)

# #  判断一个字符串是不是IP地址
# ip_str = '192.018.0.9'
# ip_list = ip_str.split('.')
# is_ip = True
# if len(ip_list) != 4:
#     is_ip = False
# else:
#     for num in ip_list:
#         if (len(num) != 1 and num.lstrip('0') != num)or not 0<= int(num) <=255 or not num.isdigit():
#             is_ip = False
#
# if is_ip:
#     print(ip_str, "是IP")
# else:
#     print(ip_str, "不是IP")

# 函数定义和调用
# users = {"张三": "123456"}
#
# def reg(username, psw):
#     if users.get(username):
#         print("用户已存在", users.get(username))
#     else:
#         users[username] = psw
#         # users.update({username: psw})
#         print("添加成功", users)
#     # print(users)
#
#
# reg("张三1", "123456")

# 常用算法
# 冒泡排序
# def buddle_sort(under_sort_list):
#     l = under_sort_list
#     for j in range(len(l)):
#         for i in range(len(l)-j-1):
#             if l[i] > l[i+1]:
#                 l[i], l[i+1] = l[i+1], l[i]
#
#     return l

# 快速排序
# def quick_sort(l):
#     if len(l) < 2:
#         return l
#     else:
#         pivot = l[0]
#         low = [i for i in l[1:] if i < pivot]
#         high = [i for i in l[1:] if i >= pivot]
#         return quick_sort(low) + [pivot] + quick_sort(high)
#
#
# ls = quick_sort([3,1,7,6])
# print(ls)

# 二分查找
# def bin_search(l, n):
#     low, high = 0, len(l) - 1
#     while low < high:
#         mid = (high - low)//2
#         if l[mid] == n:
#             return mid
#         elif l[mid] > n:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None

# 读取文件中每行数据
# f = open("text.txt")
# ls = f.readlines()

# 打印每行数据
# for i in ls:
#     print(str(i).strip(), "长度：", len(str(i).strip()))

# 判断文件中最长的行
# m = 0
# for i in ls:
#     l = len(str(i).strip())
#     if l > m:
#         m = l
#         n = i
# print("最长的行：", m, n)

# f = open("text.txt").read()
# print(f)
# count_dg = 0
# # 判断文件中数字个数
# for s in f:
#     if s.isdigit():
#         count_dg = count_dg+1
# print(count_dg)
# # 判断文件中中英文个数
# count_zh = 0
# for s in f:
#     if s.isalpha():
#         count_zh = count_zh+1
# print(count_zh)


# 判断字符串中第一个不重复的字符
str = "aaa"
ls = []
for s in str:
    ls.append(s)
print(ls)
for m in ls:
    b = 0
    n = 0
    while b < len(ls):
        if m != ls[b]:
            b += 1
        else:
            n += 1
            b += 1
    if n == 1:
        print(m)
        break
if n != 1:
    print("没有不重复字符")
























