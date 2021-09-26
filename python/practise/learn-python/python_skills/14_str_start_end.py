#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    14_str_start_end.py
 @Function:    判断字符串a是否以字符串b开头或结尾
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/9/3
"""

"""如何判断字符串a是否以字符串b开头或结尾？"""

"""
实际案例：
    某文件系统目录下有一系列文件: 
    quicksort.c
    graph.py
    heap.java
    install.sh
    stack.cpp
    .....
    编写程序给其中所有.sh文件和.py文件加上用户可执行权限.
"""

"""
解决方案：
    使用字符串的str.startswith()和str.endswith()方法
    注意：多个匹配时参数要使用元组
"""

import os, stat

print(os.listdir('.'))

files = [fn for fn in os.listdir('.') if fn.endswith(('.sh', '.py'))]
print(files)

print(os.stat('a.sh').st_mode)  # 33188
# 转换成八进制输出
print("%o" % os.stat('a.sh').st_mode)  # 100644

# 增加用户可执行权限
os.chmod('a.sh', os.stat('a.sh').st_mode | stat.S_IXUSR)

#  ll a.sh
# -rwxr--r--  1 anzhihe  staff     0B Sep  3 09:02 a.sh