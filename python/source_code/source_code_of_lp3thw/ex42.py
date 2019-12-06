## Animal is-a object(yes,sort of confusing) look at the extra credit
## 动物 is-a 对象（对，）……
class Animal(object):# 这是一个类（初始类，顶级类）
#    """docstring forAnimal."""
#    def __init__(self, arg):
#        superAnimal, self).__init__()
#        self.arg = arg

## 狗 is-a 类，这个类从Animal处继承。
class Dog(Animal):#这也是一个类，动物类下的，狗类。
#    """docstring forDog."""
    def __init__(self, name):
##??    superDog, self).__init__()
        self.name = name

##猫 is-a 类，这个类从Animal处继承。
class Cat(Animal):#这也是一个类，动物类下的，猫类。
#   """docstring forCat."""
    def __init__(self, name):
#       superCat, self).__init__()
        self.name = name

## 人类 is-a 类（也是个object对象……）
class Person(object):#这是一个类，人类。
#    """docstring forPerson."""
    def __init__(self, name):
#        superPerson, self).__init__()
        self.name = name

        ## 人类 has-a 宠物 of 一些。初始属性设置为None.
        self.pet =None

## 雇员 is-a 类
class Employee(Person):#这是另一个类，子类——雇员类。
#    """docstring forEmployee."""
    def __init__(self, name, salary):#这里可以看到Employee()函数，出了 self 之外，还有两个参数name和salary
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)# 这是你怎样运行__init__方法，从母类继承。
        ## ??
        self.salary = salary

## 鱼类是一个类。
class Fish(object):# 声明了一个类——母类
#    """docstring forFish."""
#    def __init__(self, arg):
#        superFish, self).__init__()
#        self.arg = arg
    pass

## 鲑鱼是一个子类，从  Fish 处继承。
class Salmon(Fish):#声明了一个子类-鲑鱼类。
    pass

## 碟鱼是一个子类，从  Fish 处继承。
class Halibut(Fish):#声明了一个子类——碟鱼类。
    pass

## rover(对象) is-a 狗（类）——把一只叫做Rover的狗，实例化了，也就是rover是一个“实例”
rover = Dog("Rover")

## satan（对象） is-a 猫（类）
satan = Cat("Satan")

## Mary （对象）is-a 人（类）——mary 是一个“实例”
mary = Person("Mary")
## Mary（对象）.属性 =
mary.pet = satan#Person 这个类的定义里面预制了self.pet这个属性。这里，把 satan（实例）赋值给了另一个“实例”的pet属性

##??通过给Employee(__,___)赋2个值，造就了一个实例Frank,将这个实例赋值给变量frank
frank = Employee("Frank",120000)

## 将叫做rover的这条狗的这个实例赋值给frank这个实例的pet属性。
frank.pet = rover

## 将 鱼类，这个类，赋值给flipper
flipper = Fish()

## 将 鲑鱼 ，这个类，赋值给crouse
crouse  = Salmon()

## 将 碟鱼，这个类，赋值给harry
