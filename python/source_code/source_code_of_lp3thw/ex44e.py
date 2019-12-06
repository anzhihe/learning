class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):#定义了一个 类

    def __init__(self):
        self.other = Other()

    def implicit(self):#新定义的函数：Child.implicit
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER alterd()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

'''
运行后结果：

bogon:lp3thw yyy$ python ex44e.py
OTHER implicit()
CHILD override()
CHILD, BEFORE OTHER alterd()
OTHER altered()
CHILD, AFTER OTHER altered()

'''

'''
# 大练习：从下列代码中，筛选可以复用的代码：

https://www.python.org/dev/peps/pep-0008/
'''
