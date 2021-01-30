#coding:utf-8
import re
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d+')
# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern,'192abc')
if result1:
    print result1.group()
else:
    print '匹配失败1'
result2 = re.match(pattern,'abc192')
if result2:
    print result2.group()
else:
    print '匹配失败2'
