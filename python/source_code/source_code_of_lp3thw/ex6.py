types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"#二进制
do_not = "don't"
y = f"Theose who know {binary} and those who {do_not}."

print (x)
print (y)

print(f"I said: {x}")#字符串中嵌入了一个字符串变量，这个字符串变量中还嵌套着另外一个字符串变量。
print(f"I also said:'{y}'")

hilarious = False #意思是 欢闹的。我经常喜欢把False错误的写成Flase，从而造成错误。
joke_evalution = "Isn't that joke so funny?! {}"#这是一种嵌入变量的新方式。

print(joke_evalution.format(hilarious))#.format()中引入了新的变量方法。

w = "This is the left side of ..."
e = "a string with a right side."

print(w+e)# 通过+直接将两个字符串变量连接起来了。

'''
运行后的结果：
itifadeMacBook-Pro:LP3THW yyy$ python ex6.py
There are 10 types of people.
Theose who know binary and those who don't.
I said: There are 10 types of people.
I also said:'Theose who know binary and those who don't.'
Isn't that joke so funny?! False
This is the left side of ...a string with a right side.
'''
