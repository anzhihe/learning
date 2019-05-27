#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
列表使用中括号([])括起来，用,分割每个元素
列表是有序的，可以被修改，而字符串创建后不可修改
列表中可以嵌套任何数据类型，本质是集合，内部可以放置任何东西
列表元素修改和删除都可以通过切片操作
'''

'''
cast = ["Cleese",'Palin','Jones','Idle']
print(cast)
print(len(cast))
print(cast[1])

# append(): 从列表末尾增加一个数据项
cast.append("Gilliam")
print(cast)

# pop(): 删除某个值（1.默认最后一个 2.指定索引），并获取删除的值
cast.pop()
print(cast)

# extend(): 扩展原列表,各数据项之间腹膜逗号隔开,整个列表用中括号，参数：可迭代对象
cast.extend(["anzhihe","eto"])
print(cast)

# remove(): 从列表中找到并删除一个特定的数据项，左边优先
cast.remove("eto")
print(cast)

# insert(): 在某个特定的位置前面增加一个数据项
cast.insert(0,"Chapman")
print(cast)

li = [11, 22, 33, 44, 55, 22,10]

# clear()：清空列表
# li.clear()
# print(li)


# copy()：拷贝，浅拷贝
cp = li.copy()
print(cp)

# index()：根据值获取当前值索引位置（左边优先）
ind = li.index(22)
print(ind)

# reverse()：将当前列表进行翻转
li.reverse()
print(li)

# sort()：列表的排序
li.sort()
#li.sort(reverse=True) 降序排序
print(li)

# 字符串转换成列表，内部需使用for循环
s = "anzhiheehihzna"
new_li = list(s)
print(new_li)

# 列表转字符串：1.列表中的元素只有字符串，可以直接使用join方法
li_str = ["123", "anzhihe"]
new_li2 = "".join(li_str)
print(new_li2)

# 2.列表中元素既有数字又有字符串，需要自己写for循环一个一个处理
li_str2 = [11, 22, 33, "anzhihe"]
new_li3 = str(li_str2)
print(new_li3)
s1 = ""
for i in li_str2:
    s1 = s1 + str(i)
print(s1)

'''


'''
movies = ["The Holy Grail","The Life of Brian","The Meaning of Life"]
movies.insert(1,1975)
movies.insert(3,1979)
#movies.insert(5,1983)
movies.append(1983)
print(movies)

# 使用for循环迭代输出列表,for循环是可伸缩的,适用于任意大小的列表
fav_movies = ["The Holy Grail","The Life of Brian"]
for each_flick in fav_movies:
    print(each_flick)

# while遍历列表,需使用一个计数标识符
count = 0
while count < len(fav_movies):
    print(fav_movies[count])
    count += 1

######################################################################
'''

# isinstance(): 检查某个特定标识符是否包含某个特定类型的数据

names = ['anzhihe','Terry']
print(isinstance(names,list))

num_names = len(names)
print(isinstance(num_names,list))


# 在列表中查找列表
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
                ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)

print(movies)

# 使用递归函数,python3默认递归尝试不能超过100,如果希望嵌套更深,还可以改变这个深度上限
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)
