from sys import argv # 从sys库里导入 argv模块。

script, filename = argv # argv 模块里有两个参数变量，分别是script和filename

txt = open(filename) # 用open() 方法打开这个叫做filename的文件，获得了文档内容，并将它赋值给了txt变量。

print(f"Here's your file {filename}:")#打印带参数的字符出啊内容，其中字符串变量用 {filename}代替
print(txt.read()) #将txt变量的内容用read()方法读出来，然后直接用print()函数打印出来。
#我又查了一遍，原文中并没有这一句： txt.close()#将txt变量使用.close()方法进行关闭。# 上面用一个txt变量承载和传递了filename（文件名）这个变量的信息，然后采用read()方法读取出来，然后用print()函数打印出来。# 下面这个代码，是用file_again这个变量承载了新输入的信息（采用>进行引导），采用open（）方法打开这个文件名，txt_again承载了这些信息。采用read()方法读出来，然后print()出来。
print("Type the filename again:") #这里打印了个字符串
file_again = input("> ") #这里使用了一个input()方法，这个方法是带提示符“>”的方法，将需要输入的内容赋值给变量 file_again

txt_again = open(file_again) # 将文件名，通过open()方法打开，并传递给txt_agian 这个变量。

print(txt_again.read()) # 将txt_agian这个文件代表的变量采用 read()方法读取内容，然后通过 print()方法打印出来。

txt_again.close() #将txt_again这个文件代表的变量，采用close()方法关闭掉。

'''
# 在本题中，我们发现了一个问题就是在“终端”中原来的用户名itifa变成了bogon这种莫名奇妙的东西。

# 运行后的结果：

bogon:LP3THW yyy$ python ex15.py ex15_sample.txt
Here's your file ex15_sample.txt:
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Type the filename again:
> ex15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
'''

# 附加题
'''
# 这节的难度跨越有点大，所以你要尽量做好这节加分习题，然后再继续后面的章节。

- 在每一行的上面加上注释。
- 如果你不确定答案，就问别人，或者上网搜索。大部分时候，只要搜索 “python” 加上你要搜的东西就能得到你要的答案。比如搜索一下“python open”。
- 我使用了“命令”这个词，不过实际上它们的名字是“函数（function）”和“方法（method）。上网搜索一下这两者的意义和区别。看不明白也没关系，这本书后面也会讲到这些。
- 删掉 10-15 行使用到raw_input的部分，再运行一遍脚本。
- 只用raw_input写这个脚本，想想哪种得到文件名称的方法更好？为什么？
- 运行 python 在命令行下使用 open 打开一个文件，这种 open 和 read 的方法也值得你一学。
- 让你的脚本对 txt和txt_again两个变量执行一下 close()，处理完文件后你需要将其关闭，这是很重要的一点。
'''
