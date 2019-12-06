# ex19.函数和变量
'''
函数这个概念也许承载了太多的信息量，不过别担心。只要坚持做这些练习，对照上个练习中的检查点,检查一遍这次的练习，你最终会明白这些内容的。
有一个你可能没有注意到的细节，我们现在强调一下:
函数里边的变量和脚本里边的变量之间是没有连接的。下面的这个练习可以让你对这一点有更多的思考:
'''

def cheese_and_crackers(cheese_count,box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function number directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our scripts:")
amount_of_cheese = 10
amount_of_crackers =50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)

#  运行后显示
'''
bogon:LP3THW yyy$ python ex19.py
We can just give the function number directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR, we can use variables from our scripts:
You have 10 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do math inside too:
You have 30 cheeses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two, variables and math:
You have 110 cheeses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.
'''
