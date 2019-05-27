#!/usr/bin/env python3
# coding: utf8

'''
set集合：
set是一个无序且不重复的元素集合
1.集合由不同元素组成，元素不重复
2.集合中的元素必须是不可变类型（数字、字符串、元组）
3.集合是无序的

主要作用：
1.去重
2.关系测试，测试两组数据之间的交集、并集、差集等关系
'''

set_1 = set('chegva.com')
print(set_1)


set_2 = set(['anzhihe','chegva','hehe'])
print(set_2)

set_3 = {1,3,2,3,5,6}

# 添加:add
set_3.add('s')
# set_3.add('4')
# set_3.add(4)
print(set_3)

# len()：set的长度
print(len(set_3))

# 清除集合元素：clear()
# set_3.clear()
# print(set_3)

# 返回 set 的一个浅复制：copy()
set_4 = set_3.copy()
print(set_4)

# 随机删除set里的元素：pop()
set_5 = {'chegva',1,2,3,4,5,6}
set_5.pop()

#指定删除：remove()
set_5.remove('chegva')
# set_5.remove('hehe') #删除元素不存在会报错
# set_5.discard('haha') #删除元素不存在不会报错
print(set_5)


set_6 = ['chegva', 'com', 'anzhihe', '123']
set_7 = ['chegva', 'com', '456']
set_8 = set(set_6)
set_9 = set(set_7)

# 求交集：intersection(), &
print(set_8, set_9)
print(set_8.intersection(set_9))
# print(set_8&set_9)

# 求并集：union(), |
print(set_8.union(set_9))
# print(set_8|set_9)

# 差集：differenct()，-
print('差集:',set_8 - set_9)
# print(set_8.difference(set_9))
print('差集:',set_9 - set_8)
# print(set_9.difference(set_8))

# 返回一个新的 set 包含 set_8 和 set_9 中不重复的元素
# 交叉补集：symmetric_difference(), ^
print('交叉补集:',set_8.symmetric_difference(set_9))
# print('交叉补集:',set_8 ^ set_9)

# difference_update()
set_10 = set_8 - set_9
set_10.difference_update(set_9)
print(set_10)


set_11 = {1,2}
set_12 = {2,3,5}
print(set_11.isdisjoint(set_12))

# 判断子集：issubset()
s1={1,2}
s2={1,2,3}
print(s1.issubset(s2)) # s1 是 s2 的子集
print(s2.issubset(s1)) # False

print(s2.issuperset(s1)) # s1 是 s2 的父集

set_13 = {1,2}
set_14 = {1,2,3}
set_13.update(set_14) # 更新多个值

# set_13.add(1,2,3,4) # 更新一个值
# set_13.union(set_14) # 不更新
print(set_13)


set_15 = frozenset('chegva.com')
print(set_15)
names=['anzhihe','chegva','com']
names=list(set(names))
print(names)