# Class 可以被当做“函数字典”来使用。map one thing to another映射一种东西到另一种东西。

#---------
# Modules的练习：mystuff.py就是个module
#! 下面这两句代码存在mystuff.py里。
mystuff = {'apple':"I AM APPLES!"}#一个字典型的变量。
print(mystuff['apple'])#打印mystuff中索引apple对应的内容——即输出I AM APPLES!

# Modules 就是get X from Y的逻辑。

#第1步：一个py文件（里面有 公式，有变量。）
#第2步：你import了这个文件。
#第3步：你通过.(dot)操作符号，获得了这个function或者变量。
# 你想着：我有个module ，我决定把它命名为 mystuff.py,并且我在里面定义了一个函数，我把它起名叫做apple
# ----------------------------------------
# 下面的代码在mystuff.py里面。
#! 下面这两句代码存在mystuff.py里。
def apple():
    print("I AM APPLES!")

#-------------
# 你可以通过import mystuff 这个module的方法引入
import mystuff
mystuff,apple()

#-------
#你也可以在里面添加一个变量named -----tangerine
def apple():
    print("I AM APPLES!")
tangerine = "Living reflection of dream"#这里仅仅是个变量而已。
#------
当然还有同样的方法：
import mystuff

mystuff.apple()
print(mystuff.tangerine)

# 回顾一下“字典”的语法，非常类似，但是语法也有所不同。下面进行比较：
mystuff['apple']#从字典里得到apple
mystuff.apple()#从 Module里得到apple的方法。
mystuff.tangerine # 同样的，这里只是个变量而已。

# 这意味着 我们有一个“非常”普通的pattern里。
#1.获得一个 key= 数值类型容器
#2.通过 key 的名字得出一些东西。
'''
总结：
A1   当它是字典的时候，这个 key 是一个字符串，其语法是 [key].
A2   当它是module的时候，这个key是一个 辨识符（identifier）,语法是 .key

'''
# 40.1.1 Classed 和 Modules类似：
'''
你可以把modules想象成一种特殊的dictionary——它可以存储python代码——你可以通过.操作符号。
python 还有另外一种数据类型，作为类似的目的，它叫做 CLass。一个Class是一种方法，这种方法能够
它可以从一组函数和数据里取的，并且把他们放在一个容器里，你可以使用.操作符，获得他们。

如果我想要像mystuff的module一样，要创造一个class, 我会做成下面这种样子：
'''
#ex40a.py
class MyStuff(object):

    def _init_(self):# _init_() 函数用于initialize初始化你新建立的object.额外的变量self
        self.tangerine ="And now a thousand years between"

    def apple(self):
        print("I AM ClASSY APPLES!")
'''

和modules相比，它看起来确实有些复杂。对比起来的话，区别也非常明显。
但是，你应该能够搞明白--内嵌了一个apple()函数的“微module”--MyStuff。
这里，什么可能把你搞晕呢？就是这个包含了self.tangerine的_init_()函数
这个函数设置了tangerine为例子的变量。
下面解释为什么classes用来代替modules: 你可以用MyStuff这个class，创造很多的它们。
可以创造很多很多，彼此之间还互不影响。但是，当你import一个module的时候呢，真个程序一般
只会引入1个，除非...你想做恐怖的黑客行为。
在你搞明白这些之前，你需要明白这个object是个什么鬼，还需要搞明白怎样使用MyStuff就像你使用
使用mystuff.py这个module一样。
# 40.1.2 objects Are Like import
如果一个class真的像一个小的module,那么应该有一个类似的概念，例如import这个class.
这个叫做“instantiate（实例-化）”，这是一个奇特的，讨厌的，极度剧烈的方法来说"创造"，
当你instantiate（实例-化）一个class，你得到的就是一个object.
你instantiate（实例-化）（创造）了一个class，是通过“召唤”class的方式，好像它是个公式。
例如下面这样：
'''

thing = MyStuff()
thing.apple()#这个object好像就有了个属性--MyStuff().apple()MyStuff().tangerine;
print(thing.tangerine)

'''
第一行就是这个所谓的“instantiate（实例-化）”，它看起来很像是在召唤一个公式。
然而，这个就是python在为你协调事件的顺序，在现场的背后。
我将会使用前述MyStuff的代码来进行如下的步骤：
1.python寻找MyStuff()，并且发现这是一个你定义的class
2.python制作了一个空的object使用了你定义的函数，这里你在  class 里用def定义的。
3.python然后来找，看看你是否制作了这个“神奇的”_init_函数，如果你制作了，
它就召唤这个函数，让他初始化你新创造的这个空的object.
4.在MyStuff函数_init_里，我们使用这个额外的变量 self,这是python为我制作的一个空的
object.我可以在它里面设置变量，就像你使用module dictionary或者其他object一样。
5.在这种情况下，我为歌词设置了self.tangerine，我初始化了这个object
6.现在 python 可以使用这个刚制作完成的object了，然后把它注册到thing这个变量。

这就是当你像使用公式一样call一个class的时候，python 做的事。这是使用 class 的一个蓝图。
实际上，class和objects是从module来的分叉。如果我更加诚实一点,我会这样说：
- class 像制作新的mini-module的蓝图或定义。
- 实例化 是指 你怎样制作一个mini-modules 并且同时import它。
- 作为结果产生的mini-module 被称作一个object，随后你注册它到一个变量下面，然后使用他。
此时，object和module 的表现就是不同的了。这个就是帮助你理解他们的不同。

'''
# 40.1.3 Getting Thins from Things：

# 有三种方法从 things 里得到 things

# 方法一：字典类型：dict style

mytuff['apples']

# 方法二：模快类型， module style

mystuff.apples()
print(mystuff.tangerine)

#  方法三：类的类型，class style

thing = MyStuff()
thing.apples()
print(thing.tangerine)

# 40.1.4 第一个 Class 例子
