print("How old are you?", end=' ')#Attention: put a end=' ' at the end,means not a new line.
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?",end=' ')
weight = input()

print(f"So,you're {age} old, {height} tall and {weight} heavy.")

'''
这是一个可以获得用户输入的交互作用的程序。

输出的内容
itifadeMacBook-Pro:LP3THW yyy$ python ex11.py
How old are you? 35
How tall are you? 175cm
How much do you weigh? 75kg
So,you're 35 old, 175cm tall and 75kg heavy.


'''
