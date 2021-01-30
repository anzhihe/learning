#coding:utf-8
import re
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d+')
# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.search(pattern,'abc192edf')
if result1:
    print result1.group()
else:
    print '匹配失败1'
