# 面向对象的分析和设计基础。
## 这个过程如下：
'''
1.首先，写下或者画出来，这些问题。
2.从1里提取关键概念，对他们进行研究。
3.对于这些概念，创造出类的层级和对象地图。
4.对于类，进行编程，测试运行他们。
5.重复，改善。

#43.1.1 写出和画出关于这个问题。

场景：
死亡 Death
中心走廊 Central Corridor 有怪物在这里。
激光武器库 Laser Weapon Armory 英雄在这里要得到一个中子弹并输入密码。
桥 Bridge 另一个战斗场景，英雄在这里布放了炸弹。
逃生舱 Escape Pod 只有 Hero 推测正确了才能进入。

# 43.1.2 提取重要概念
首先我把所有的名词汇都提出来了：
Alien
Player
Ship
Maze
Room
Scene
Gothon
Escape Pod
Planet
Map
Engine
Death
Central Corridor
Laser Weapon Armory
The Bridge

# 43.1.3 为这些概念创造一个 Class 的层级和 Object 地图
* Map
    - next_scene
    - opening_scene
* Engine
    - play
* Scene
    - enter
    * Death
    * CentralCorridor
    * LaserWeaponArmory
    * TheBridge
    * EscapePod

wrap

# 43.1.4 为 Class 编码，并且运行测试


# 43.1.5 重复和提炼
从上到下vs 从下到上。
1.黑客进入一些小问题，黑客进入代码，并且使他勉强运行。
2.提炼这些代码，使它编的更加正式（使用 class 和自动化测试。）
3.提取你用到的关键概念，为这些做一些足够的检索工作。
4.为你真正想要做的东西写一个描述性的文字。
5.返回并且提炼你的代码，很可能砍掉很多代码，并且重新开始。
6.重复，转入到其他问题。


'''
#20180320凌晨12：39已经阅读到了p201,准备睡觉了。
# base class ,Subclass:
from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.这个场景还没定义")
        print("Subclass it and implement enter()实施enter（）来进行声明一个子类")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)#括号里对不对？

        # be sure to print out the last scene 确定你只打印粗了最后的场景。
        current_scene.enter()
'''
我也有Engine这个class,而且你可以看到我已经怎样使用了了方法Map.opening_scene和
Map.next_scene.因为我已经做了一些计划。我在定义Map这个 class 之前我就直接欧诺个了 Map 的方法。。为啥呢？
'''



class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
            ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):#dedent没有定义？
        print(dedent("""
                    行星percal # 25 gothons入侵你的船和摧毁你的整个船员。你是最后一个幸存的成员.
                    你最后的任务是从武器军械库得到中子破坏炸弹，把它放在桥上，进入逃生舱后炸掉飞船。
                    你跑在中央走廊的武器库，当gothon跳出来，红鳞，黑暗肮脏的牙齿，和邪恶的小丑服装，流动在他充满仇恨的身体。
                    他挡住了军械库的门，正要拔出武器来炸你。
            """))
        action = input("shoot! or dodge! or tell a joke or... >  ")
#在自定义 类里面 嵌套了个 if-elif-elif-else分支语句。
        if action == "shoot!":#开枪。
            print(dedent("""
                    你猛的抽出你的武器，向Gothon射击。他的小丑服装流淌在他的身体周围，抛弃了你的目标。
                    你的激光打他的服装，但完全没打中。这完全毁了他母亲给他买的全新服装。
                    这让他在疯狂的愤怒中飞起来，并往你脸上猛烈的大，直到你死去。然后，他吃了你……
                    """))
            return 'death'

        elif action == "dodge!":# 单次 dodge 躲闪。
            print(dedent("""
                    就像一个世界级的拳击手，你躲闪，左右右滑动为Gothon的布莱瑟曲柄激光过去你的头。
                    在你狡猾的躲闪中间，你的脚滑倒，你将头撞在金属墙上，然后晕倒。
                    你不久就醒来，因为Gothon跺着头，吃了你。
                    """))
            return 'death'

        elif action == "tell a joke":#讲个笑话。
            print(dedent("""
                    为你幸运的是，他们让你学习了哥通侮辱Lbhe zbgure vf fb sng，jura fur fvgf nebhaq gur ubhfr，fur fvgf nebhaq gur ubhfr。
                    Gothon停下来，尽量不要笑，然后笑出声来，不能动弹。
                    在他笑的时候，你跑了起来，在头上将他击倒，然后跳过武器库门。
                    """))
            return 'laser_weapon_armory'

        else:
            print("没有推断!")
            return 'central_corridor'
#在这之后我创造了CentralCorridor这个才是游戏的开始。
#我先于 Map，把场景构建出来，因为我在后面会引用它们。你也可以看到我是怎样使用dedent函数的。
#你可以试试移除它，看看会发生什么？
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
                你潜入武器军械库，蹲伏，扫描房间里可能隐藏的更多的Gothons。
                那里死气沉沉，太安静了。你站起来，跑到房间的另一边，在它的容器里找到中子炸弹。
                盒子上有一个键盘锁，你需要密码才能把炸弹拿出来。
                如果你错了10次，那么锁就会永远关闭，你就得不到炸弹了。代码是3位数。
              """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(code)
        guess = input("[keypad]> ")
        guessed = 0#原来这里写的 guesses 我判断不对，应该是guessed,另外这里初始化是1才是测试10次。

        while guess != code and guessed < 10:
            print("BZZZZEDDD!")
            guessed += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                    容器点击打开，密封断开，放出气体。你抓住中子炸弹，尽可能快地跑到你必须把它放在正确位置的桥上。
                    """))
            return 'the_bridge'
        else:
            print(dedent("""
                    锁最后一次发出嗡嗡声，然后你听到一种令人恶心的融化声音，因为机制融合在一起。
                    你决定坐在那里，最后哥特人把船从船上炸开，你就死了。
                    """))
            return 'death'

class TheBridge(Scene):

    def enter(slef):
        print(dedent("""
                在你的手臂下，你突然在桥上爆炸，突然有5个暴徒试图控制这艘船。
                他们每个人都有一个比最后一个更丑的小丑服装。
                他们还没有拔出他们的武器，因为他们看到了你胳膊下的炸弹，不想把它引爆。
                """))

        action = input("throw the bomb  OR slowly place the bomb OR... >  ")

        if action == "throw the bomb":
            print(dedent("""
                        在恐慌中，你把炸弹扔在一群暴徒身上，然后跳上门。
                        就像你把它扔到地上一样，它会在你的背后射杀你。
                        当你死的时候，你看到另一个人疯狂地试图拆除炸弹。
                        你会死的，知道他们可能会在爆炸的时候爆炸。
                        """))

            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                    Y你把你的爆裂弹指向你手臂下的炸弹，戈特森举起手来开始冒汗。
                    你向后叩门，打开它，然后小心地将炸弹放在地板上，指着你的冲击器。
                    然后，你从门后跳回来，按下关闭按钮，然后打开门锁，让Gothons不能离开。
                    现在放置了炸弹，你跑到逃生舱去掉这个锡罐。
                    """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
                你冲过这艘船，拼命想把它赶到逃生舱，然后整艘船都爆炸了。
                看起来几乎没有任何的Gothons在船上，所以你的运行是明显的干扰。
                你带着逃生舱进入房间，现在需要选择一个。
                有些可能会损坏，但你没有时间去看。有5个吊舱，你要哪个?
              """ ))

        good_pod = randint(1,5)
        print(good_pod)# 这一行是我新加的。
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print(dedent("""
                    “您跳入吊舱并弹出弹出按钮。”
打印“荚释放到空间的空隙中，然后在船体破裂时爆裂，把你的身体压成果酱。”
                    """))
            return 'death'
        else:
            print(dedent("""
                    你跳进吊舱并弹出弹出按钮。
                    这个吊舱很容易滑向太空，朝向下面的星球。
                    当它飞向地球时，你回头看看你的船内爆，然后像一颗明亮的恒星爆炸一样，同时取出戈吞船。
                    你赢了！
                        """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

'''
又一段话：

'''
class Map(object):

    scenes ={
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(slef, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


'''
运行后的结果：


bogon:lp3thw yyy$ python ex43.py

行星percal # 25 gothons入侵你的船和摧毁你的整个船员。你是最后一个幸存的成员.
你最后的任务是从武器军械库得到中子破坏炸弹，把它放在桥上，进入逃生舱后炸掉飞船。
你跑在中央走廊的武器库，当gothon跳出来，红鳞，黑暗肮脏的牙齿，和邪恶的小丑服装，流动在他充满仇恨的身体。
他挡住了军械库的门，正要拔出武器来炸你。

shoot! or dodge! or tell a joke or... >  tell a joke

为你幸运的是，他们让你学习了哥通侮辱Lbhe zbgure vf fb sng，jura fur fvgf nebhaq gur ubhfr，fur fvgf nebhaq gur ubhfr。
Gothon停下来，尽量不要笑，然后笑出声来，不能动弹。
在他笑的时候，你跑了起来，在头上将他击倒，然后跳过武器库门。


你潜入武器军械库，蹲伏，扫描房间里可能隐藏的更多的Gothons。
那里死气沉沉，太安静了。你站起来，跑到房间的另一边，在它的容器里找到中子炸弹。
盒子上有一个键盘锁，你需要密码才能把炸弹拿出来。
如果你错了10次，那么锁就会永远关闭，你就得不到炸弹了。代码是3位数。

827
[keypad]> 334
BZZZZEDDD!
[keypad]> 333
BZZZZEDDD!
[keypad]> 234
BZZZZEDDD!
[keypad]> 444
BZZZZEDDD!
[keypad]> 222
BZZZZEDDD!
[keypad]> 222
BZZZZEDDD!
[keypad]> 111
BZZZZEDDD!
[keypad]> 1111
BZZZZEDDD!
[keypad]> 2222
BZZZZEDDD!
[keypad]> 111
BZZZZEDDD!
[keypad]> 222

锁最后一次发出嗡嗡声，然后你听到一种令人恶心的融化声音，因为机制融合在一起。
你决定坐在那里，最后哥特人把船从船上炸开，你就死了。

You died. You kinda suck at this.
'''
