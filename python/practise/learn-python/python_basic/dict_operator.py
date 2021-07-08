#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    dict_operator.py
 @Function:    dict operator
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/28
"""

"""一、字典的"查"操作"""

"""
如果想在字典中根据指定的key查找对应的value，常见的方式有两种：
1、使用中括号
"""

d = {'name': 'Jack', 'age': 18}
print(d['name'])    # Jack

# 如果字典中不存在指定的key，抛出KeyError
# print(d['gender'])  # KeyError: 'gender'

"""
2、调用方法get
"""

print(d.get('name'))    # Jack

# 如果字典中不存在指定的key，并不会抛出KeyError，而是返回None
print(d.get('gender'))  # None

"""
    可以通过参数设置默认的value，以便在字典中不存在指定的key时将其返回
"""

print(d.get('gender', '男')) # 男

"""
    此外，可以使用运算符in(not)检查字典中是否存在(不存在)指定的key
"""

print('age' in d)       # True
print('gender' in d)    # False

print('age' not in d)       # False
print('gender' not in d)    # True


"""二、字典的"改"操作"""

"""
如果想要修改字典中指定的key对应的value，常见的方式有两种：
1、为已经存在的key赋予一个新的value值(一次只修改一个key对应的value)
"""

d = {'name': 'Jack', 'age': 18, 'gender': '男'}
d['age'] = 20
print(d)    # {'name': 'Jack', 'age': 20, 'gender': '男'}

"""
2、调用方法update(一次至少修改一个key对应的value)
"""

d = {'name': 'Jack', 'age': 18, 'gender': '男'}

# d.update({'name': 'Mike', 'age': 20})
# d.update([('name', 'Mike'), ('age', 20)])
d.update(name = 'Mike', age = 20)

print(d)    # {'name': 'Mike', 'age': 20, 'gender': '男'}


"""三、字典的"增"操作"""

"""
如果想要往字典中添加key-value时，常见的方式有两种：
1、为不存在的key赋予一个value值(一次只添加一个key-value对)
"""

d = {'name': 'Jack', 'age': 18}
d['gender'] = '男'
print(d)    # {'name': 'Jack', 'age': 18, 'gender': '男'}

"""
二、调用方法update(一次至少添加一个key-value对)
"""

d = {'name': 'Jack', 'age': 18}

# d.update({'gender': '男', 'score': 90})
# d.update([('gender', '男'), ('score', 90)])
d.update(gender = '男', score = 90)

print(d)    # {'name': 'Jack', 'age': 18, 'gender': '男', 'score': 90}


"""四、字典的"删"操作"""

"""
如果想要删除字典中的key-value对，常见的方式有四种：
1、调用方法pop(一次只删除一个指定key的key-value对)
    该方法返回指定的key对应的value
"""

d = {'name': 'Jack', 'age': 18, 'gender': '男'}
print(d.pop('age')) # 18
print(d)    # {'name': 'Jack', 'gender': '男'}

# 如果指定的key不存在，抛出KeyError
# d.pop('score')  # KeyError: 'score'

# 为了防止指定的key不存在时抛出KeyError,可以通过参数指定一个默认返回的value
print(d.pop('score', 90))   # 90

"""
2、使用del语句(一次只删除一个指定key的key-value对)
"""

d = {'name': 'Jack', 'age': 18, 'gender': '男'}
del d['age']
print(d)    # {'name': 'Jack', 'gender': '男'}

"""
3、调用方法popitem(一次只删除一个任意的key-value对)
    该方法返回被删除的key-value对
"""

d = {'name': 'Jack', 'age': 18, 'gender': '男'}
print(d.popitem())  # ('gender', '男')
print(d)    # {'name': 'Jack', 'age': 18}

"""
4、调用方法clear清空字典
"""

d = {'name': 'Jack', 'age': 18, 'gender': '男'}
d.clear()
print(d)    # {}


"""五、为字典中指定的key设置默认的value值"""

"""
    为了确保字典中指定的key总是存在的，可以调用方法setdefault，这样，
    (1) 如果字典中存在指定的key，该方法返回指定的key对应的value，字典不发生变化
    (2) 如果字典中不存在指定的key，该方法返回指定的默认value的值，字典中添加一个key-value对：
        "指定的key：指定的默认value值"。此时，调用方法setdefault相当于语句：if...not in...
"""

d = {'name': 'Jack'}
print(d.setdefault('name', 'defaultName'))  # Jack
print(d)    # {'name': 'Jack'}

d = {}
print(d.setdefault('name', 'defaultName'))  # defaultName
print(d)    # {'name': 'defaultName'}

if 'name' not in d:
    d['name'] = 'defaultName'
