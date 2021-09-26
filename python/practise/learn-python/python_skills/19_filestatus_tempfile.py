#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    19_filestatus_tempfile.py
 @Function:    访问文件状态，使用临时文件
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/9/7
"""

"""一、如何访问文件的状态？"""

"""
实际案例：
    在某些项目中，我们需要获得文件状态,例如:
    1.文件的类型(普通文件,目录,符号链接,设备文件...). 
    2.文件的访问权限.
    3.文件的最后的访问/修改/节点状态更改时间.
    4.普通文件的大小.
    ......
"""

"""
解决方案：
    系统调用：标准库中os模块下的三个系统调用stat，fstat， lstat获取文件状态
    快捷函数：标准库中os.path下一些函数，使用起来更加简洁
"""

import os
import stat
import time

# touch a.txt && mkdir d && ln -s a.txt x.txt
s = os.stat('a.txt')
# os.stat_result(st_mode=33188, st_ino=28465047, st_dev=16777223, st_nlink=1, st_uid=501, st_gid=20, st_size=0, st_atime=1630973082, st_mtime=1630973082, st_ctime=1630973082)
print(s)

# 文件类型
print(stat.S_ISDIR(s.st_mode))  # False
print(stat.S_ISREG(s.st_mode))  # True

print(os.path.isdir('x.txt'))   # False
print(os.path.islink('x.txt'))  # True
print(os.path.isfile('a.txt'))  # True

# 文件访问权限
# -rw-r--r--  1 anzhihe  staff     0B  9  7 08:04 a.txt
print(s.st_mode & stat.S_IRUSR) # 256
print(s.st_mode & stat.S_IXUSR) # 0

# 文件状态更改时间
# time.struct_time(tm_year=2021, tm_mon=9, tm_mday=7, tm_hour=8, tm_min=4, tm_sec=42, tm_wday=1, tm_yday=250, tm_isdst=0)
print(time.localtime(s.st_atime))
# print(time.localtime(s.st_mtime))
# print(time.localtime(s.st_ctime))

print(os.path.getatime('a.txt'))    # 1630973663.346157
print(os.path.getmtime('a.txt'))    # 1630973660.6686056
print(os.path.getctime('a.txt'))    # 1630973660.6686056

# 普通文件大小
print(s.st_size)    # 4

print(os.path.getsize('a.txt')) # 4


"""二、如何使用临时文件？"""

"""
实际案例：
    某项目中，我们从传感器采集数据,每收集到1G数据后，
    做数据分析,最终只保存分析结果.这样很大的临时数据
    如果常驻内存，将消耗大量内存资源,我们可以使用临时
    文件存储这些临时数据(外部存储).
    
    临时文件不用命名，且关闭后会自动被删除.
"""

"""
解决方案：
    使用标准库中tempfile下的TemporaryFile，NamedTemporaryFile
"""

from tempfile import TemporaryFile, NamedTemporaryFile

# TemporaryFile()创建的临时文件在系统中找不到，只能通过文件句柄调用
f = TemporaryFile()
f.write(b'abcdefg' * 100)
# 访问临时数据，读入到内存中
f.seek(0)
# 每次导入一小部分
print(f.read(10))   # b'abcdefgabc'
print(f.read(10))   # b'defgabcdef'

ntf = NamedTemporaryFile(dir='/tmp')
# 输出文件系统下的文件路径，每次运行结束后会自动删除，不会保存
print(ntf.name) # /tmp/tmpyseriv1e

# ll /tmp/tmpyseriv1e
# ls: /tmp/tmpyseriv1e: No such file or directory

# 临时文件不自动删除
ntf = NamedTemporaryFile(dir='/tmp', delete=False)
print(ntf.name) # /tmp/tmpbvdrzkta

# ll /tmp/tmpbvdrzkta
# -rw-------  1 anzhihe  wheel     0B  9  7 08:36 /tmp/tmpbvdrzkta