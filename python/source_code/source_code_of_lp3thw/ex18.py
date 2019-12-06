# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")

# Ok,that *argv is actually pointless,we can just do this
def print_two_again(arg1, arg2):# 优于上面那种表达式。
    print(f"arg1:{arg1}, arg2:{arg2}")

# this just takes one argument(参数)
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothing'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

'''
# 运行后结果：
bogon:lp3thw yyy$ python ex18.py
arg1:Zed, arg2:Shaw
arg1:Zed, arg2:Shaw
arg1: First!
I got nothing'.
'''
