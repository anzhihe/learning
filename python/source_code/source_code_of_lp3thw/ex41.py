'''
# 关键词 训练：
class :告诉python你要做个新型式的东西出来。

object：有两层意思：第一，事物的最基础的类型；第二，any instance(建议、情况？) of thing.

instance：建议、情况。当你告诉 python 去创作一个 class 的时候，你得到的东西。

def ：你在 class 里你定义了一个函数。

self ：在 class 里的函数，self是一个为 instance、object可以被访问的一个变量。

inheritance ：继承。这个概念是说一个 class 可以继承另一个 class 的特质，就像你和你的父母一样。

composition ：合成。这个概念是说一个 class 可以由其他几个 class 进行合成，类似于汽车有4个轮子

attribute ：特质、属性。class 所具有的特质，常常是通过合成得到的，并且通常是变量。

is-a：这是说这个东西是从其他东西合成的，或者说具有一种trait（特性），举个例子鲑鱼has-a嘴。

你最好做一些闪存卡，以更好的记住这些东西。

# 短语 训练：
1.class X(Y)：制作一个 叫 X 的 class，这个 class 中有 Y（制作了一条鱼X，这条鱼有嘴 Y）。

2.class X（object）：def _init_(slef,J):   class X 具有一个叫做 M 的函数，这个函数具有 self和 J 两个参数。

3.foo =X()：把 foo 设置给 classX 的情况。

4.foo.M(J)：从 foo 里，获得 M 函数，并且 使用参数 self 和 J来call 它

5.foo.K = Q: 从 foo 里获得 K 特性，并把它这个特性赋值给 Q。

在上面这些里，当你看到 XYMJKQ 以及 foo，你可以对待他们像对待空白点一样。举个例子，你可以像下面这种方法来写：

1."制作一个 叫 ??? 的 class，这个 class 中有 Y"
2."class???具有一个_init_它具有 self 和 ？？？变量 "
3.class？？？具有一个函数，函数名为？？？这个函数具有 self 和？？？参数。
4.把 foo 设置给一个 class？？？ 的 instance
5.从 foo 中获得？？？函数，并且使用 self=？？？和参数？？？来call 它。
6.从 foo 里，得到？？？特质，并且把它设置赋值给？？？

# 联结训练：
1.拿短语卡片并且训练。
2.练习再练习。
# 一个阅读测试
我准备了一个小的 hack 代码，用来训练你。下面就是代码，这些代码你应该敲进oop_test.py来使用。

#下面是ex41.py的代码：
'''
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
# 楼下写的像狗屎一样，鉴定完毕！20180319
PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":#下面代码里没有
    "class %%% has-a function *** that takes self and @@@",#下面代码里没有
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with parameters self,@@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

'''
来自这了的代码http://blog.csdn.net/github_37430159/article/details/54808102

'''



# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding = 'utf-8'))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results =[]
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(','.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class class_names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other class_names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameters lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                 question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")

'''
20180318 代码错误：
bogon:lp3thw yyy$ python ex41.py
  File "ex41.py", line 63
    "class %%%(object):\n\tdef ***(self, @@@)":
                                              ^
SyntaxError: invalid syntax
暂时未解决。
'''
# 一些观点20180319：
'''
看ex40和 ex41 看的恶心了，也没闹明白这个老外到底在讲什么，翻开廖雪峰大神的网站，可算明白类的概念和实例的概念了。
# 小结：面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# 参考地址：1.https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318645694388f1f10473d7f416e9291616be8367ab5000
# 2.https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431864715651c99511036d884cf1b399e65ae0d27f7e000
# 另：廖神的网站做的太酷了，这种以 wiki 的形式来生成自己的知识架构是在是一件很棒的事情，我怎么来做呢？
'''
# LOG:20180319 我承认我快疯了，虽然早上看明白了廖雪峰的 class 但是看到 LP3THW 我彻底的晕菜了，晚上代码调试是通过了，但是还是浑身冒汗，这个作者写的都是些什么！！。
