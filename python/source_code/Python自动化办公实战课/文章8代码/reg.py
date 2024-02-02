# 字符串s是一个手机号
s = "13855556666"

digit = s.isdigit() 

len11 = len(s)==11

print(f'字符串是否是数字 {digit}')
print(f'字符串的长度是否为11个 {len11}')


import re

re.search("[0-9]{11}","13855556666")
# <re.Match object; span=(0, 11), match='13855556666'> #执行结果

# 使用元字符.匹配字符串
points = re.search(".....","aaa13855557890bbb")
print(points)

yesno = re.search("(Y|y)(es)*","aayesbb").group(0)
print(f'yesno is {yesno}')

# 将字符串中的yes替换为no
print(re.sub("(Y|y)(es)*", "No","aayesbb"))

