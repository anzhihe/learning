#!/usr/bin/env python3
# coding: utf8

'''
元组，元素不可被修改，增加，删除（一级元素）
使用（）定义，可以允许加入所有数据类型
元组是有序的,是可迭代对象
一般写元组的时候，推荐在最后加入 ,
'''

tu = (111,"chegva",(11,22),[(33,44)],True,33,44,111,22,11,)

# count()：获取指定元素在元组中出现的次数
tu_num = tu.count(111)
print(tu_num)

# index()：查找元素位置
tu_ind = tu.index(33)
print(tu_ind)

# 索引
ind = tu[0]
print(ind)

# 切片
sli = tu[0:2]
print(sli)

# 可以被for循环，可迭代对象
for item in tu:
    print(item)

# 转换
str_tu = "chegva.com"
list_tu = ["anzhihe", "chegva"]
tu_list = ("anzhihe", "chegva",)

res1 = tuple(str_tu)
print(res1)

res2 = tuple(list_tu)
print(res2)

res3 = list(tu_list)
print(res3)

res4 = "_".join(tu_list)
print(res4)

list_ext = ["test", "chegva"]
list_ext.extend((11,22,33))
print(list_ext)
