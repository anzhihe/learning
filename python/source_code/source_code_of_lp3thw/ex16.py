from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")#CTRL-C可以终止命令？
print("If you do want that, hit RETURN.")

input("?")#这里敲入Enter，返回一个什么数值？Ture False？

print("Opening the file...")
target = open(filename, 'w')## Truncating is not needed since the file is being opened in 'w' write mode.which automatically truncates the file. Comm'''enting out the lines below:https://github.com/lotspaih/python3HardWay/blob/master/ex16.py
'''
print("Turncating the file. Goodbye!")#上面那条语句里的open()方法里面用到了一个'w'参数，本来就是一个写(write)的模式，这样自动就“切断”了，不需要进行
target.turncate()#有这个语句，会报错——AttributeError: '_io.TextIOWrapper' object has no attribute 'turncate'
'''
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
line4 = input("line 4: ")
line5 = input("line 5: ")
line6 = input("line 6: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# 上面用了6条语句，感觉有些啰嗦，于是将6句，改成3句，如下：
target.write(f"{line4}\n")#\n在字符串里具有换行的意思。
target.write(f"{line5}\n")
target.write(f"{line6}\n")

# 以「读read」模式打开文件 'r', 读取内容, 并将其打印到窗口。
target = open(filename, 'r')
text_in_file = target.read()

print(f"\n{text_in_file}")#此处的\在text_in_file的前面，这个前后有什么关系呢？
print("1111111111111111111")
print ("----- 我是一条华丽的分割线 -----")
print("1111111111111111111")
print(f"{text_in_file}\n")#此处把转意义字符后置，看看有什么结果。n如果放后面的话就会换2行
print("1111111111111111111")
print(f"\n{text_in_file}")
print("1111111111111111111")#把n放在前面，则换一行。
print("And finally, we close it.")
target.close()


'''
运行后的效果1如下：------

bogon:lp3thw yyy$ python ex16.py test.txt
We're going to erase test.txt.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
?
Opening the file...
Now I'm going to ask you for three lines.
line 1: 寒蝉凄切
line 2: 对长亭晚
line 3: 骤雨初歇
line 4: 都门帐饮无绪
line 5: 留恋处兰舟催发
line 6: 执手相看泪眼 竟无语凝噎
I'm going to write these to the file.

寒蝉凄切
对长亭晚
骤雨初歇
都门帐饮无绪
留恋处兰舟催发
执手相看泪眼 竟无语凝噎

1111111111111111111
----- 我是一条华丽的分割线 -----
1111111111111111111
寒蝉凄切
对长亭晚
骤雨初歇
都门帐饮无绪
留恋处兰舟催发
执手相看泪眼 竟无语凝噎


1111111111111111111
And finally, we close it.

# 执行效果2如下：

bogon:lp3thw yyy$ python ex16.py test.txt
We're going to erase test.txt.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
?
Opening the file...
Now I'm going to ask you for three lines.
line 1: 寒蝉凄切
line 2: 对长亭晚
line 3: 骤雨初歇
line 4: 都门帐饮无绪
line 5: 留恋处兰舟催发
line 6: 执手相看泪眼 竟无语凝噎
I'm going to write these to the file.

寒蝉凄切
对长亭晚
骤雨初歇
都门帐饮无绪
留恋处兰舟催发
执手相看泪眼 竟无语凝噎

1111111111111111111
----- 我是一条华丽的分割线 -----
1111111111111111111
寒蝉凄切
对长亭晚
骤雨初歇
都门帐饮无绪
留恋处兰舟催发
执手相看泪眼 竟无语凝噎


1111111111111111111

寒蝉凄切
对长亭晚
骤雨初歇
都门帐饮无绪
留恋处兰舟催发
执手相看泪眼 竟无语凝噎

1111111111111111111
And finally, we close it.


# 以下是一些重要的命令：
close   关闭文件。
read    读取文件的内容。你可以把结果分配给一个变量。
readline    只读取文本文件中的一行。
turncate    清空文件。
write('stuff')  把'材料'写进文件里。
seek(0) 把读写文件的‘光标’移动到文件的开始位置。

'''
