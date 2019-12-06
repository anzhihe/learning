ten_things = "Apples Oranges Crows Telephone Light Sugar"# 定义了个变量接受字符串,还有6个东西，这些字符间有空格。

print("Wait there are not 10 things in the list. Let's fix that.")#打印提示，说这个变量中不包含10个东西，下面将要填充它。

stuff = ten_things.split(' ')#对于上面这个变量使用.split()方法，也即是“分裂”方法，往其中添加空格，之后赋值给了新变量stuff。
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]#建立一个含有8个量的列表数据结构，赋值给more_stuff变量。


while len(stuff) != 10:#采用while循环，使用len()函数，判断stuff变量的长度，如果不等于10就继续执行，直到等于10.
    next_one = more_stuff.pop()#对于more_stuff采用pop()函数（方法？）pop（）函数用于移除列表中的一个元素（默认是最后一个），并返回该该元素值。赋值给了新变量next_one
    print("Adding:", next_one)#打印出来说，我要“增加一个”元素进来，增加的这个元素就是next_one，也就是more_stuff这个列表中的最后一个元素，第一个循环时候是"Boy"
    stuff.append(next_one)#对于stuff变量，使用了append方法，增加了这个next_one元素到里面，也就是说stuff变量增长了。
    print(f"There are {len(stuff)} items now. ")#这里打印出来一句话，字符串中内嵌了一个变量 {len(stuff)}，也就是说stuff的长度。stuff的长度是以空格界定的？

print("There we go:", stuff)#执行完上述循环后，打印出一行字，这个打印里包含了一个字符串，并且还包含了一个变量stuff(这是个列表变量？)请注意这中字符串+变量的打印方法。
print(f"There we go again:{stuff}")#这里试试另一种表达方式，这一行是我自己加进去的。可行。
print("Let's do some things with stuff.")#打印一行字。

print(stuff[1])#打印列表变量中索引号为1的一个值。注意索引号为1的值其实是列表中的第2个，也就是Oranges，当然如果索引号为0，才是 Apples。
print(stuff[-1])#whoa!fancy#这里打印索引号是-1的列表中的一个值，这里应该是倒数第一元素，也就是Corn。
print(stuff[-9])#我再试试-9是谁，难道是倒数第9个数？好奇怪啊，那么对于本列表来说还应该是 Oranges？正数第一个不是索引1，倒数第一个确实索引-1，这个是不是容易造成混乱呢？
print(stuff.pop())#对于stuff列表变量，采用了pop（）函数（方法？），取出了最后一个元素（默认是最后一个，如果不是最后一个，那参数里应该如何填写呢？？？？？）打印出来。
print(' '.join(stuff)) #what?cool!对于' '空格这个？？，采用了join函数，将stuff变量插进来？注意stuff 到现在为止已经变成了9个量了。
print('#'.join(stuff[3:5]))#super tellar!#对于'#'这个元素，采用了 jion函数，将stuff变量中的[3:5]——也就是第4、5、6个变量（'Telephone', 'Light', 'Sugar）给怎么了？（错误）
#注意：这里用到一个新函数(方法？):'sep'.join(seq):其中'sep'是分隔符，可以为空值；将seq中所有的元素合并成一个新的字符串
#注意：列表变量中取一部分的用法：stuff[3:5]的意思是取index号为3和5的元素，而不是3~5哦。
#print(' # '.join(stuff[3,5]))#看看stuff[3,5]是不是指3~5.报错：list indices must be integers or slices切片, not tuple元组
print('#'.join(stuff[3:4:5]))#为啥这样只能打印出第一个？
print('&&'.join(stuff[3:6]))#这样为啥只打印出345而不包含6？最后一位不打印？
print("------下面是加分题练习--------")


'''
# 运行后结果1：
bogon:lp3thw yyy$ python ex38.py
Wait there are not 10 things in the list. Let's fix that.
Adding: Boy
There are 7 items now.
Adding: Girl
There are 8 items now.
Adding: Banana
There are 9 items now.
Adding: Corn
There are 10 items now.
There we go: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do some things with stuff.
Oranges
Corn
Corn
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
Telephone#Light

# 运行后结果2：
bogon:lp3thw yyy$ python ex38.py
Wait there are not 10 things in the list. Let's fix that.
Adding: Boy
There are 7 items now.
Adding: Girl
There are 8 items now.
Adding: Banana
There are 9 items now.
Adding: Corn
There are 10 items now.
There we go: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
There we go again:['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do some things with stuff.
Oranges
Corn
Oranges
Corn
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
Telephone#Light
Telephone
Telephone&&Light&&Sugar


'''
