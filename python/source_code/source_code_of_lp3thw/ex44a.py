# 继承 Inheritance和 构成 composition
# 4.1 含蓄（盲从？）继承 Implicit Inheritance
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

'''
运行后的结果:

bogon:lp3thw yyy$ python ex44a.py
PARENT implicit()
PARENT implicit()

'''
