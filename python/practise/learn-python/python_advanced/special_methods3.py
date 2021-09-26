#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    special_methods3.py
 @Function:    python类对象的特殊方法
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/17
"""


"""一、类对象的特殊方法之__del__()"""

"""
    系统会自动销毁不再需要的对象以释放内存。因此，当对象被销毁时通常不需要手动地执行清理工作。
    但是，当使用我们自己创建的资源时，可能需要执行一些额外的清理工作，例如，如果创建了一个自定义的
    类对象来打开一个文件并写入一些数据，可能需要在实例对象被销毁之前关闭该文件。为了执行这些额外的
    清理工作，可以在自定义的类对象中实现特殊方法__del__()
    当内存中的对象被销毁(垃圾回收)之前，会自动调用其对应的特殊方法__del__()
    当对象的引用计数为0时，对象并不会立刻被销毁(垃圾回收)，何时进行垃圾回收是不确定的。因此，
    特殊方法__del__()何时会被调用也是不确定的
"""

class MyClass(object):
    def __del__(self):
        print("特殊方法__del__被调用")

mc = MyClass()
del mc  # 特殊方法__del__被调用


"""二、类对象的特殊方法之__getattr__()"""

"""
    当访问实例对象的属性或方法时，如果指定的属性或方法不存在，就会抛出AttributeError
"""

class MyClass(object):
    pass

mc = MyClass()

# print(mc.data)  # AttributeError: 'MyClass' object has no attribute 'data'
# mc.do_sth() # AttributeError: 'MyClass' object has no attribute 'do_sth'

"""
    当访问实例对象的属性或方法时，为了避免指定的属性或方法不存在时抛出AttributeError，
    可以在实例对象对应的类对象中实现特殊方法__getattr__()。这样，当指定的属性或方法不存在时，
    会自动调用特殊方法__getattr__()
"""

class SomeClass(object):
    def __getattr__(self, name):
        if name == "data":
            return 18
        elif name == "do_sth":
            return print
        raise AttributeError("'SomeClass' object has no attribute '%s'" % name)

sc = SomeClass()
print(sc.data)  # 18
sc.do_sth(1, 2, 3)  # 1 2 3
# print(sc.score) # AttributeError: 'SomeClass' object has no attribute 'score'


"""三、类对象的特殊方法之__getitem__()"""

"""
    对于自定义对象的实例对象，在默认情况下，是不能像列表和字典那样使用中括号语法来操作数据的
"""

class MyClass(object):
    pass

mc = MyClass()
# print(mc[3])    # TypeError: 'MyClass' object is not subscriptable

"""
如果想让自定义类对象的实例对象可以像列表和字典那样，使用中括号语法来操作数据，
必须在自定义类对象中实现以下特殊方法：
1. __getitem__(self, key)    
    当执行操作obj[key]时，会自动调用该特殊方法
2. __setitem__(self, key, value)
    当执行操作obj[key] = value时，会自动调用该特殊方法
3. __delitem__(self, key)
    当执行操作del obj[key]时，会自动调用该特殊方法
"""

class MyDict(object):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

md = MyDict()

md["one"] = 18
md["two"] = 32
print(md.data)  # {'one': 18, 'two': 32}

print(md["two"])    # 32

del md["two"]
print(md.data)  # {'one': 18}


"""四、类对象的特殊方法之__call__()"""

"""
    如果在类对象中实现了特殊方法__call__()，那么就可以像调用函数一样直接调用这个类对象的
    实例对象，从而会自动调用特殊方法__call__()
"""

class MyClass(object):
    def __call__(self, *args, **kwargs):
        print(args, kwargs)

mc = MyClass()
mc()
mc(1, 2, x = 3, y = 4)

"""
    内置函数callable用于判断指定对象是否是可调用的
    除了函数对象是可调用的之外，对于实现了特殊方法__call__()的类对象，其实例对象也是可调用的
"""

print(callable(print))  # True

def do_sth():
    pass

print(callable(do_sth)) # True

print(callable(MyClass()))  # True