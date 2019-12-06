# 继承 Inheritance和 构成 composition
# 44.1.2 明确的不顾的 Override Explicitly
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
