#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    dict_view_placeholder.py
 @Function:    dict view & placeholder
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/28
"""

"""一、字典的视图"""

"""
1、得到字典相关视图的三个方法：
    (1) keys：返回字典所有key的视图
    (2) values：返回字典所有value的视图
    (3) items：返回字典所有key-value对的视图
"""

d = {'name': 'Jack', 'age': 18}

keys = d.keys()
print(keys)         # dict_keys(['name', 'age'])
print(list(keys))   # ['name', 'age']

values = d.values()
print(values)       # dict_values(['Jack', 18])
print(list(values)) # ['Jack', 18]

items = d.items()
print(items)        # dict_items([('name', 'Jack'), ('age', 18)])
print(list(items))  # [('name', 'Jack'), ('age', 18)]

"""
2、视图会随字典的变化而随之变化
"""

d.pop('age')
print(d)    # {'name': 'Jack'}

print(keys)     # dict_keys(['name'])
print(values)   # dict_values(['Jack'])
print(items)    # dict_items([('name', 'Jack')])


"""二、借助字典创建格式化字符串"""

"""
1、使用百分号作为占位符
"""

phonebook = {'张三': '13333333333',
 '李四': '14444444444',
 '王五': '15555555555',
 '赵六': '16666666666'}

# 王五的号码：15555555555，张三的号码：13333333333
print('王五的号码：%s，张三的号码：%s' % (phonebook['王五'], phonebook['张三']))

"""
    当定义的格式化字符串中的占位符是百分号，并且占位符对应的实际值来自于某个字典的value时，
    可以把所有的实际值改写为字典，同时根据字典的value对应的key在占位符%的后面添加：(字典的key)
    其中，字典的key会被添加一对引号，因此，如果字典的key是字符串，需要去掉字典的key自带的引号
"""

# 王五的号码：15555555555，张三的号码：13333333333
print('王五的号码：%(王五)s，张三的号码：%(张三)s' % phonebook)

"""
2、使用花括号作为占位符
"""

phonebook = {'张三': '13333333333',
 '李四': '14444444444',
 '王五': '15555555555',
 '赵六': '16666666666'}

# 王五的号码：15555555555，张三的号码：13333333333
print('王五的号码：{}，张三的号码：{}'.format(phonebook['王五'], phonebook['张三']))

"""
    当定义的格式化字符串中的占位符是花括号，并且占位符对应的实际值来自于某个字典的value时，
    可以调用方法format_map并把该字典直接作为方法的参数，同时根据字典的value在花括号中指定对应的key：
    {字典的key}。其中，字典的key会被添加一对引号，因此，如果字典的key是字符串，需要去掉字典的key自带的引号 
"""

# 王五的号码：15555555555，张三的号码：13333333333
print('王五的号码：{王五}，张三的号码：{张三}'.format_map(phonebook))