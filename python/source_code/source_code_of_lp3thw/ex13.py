from sys import argv #argv叫做参数变量。这里要搞清楚的是pydoc也应该是个库？open,file,os,sys.
# read the WYSS section for how to run this
script, first, second, third = argv
# argv = argument variable
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

'''
运行后的结果1：

itifadeMacBook-Pro:LP3THW yyy$ python ex13.py stuff things that
The script is called: ex13.py
Your first variable is: stuff
Your second variable is: things
Your third variable is: that

运行后的结果2:
itifadeMacBook-Pro:LP3THW yyy$ python ex13.py apple orange grapefruit
The script is called: ex13.py
Your first variable is: apple
Your second variable is: orange
Your third variable is: grapefruit

'''
