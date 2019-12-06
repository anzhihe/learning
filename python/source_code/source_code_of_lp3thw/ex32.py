the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list for number in the_count
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type:{fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:#这里可以是一个通用的算法:i表示一个“列表”中的任意一项。
    print(f"I got {i}")

# we can also build lists ,first start with an empty one elements = []
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was:{i}")

#对line22进行直接赋值。直接将elements赋值为range(0,6),下面进行测试。
elements2 = range(0,6)

for i in elements2:
    print(f"Element2 was:{i}")

'''
# 这个程序代码很好玩。可以利用for 循环往数组里添加和读取信息。

运行后结果：

bogon:LP3THW yyy$ python ex32.py
This is count 1
This is count 2
This is count 3
This is count 4
This is count 5
A fruit of type:apples
A fruit of type:oranges
A fruit of type:pears
A fruit of type:apricots
I got 1
I got pennies
I got 2
I got dimes
I got 3
I got quarters
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
Element was:0
Element was:1
Element was:2
Element was:3
Element was:4
Element was:5

'''
