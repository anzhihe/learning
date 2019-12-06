class Song(object):#“instantiate（实例-化）”召唤一个公式，创造了一个Object

    def _init_(self, lyrics):#内嵌了一个函数，初始化了一个_init_(self)声明了2个私有变量。
        self.lyrics = lyrics#将lyrics这个获得的参数字符串，赋值给self.lyrics

    def sing_me_a_song(self):#内嵌了一个函数，叫做“sing_me_a_song(self)（给我唱首歌）”
        for line in self.lyrics:#采用for循环，依次从self.lyrics里提取每一行。
            print(line)#打印每一行。
# 下面这行：将变量注册（赋值）给happy_bday ，用到了class制造的这个Object
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])#不知道哪里出错了20180318：报错：
# 下面这行：将变量注册（赋值）给bulls_on_parade ，用到了class制造的这个Object
bulls_on_parade = Song(["They rally around tha family",
                        "With pocket full of shells "])

happy_bday.sing_me_a_song()# 第一个变量》》》属性？方法第二个变量？

bulls_on_parade.sing_me_a_song()# 第2个变量》》》属性？方法第1个变量？
'''
# 报错内容：尚未解决，等待解决。20180318Flag！！！
Traceback (most recent call last):
  File "ex40.py", line 10, in <module>
    happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])
TypeError: object() takes no parameters

# 讲真，这里真的不是很明白。
'''
