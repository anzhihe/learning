from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Coping from {from_file} to {to_file}")

# 我们可以用一行代码做两件事，怎么做呢？
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long") #len()函数是用来判断“长度”的。

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('Alright, all done.')

out_file.close()
in_file.close()

'''
# 运行后的结果
bogon:lp3thw yyy$ echo "This ia a testttt file." > test.txt #echo 命令貌似是，echo "一段文字" > XXX.txt将一段文字写入txt文件。
This ia a testttt file.
bogon:lp3thw yyy$ python ex17.py test.txt new_file.txt
Coping from test.txt to new_file.txt
The input file is 24 bytes long
Does the output file exist? False
Ready, hit RETURN to continue, CTRL-C to abort.

'''
