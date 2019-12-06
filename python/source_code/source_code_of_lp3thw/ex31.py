print("""Your enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear熊 here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear or else?")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.深渊邪神的视网膜")#abyss深渊邪神的视网膜。
    print("1.Blueberries.")#蓝色的浆果
    print("2.Yellow jacked clothespins衣服夹.")#黄色的衣服夹
    print("3.Understanding revolvers左轮手枪 yelling melodies.")#左轮手枪大叫旋律

    insanity = input("> ")#疯狂

    if  insanity == "1" or insanity == "2":
        print("Your body survives powered by mind of jello果冻. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck粪.Good job!")

else:
    print("You stumble around绊倒 and fall on a knife and die死了.Good job!")

'''
运行后的结果：
bogon:LP3THW yyy$ python ex31.py
Your enter a dark room with two doors.
Do you go through door #1 or door #2?
> 1
There's a giant bear熊 here eating a cheese cake.
What do you do?
1. Take the cake.
2. Scream at the bear.or else?
> 2
The bear eats your legs off. Good job!
bogon:LP3THW yyy$ python ex31.py
Your enter a dark room with two doors.
Do you go through door #1 or door #2?
> 1
There's a giant bear熊 here eating a cheese cake.
What do you do?
1. Take the cake.
2. Scream at the bear.or else?
> 1
The bear eats your face off. Good job!
bogon:LP3THW yyy$ python ex31.py
Your enter a dark room with two doors.
Do you go through door #1 or door #2?
> 1
There's a giant bear熊 here eating a cheese cake.
What do you do?
1. Take the cake.
2. Scream at the bear.or else?
> dd
Wll, doing dd is probably better.
Bear runs away.
bogon:LP3THW yyy$ python ex31.py
Your enter a dark room with two doors.
Do you go through door #1 or door #2?
> 2
You stare into the endless abyss at Cthulhu's retina.深渊邪神的视网膜
1.Blueberries.
2.Yellow jacked clothespins衣服夹.
3.Understanding revolvers左轮手枪 yelling melodies.
> 1
Your body survives powered by mind of jello果冻. Good job!
bogon:LP3THW yyy$ python ex31.py
Your enter a dark room with two doors.
Do you go through door #1 or door #2?
> 2
You stare into the endless abyss at Cthulhu's retina.深渊邪神的视网膜
1.Blueberries.
2.Yellow jacked clothespins衣服夹.
3.Understanding revolvers左轮手枪 yelling melodies.
> 3
The insanity rots your eyes into a pool of muck粪.Good job!
'''
