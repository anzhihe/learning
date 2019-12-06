from sys import exit#从sys模块里导入exit模块

def gold_room():#定义一个函数：金屋子。
    print("这个屋子里堆满了金子，你准备要带走多少？")

    choice = input("请输个数吧> ")#只有选择0和1的时候将choice转换成int?其他的数呢？因此我改了。

    if choice.isdigit():#判断你输入的是否是数字。
        how_much = int(choice)
        if how_much < 50:
            print("很好，你不贪婪，你赢了！")
            exit(0)
        else:
            dead("你是个贪婪的混蛋!")
    else:
        print("先生, 敲个'数字'进去嘛？")
        gold_room()


def bear_room():#定义第二个函数：熊屋子。
    print("""
    这里有一头熊.
    这头熊有一罐蜂蜜.
    这头熊在另一个门口.
    你准备怎么移动开这头熊?
    """)
    bear_moved =False

    while True:#当什么？是真？
        choice = input("你可以输入：take honey、taunt bear、open door：/n> ")

        if choice == "take honey":
            dead("熊看着你，然后开始打你打脸。")#调用dead()函数。
        elif choice == "taunt bear" and not bear_moved:
            print("熊从门口移开了.")
            print("你现在可以进去了.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("熊生气了，咬了你的腿.")#调用dead()函数。
        elif choice == "open door" and bear_moved:
            gold_room()#调用gold_room()函数。
        elif choice == "open door" and not bear_moved:#这一行是我新加的。
            dead("熊生气了，咬了你的腿.")#调用dead()函数。
        else:
            print("我不知道那是什么意思。")


def cthulhu_room():#邪神房间
    print("这里你看到邪神房间。")
    print("他，不管你怎么看都疯了。")
    print("你是逃避生命还是吃你的头?")

    choice = input("flee逃走，head头？> ")

    if "flee" in choice:#逃走
        start()
    elif "head" in choice:#头
        dead("嗯，那很好吃!")
    else:
        cthulhu_room()


def dead(why):#这是一个定义的dead()函数，参数是why?
    print(why, " Well Done!")
    exit(0)

def start():#这是最开始的一个函数，可以用来调用熊房间或者邪神房间。
    print("你在一个黑屋子里.")
    print("有2个门在你的左右。")
    print("你选择哪个呢?")

    choice = input("请选择left或者right> ")

    if choice == "left":#如果选择左边的门，则调用-熊房间这个函数。
        bear_room()
    elif choice == "right":#如果选择左边的门，则调用-邪神这个函数。
        cthulhu_room()
    else:
        dead("你在房间里跌跌撞撞，直到饿死。")

start()#调用start（）函数。

'''
# 运行后的结果如下：
bogon:LP3THW yyy$ python ex35n.py
你在一个黑屋子里.
有2个门在你的左右。
你选择哪个呢?
请选择left或者right> right
这里你看到邪神房间。
他，不管你怎么看都疯了。
你是逃避生命还是吃你的头?
flee逃走，head头？> flee
你在一个黑屋子里.
有2个门在你的左右。
你选择哪个呢?
请选择left或者right> right
这里你看到邪神房间。
他，不管你怎么看都疯了。
你是逃避生命还是吃你的头?
flee逃走，head头？> flee
你在一个黑屋子里.
有2个门在你的左右。
你选择哪个呢?
请选择left或者right> left

    这里有一头熊.
    这头熊有一罐蜂蜜.
    这头熊在另一个门口.
    你准备怎么移动开这头熊?

你可以输入：take honey、taunt bear、open door：/n> open door
熊生气了，咬了你的腿.  Well Done!
'''
