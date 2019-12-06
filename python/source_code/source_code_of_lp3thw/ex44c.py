# 继承 Inheritance和 构成 composition
# 44.1.3 Alter Before or After 前后发生改变
class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, Before PARENT altered()")
        super(Child,self).altered()#采用 Python 的嵌入式函数 super（）来 call这个 Parent
        print("Child, After PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

'''
# 运行后结果：
PARENT altered()
CHILD, Before PARENT altered()
PARENT altered()# 这里就是嵌入式函数发挥的作用。
Child, After PARENT altered()
'''
