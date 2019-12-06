age = input("How old are you?") #问号与双引号之间没有空格。
height = input("How tall are you? ") #问号与双引号之间有空格。
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

'''
运行后显示的内容：
Last login: Wed Jan 31 09:21:32 on ttys000
itifadeMacBook-Pro:~ yyy$ python ex12.py
python: can't open file 'ex12.py': [Errno 2] No such file or directory
itifadeMacBook-Pro:~ yyy$ cd LP3THW
itifadeMacBook-Pro:LP3THW yyy$ python ex12.py
How old are you?35
How tall are you? 173cm
How much do you weigh? 75kg
So, you're 35 old, 173cm tall and 75kg heavy.
itifadeMacBook-Pro:LP3THW yyy$



'''
