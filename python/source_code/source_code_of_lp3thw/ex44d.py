# 所有三种组合
# 44.1.4 All Three Combine
class Parent(object):#定义了一个 父母类
    def override(self):#在母类里，定义了一个override()函数——推翻
        print("PARENT override()")#这个 override（）函数要求打印出PARENT override()

    def implicit(self):#在这个母类里，又定义了第二个函数——盲从，
        print("PARENT implicit()")

    def altered(self):#在这个母类里，又定义了第三个函数——变异，
        print("PARENT altered()")

class Child(Parent):#这里定义了一个 子类，子类通过（）继承了母类。
    def override(self):#在子类里，定义了一个子函数，通过新定义了override（）函数，直接打印新的东西。
        print("CHILD override()")#这个新的子函数打印的东西和母函数不一样，体现在 print 的东西不一样。

    def altered(self):#在子类里，定义了一个函数——变异，
        print("CHILD, Before PARENT altered()")#函数里，打印出来，在母函数变异前的字符——即：子函数和母函数不一样。
        super(Child,self).altered()#采用 Python 的嵌入式函数 super(Child,self)来 call这个 Parent；可以预期的，打印出“print("PARENT altered()")”
        print("Child, After PARENT altered()")#又增加了一条打印，说，这里打印出来的是调用母类之后，又恢复了子类的功能。

dad = Parent()
son = Child()

dad.implicit()#这个没问题，是母类
son.implicit()#这个在子类里没有的函数，默认的是调用母函数？

dad.override()#这个调用母类的函数，没问题。
son.override()#这个调用了子类的相应函数，也没问题

dad.altered()#调用了母类
son.altered()#调用了子类，子类应该打印出3行。

'''
# 运行后结果：
PARENT altered()
CHILD, Before PARENT altered()
PARENT altered()# 这里就是嵌入式函数发挥的作用。
Child, After PARENT altered()
'''

# 使用 super（）的原因
'''
当你使用多重继承的时候
例如：
class SuperFun(Child, BadStuff):
    pass
方法解决顺序（MRO）
algorithm（算法）C3



'''
