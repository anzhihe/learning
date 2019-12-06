
#以下为代码调试。
print("How old are you?", end=' ')#提示符在本行尾部。
age = input()
print("How tall are you?")#新起一行。
height = input()
print("How much do you weigh?", end=' >')#提示符/n在 >这里貌似不管用？
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
# 下面调用了2个参数，这样直接调用行吗？是不是有个form sys import argv?

from sys import argv
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.  ")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates= secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


people = 20
cats = 30
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!")#被打印

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")#被打印


dogs += 5#狗变成了20

if people >= dogs:
    print("People are greater than or equal to dogs.")#这条被打印1

if people <= dogs:
    print("People are less than or equal to dogs.")#这条被打印2


if people == dogs:
    print("People are dogs.")#这条被打印3


'''
# 以下为代码原文：
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
print("How much do you weigh?", end=' '
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filenme)

print("Here's your file {filename}:")
print(tx.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again_read())


print('Let's practice everything.')
print('You\'d need to know \'bout escapes
      with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------)
print(poem)
print(--------------")


five = 10 - 2 + 3 -
print(f"This should be five: {five}"

def secret_formula(started)
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars  100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(startpoint)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cates = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs
    print("People are less than or equal to dogs.)


if people = dogs:
    print("People are dogs.")

# 以下是运行后结果：
bogon:LP3THW yyy$ python ex26.py test.txt
How old are you? 35
How tall are you?
173
How much do you weigh? >75
So, you're 35 old, 173 tall and 75 heavy.
Here's your file test.txt:
1我在练习LPTHW ex17.py
2我在练习LPTHW ex17.py
3我在练习LPTHW ex17.py
4我在练习LPTHW ex17.py
5我在练习LPTHW ex17.py
6我在练习LPTHW ex17.py
7我在练习LPTHW ex17.py
8我在练习LPTHW ex17.py
9我在练习LPTHW ex17.py
Type the filename again:
> test.txt
1我在练习LPTHW ex17.py
2我在练习LPTHW ex17.py
3我在练习LPTHW ex17.py
4我在练习LPTHW ex17.py
5我在练习LPTHW ex17.py
6我在练习LPTHW ex17.py
7我在练习LPTHW ex17.py
8我在练习LPTHW ex17.py
9我在练习LPTHW ex17.py
Let's practice everything.
You'd need to know 'bout escapes with \ that do
 newlines and 	 tabs.
--------------

	The lovely world
with logic so firmly planted
cannot discern
the needs of love
nor comprehend passion from intuition
and requires an explanation

	where there is none.

--------------
This should be five: 5
With a starting point of: 10000
We'd have 5000000 beans, 5000.0 jars, and 50.0 crates.
We can also do that this way:
We'd have 500000.0 beans, 500.0 jars, and 5.0 crates.
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.

'''
