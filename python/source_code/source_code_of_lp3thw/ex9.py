# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nAug"# 这里每增加一个\n就是说要转一行的意思。

print("Here are the days:",days)
print("Here are the months:",months)

print("""There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
# 下面这行是我新添加的 使用转义字符\n实现换行。
print("""There's something going on here.\nWith the three double-quotes.\nWe'll be able to type as much as we like.\nEven 4 lines if we want, or 5, or 6.""")

'''
运行后的结果：
itifadeMacBook-Pro:LP3THW yyy$ python ex9.py
Here are the days: Mon Tue Wed Thu Fri Sat Sun
Here are the months: Jan
Feb
Mar
Apr
May
Jun
Aug
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.

There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.

'''
