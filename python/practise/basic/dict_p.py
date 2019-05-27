#!/usr/bin/env python3
# coding: utf8

'''
字典用大括号{}包含或dict定义，每个元素是由key，value组成key:value对,每个元素间通过逗号分隔
布尔值(1,0)、列表、字典不能作为字典的key，字典的value可以是任何值
字典是无序的，可以通过索引找到指定元素，字典支持del删除
'''

dic = {
    "k1": 'v1',
    "k2": 'v2'
}

# 1.根据序列，创建字典，并指定统一的值
dic_1 = dict.fromkeys(["k1", 111, "chegva"],123)
print(dic_1)

# 2.根据Key获取值，key不存在时可以指定默认值(None)
#dic_key = dic.['k111']\
dic_key = dic.get('k1',111111)
print(dic_key)

# 3.删除并获取值
#dic_del = dic.pop('k1',66)
#print(dic_del)
#k,v = dic.popitem()
#print(dic,k,v)

# 4.设置值，已存在的不设置，不存在才设置，都会获取当前key对应的值
dic_set = dic.setdefault('k1',123)
print(dic_set)
dic_set1 = dic.setdefault('k11111',123)
print(dic,dic_set1)

# 5.更新
dic.update({'k1':'111111','k3':123})
print(dic)
dic.update(k1=123,k3=345,k5="che")
print(dic)