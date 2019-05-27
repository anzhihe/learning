#!/usr/bin/env python
# coding: utf8

score = raw_input("Please input your score: ")
score = int(score)

if score < 0:
    print '你输入错误'
elif score < 60:
    print '不及格'
elif score < 70:
    print '一般'
elif score < 80:
    print '良好'
elif score < 90:
    print '优良'
elif score <= 100:
    print '优秀'
else:
    print '你输入错误'