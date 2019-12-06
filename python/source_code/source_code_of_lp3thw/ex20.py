from sys import argv

scrips,input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):# 这个函数是个啥意思？切片？
    f.seek(0)#seek(0) 是什么意思？

def print_a_line(line_count, f):
    print(line_count, f.readline(),end= " ")# 如果有,end = "" 这个就不用换行了。

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line =1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line =current_line + 1
print_a_line(current_line, current_file)

current_line =current_line + 1
print_a_line(current_line, current_file)
