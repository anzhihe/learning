from sys import argv
# script 竟然直接是一个需要被打开的代码文件的名字，这样也行，在输入Python+文件名的是欧，文件名竟然可以直接作为参数输入。
script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.Nice.
""")

'''
运行后结果：

itifadeMacBook-Pro:LP3THW yyy$ python ex14.py Zed
Hi Zed, I'm the ex14.py script.
I'd like to ask you a few questions.
Do you like me Zed?
> Yes
Where do you live Zed?
> San Francisco
What kind of computer do you have?
> Tandy 1000

Alright, so you said Yes about liking me.
You live in San Francisco. Not sure where that is.
And you have a Tandy 1000 computer.Nice.

'''
