def eat1(n):
    for i in range(n):
        print("等待1min")
        print("等待1min")
        print("吃1cm面包")


def eat2(n):
    while n > 1:
        print("等待1min")
        print("等待1min")
        print("等待1min")
        print("等待1min")
        print("吃一半面包")
        n /= 2


def eat3(n):
    print("等待1min")
    print("吃一个鸡腿")


def eat4(n):
    for i in range(n):
        for j in range(i):
            print("等待1min")
        print("吃1cm面包")


eat4(16)
