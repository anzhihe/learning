#!/usr/bin/env python3
# coding: utf8

'''
定义：用', ", """,引起来的连续字符串，只要为变量分配一个值即可，可以使用方括号来截取字符串。
字符串一旦创建，将不可修改。一旦修改或者拼接，将会重新生成字符串。
Python 3的字符串使用Unicode，直接支持多语言。
字符串是可迭代的，可以使用切片，索引获取元素

字符串索引规则：
1.第一个字符的索引是0
2.最后一个字符的索引是-1
加号(+)用于字符串连接运算，星号(*)用于字符串重复
'''

# 1.capitalize()：首字母大写
str1 = "anzhihe"
res1 = str1.capitalize()
print(res1)

# 2.casefold()：所有变小写
str2 = "CheGva"
res2 = str2.casefold()
print(res2)

# 3.center()、ljust()、rjust()、zfill()，设置宽度，填充指定字符
str3 = "chegva"
res3 = str3.center(20, "中")
print(res3)

res4 = str3.ljust(20, "*")
print(res4)

res5 = str3.rjust(20, "#")
print(res5)

res6 = str3.zfill(20)
print(res6)

# 4.count()：在字符串中寻找子序列出现的次数
str4 = "anzhihechegva"
res7 = str4.count('he')
print(res7)

res8 = str4.count('he',6,10)
print(res8)

# 5.endswith()、startswith()：判断字符串以什么字符结尾和开始
str5 = "anzhihe"
res9 = str5.endswith('he')
print(res9)

res10 = str5.startswith('he')
print(res10)

# 6.expandtabs()：把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
str6 = "username\temail\tpassword\nanzhihe\tchegva@eto.com\t123\nanzhihe\tchegva@eto.com\t123\nanzhihe\tchegva@eto.com\t123"
res11 = str6.expandtabs(20) #20个空格代替\t符号
print(res11)

# 7.find()：查找子字符串返回开始的索引值（找到第一个之后），否则返回-1。
str7 = "chegvacheva"
res12 = str7.find('he')
print(res12)
res13 = str7.find('an')
print(res13)

# 8.index()：与find类似，检察是否包含在字符串指定范围内，没找到时返回异常
# res14 = str7.index('11')
# print(res14)

# 9.format()：格式化，将一个字符串中的占位符替换成指定的值
str8 = 'My name is {name}, age {age}'
print(str8)
res15 = str8.format(name='anzhihe', age=99)
print(res15)
res16 = str8.format_map({"name":'yaya', 'age':1})
print(res16)


str9 = 'My name is {0}, age {1}'
print(str9)
res17 = str9.format('chegva', 999)
print(res17)

# 10.isalnum()：字符串所有字符是否是字母或数字,或两者组合
str10 = "123456"
res18 = str10.isalnum()
print(res18)

str11 = "123.456"
res19 = str11.isalnum()
print(res19)

# 11.isalpha()：检察字符串是否只由字母组成
str12 = "chegva.com"
res20 = str12.isalpha()
print(res20)

# 12.isdecimal()、isdigit()、isnumeric() 检察当前输入是否是数字
str13 = "安"
res21 = str13.isdecimal()
res22 = str13.isdigit()
res23 = str13.isnumeric()
print(res21, res22, res23)

# 13.isprintable()：是否存在不可显示的字符 \t 制表符 \n 换行符
str14 = "anziher\t4343"
res24 = str14.isprintable()
print(res24)

# 14.isspace()：判断字符串是否全部是空格
str15 = ""
res25 = str15.isspace()
print(res25)

# 15.istitle()：字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
#  title()：返回"标题化"的字符串,就是说所有单词的首个字母转化为大写，其余字母均为小写
str16 = "If I should see you，after long year.How should I greet, with tears, with silence."
res26 = str16.istitle()
print(res26)
res27 = str16.title()
print(res27)
res28 = res27.istitle()
print(res28)

# 16.join()：将字符串中的每一个元素按照指定分隔符进行拼接
str17 = "潇洒走一回"
res29 = "_".join(str17)
print(res29)

# 17.回来大小写
# islower()：判断字符串是否全部是小写字符
# lower()：所有大写字符转换成小写
# isupper()：判断字符串是否全部是大写字符
# upper()：所有小写字符转换成大写
# swapcase()：对字符串的大小写字母进行转换
str18 = "Chegva"
res30 = str18.islower()
res31 = str18.lower()
print(res30, res31)

res32 = str18.isupper()
res33 = str18.upper()
res34 = str18.swapcase()
print(res32,res33,res34)

# 18.isidentifier()：检测字符串是否是字母开头
str19 = "chegva"
res35 = str19.isidentifier()
print(res35)

str20 = "1fdfdfd"
res36 = str20.isidentifier()
print(res36)

# 19.检察字符串开关和结尾
# startswith()：检查字符串是否是以指定子字符串开头
# endswith()：检查字符串日影不是以指定子字符串结尾
str21 = "chegva.com"
res37 = str21.startswith('a')
print(res37)

res38 = str21.endswith('com')
print(res38)


# 20.str.replace(old, new[, max])：把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
str22 = "chegva.comheheanzhihe"
res39 = str22.replace("he","HE")
print(res39)

res40 = str22.replace("he","HE",2)
print(res40)

# 21.对应关系替换
# maketrans():用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 两个字符串的长度必须相同，为一一对应的关系。
# translate()：根据参数table给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中。
str23 = "this is string example....wow!!!"
intab = "aeiou"
outtab = "12345"
trantab = str23.maketrans(intab, outtab)   # 制作翻译表

print (str23.translate(trantab))

# 22.分割
# split(str="", num=string.count(str))：通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
# partition(str)：符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
# rpartition(str):类似于 partition() 方法，只是该方法是从目标字符串的末尾也就是右边开始搜索分割符。
# splitlines([keepends])：按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
str24 = "this is string example....wow!!!"
print (str24.split( ))
print (str24.split('i',1))
print (str24.split('w'))

str25 = "www.chegva.com"
print(str25.partition("."))
print(str25.rpartition("."))

# >>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
# ['ab c', '', 'de fg', 'kl']
# >>> 'ab c\n\nde fg\rkl\r\n'.splitlines(True)
# ['ab c\n', '\n', 'de fg\r', 'kl\r\n']


# 23.移除指定字符串
# lstrip()：移除字符串左边的空格或指定字符
# rstrip()：删除字符串末尾的空格
# strip()：在字符串上执行lstrip()和rstrip()
str26 = "     this is string example....wow!!!     ";
print( str26.lstrip() );
str27 = "88888888this is string example....wow!!!8888888";
print( str27.lstrip('8') );

str28 = "     this is string example....wow!!!     "
print (str28.rstrip())
str29 = "*****this is string example....wow!!!*****"
print (str29.rstrip('*'))

str30 = "*****this is **string** example....wow!!!*****"
str31 = "123chegva.com3212121"
print(str30.strip( '*' ))  # 指定字符串 *
print(str31.strip('12'))


