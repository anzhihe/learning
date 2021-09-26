#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    01_data_filter.py
 @Function:    在列表、字典、集合中根据条件筛选数据
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/20
"""

"""一、过滤掉列表中的负数"""

"""
1、使用迭代，最通用的写法，效率很一般，速度最慢
"""

data = [1, 6, -3, -2, 5, 0, 9, 8, 7, 4]

res = []
for x in data:
    if x >= 0:
        res.append(x)

print(res)  # [1, 6, 5, 0, 9, 8, 7, 4]

"""
2、使用filter函数，效率提升很大
"""

from random import randint

# 使用列表解析随机生成值在-10到10之间的10个元素
data = [randint(-10, 10) for _ in range(10)]
print(data)     # [4, -6, 7, 8, -3, -4, 6, 0, 6, -10]

# 使用filter过滤
print(list(filter(lambda x: x >= 0, data))) # [4, 7, 8, 6, 0, 6]

"""
使用ipython timeit测下运行时间
In [9]: timeit filter(lambda x: x >= 0, data)
148 ns ± 7.19 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
"""

"""
3、使用列表解析，效率比filter要差一些，但比较直观
"""

print([x for x in data if x >= 0])   # [4, 7, 8, 6, 0, 6]

"""
In [15]: timeit [x for x in data if x >= 0]
377 ns ± 8.39 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
"""


"""二、筛出字典中值高于90的项"""

# 随机生成20个字典元素，且值在60到100间
score = {x: randint(60, 100) for x in range(1, 21)}

# 使用字典解析
print({k: v for k, v in score.items() if v > 90})   # {2: 99, 4: 91, 9: 96}


"""三、筛出集合中能被3整除的元素"""

s = set(data)
print(s)    # {-10, -6, -3, -2, -1, 2, 4, 6, 8}

# 使用集合解析
print({x for x in s if x % 3 == 0}) # {-6, -3, 6}
