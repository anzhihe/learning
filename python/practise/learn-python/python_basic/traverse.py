#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    traverse.py
 @Function:    python traverse
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/1
"""

"""一、带索引的序列遍历"""

L = ['Java', 'Python', 'Swift', 'Kotlin']

"""
    如果在遍历序列的过程中需要访问元素的索引，有以下几种实现方式：
1、第一种实现方式
"""

index = 0
for item in L:
    print('L[{}] = {}'.format(index, item))
    index += 1

"""
2、第2种实现方式
"""

for index in range(len(L)):
    print('L[{}] = {}'.format(index, L[index]))

"""
3、第3种实现方式
"""

index = 0
while index < len(L):
    print('L[{}] = {}'.format(index, L[index]))
    index += 1

"""
4、第4种实现方式
    可以调用内置函数enumerate(类enumerate的构造方法)将要遍历的序列转换为enumerate对象
"""

print(enumerate(L)) # <enumerate object at 0x10e11cd00>

# 为了清楚地表示返回的enumerate对象所表示的内容，可以将enumerate对象转换成列表
# [(0, 'Java'), (1, 'Python'), (2, 'Swift'), (3, 'Kotlin')]
print(list(enumerate(L)))

# 调用内置函数enumerate时，可以通过第二个参数指定索引的起始值
# [(1, 'Java'), (2, 'Python'), (3, 'Swift'), (4, 'Kotlin')]
print(list(enumerate(L, 1)))

# 既可以遍历enumerate对象转换后的列表，也可以直接遍历enumerate对象
for index, item in list(enumerate(L)):
    print('L[{}] = {}'.format(index, item))

for index, item in enumerate(L):
    print('L[{}] = {}'.format(index, item))


"""二、并行遍历"""

"""
    有时可能需要同时遍历多个可迭代对象，也就是并行遍历。例如：列表names中存放姓名，
    列表ages中存放对应的年龄。如果想同时遍历这两个列表，打印出所有的姓名及对应的年龄，可以这样实现：  
"""

names = ['Jack', 'Mike', 'Tom']
ages = [16, 32, 43]

for i in range(len(names)):
    print(names[i], '的年龄是：', ages[i])

"""
    上述的解决方案有更好的替代。如果需要同时遍历多个可迭代对象，可以调用内置函数zip(类zip的构造方法)
    将多个可迭代对象打包压缩成zip对象
"""

print(zip(names, ages)) # <zip object at 0x10afa60c0>

"""
    为了清楚地表示返回的zip对象所表示的内容，可以将zip对象转换成列表
"""

# 列表中的元素都是元组，元组中的第i个元素来自调用zip时的第i个参数
print(list(zip(names, ages)))   # [('Jack', 16), ('Mike', 32), ('Tom', 43)]

# 既可以遍历zip对象转换后的列表，也可以直接遍历zip对象
for name, age in list(zip(names, ages)):
    print(name, '的年龄是：', age)
for name, age in zip(names, ages):
    print(name, '的年龄是：', age)

"""
    调用内置函数zip将多个可迭代对象进行打包压缩时，如果两个可迭代对象的长度不同，那么较长的可迭代对象会被截断
"""

print(list(zip(range(3), range(5))))    # [(0, 0), (1, 1), (2, 2)]

# 可以使用*对zip对象解压缩
x = [1, 2, 3]
y = [4, 5, 6]

print(list(zip(x, y)))  # [(1, 4), (2, 5), (3, 6)]
print(list(zip(*zip(x, y))))  # [(1, 2, 3), (4, 5, 6)]

x2, y2 = zip(*zip(x, y))
print(list(x2)) # [1, 2, 3]
print(list(y2)) # [4, 5, 6]


"""三、遍历可迭代对象的内置函数map和filter"""

"""
1、遍历可迭代对象的内置函数map
    第一个参数指定函数名，第二个参数指定可迭代对象
    调用内置函数map后，会使用指定的函数名作用于指定的可迭代对象的每个元素，
    然后生成新的可迭代对象
"""

result = map(ord, 'abcd')
print(result)   # <map object at 0x109dd1700>
print(list(result)) # [97, 98, 99, 100]

# str.upper表示类str的方法upper，也就是字符串的方法upper
result = map(str.upper, 'abcd')
print(result)   # <map object at 0x105adc760>
print(list(result)) # ['A', 'B', 'C', 'D']

"""
2、用于遍历可迭代对象的内置函数filter
    第一个参数指定函数名，第二个参数指定可迭代对象
    调用内置函数filter后，会使用指定的函数名作用于指定的可迭代对象的每个元素，
    过滤掉函数返回值为False的相关元素，然后生成新的可迭代对象
"""

result = filter(str.isalpha, '123abc')
print(result)   # <filter object at 0x102d19760>
print(list(result)) # ['a', 'b', 'c']
