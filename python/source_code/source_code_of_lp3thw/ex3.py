print ("I will now count my chickens:")

print("Hens",25+30/6)
print("Roosters",100-25*3%4)#Roosters is what? % colud use like this?
# 注意：%作为运算符的意思是：“取‘模’”而不是百分号。100除以（%，模除）16得6余4，那么这里结果就是4.
# print("Roosters",100- 25 * 3 MOD 4)# test MOD,result is MOD(mod) not work in this.
print ("Now I will count the eggs:")

print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)#故意在数字和符号之间增加了空格。

print ("Is it true that 3 + 2 < 5 - 7?")

print (3 + 2 < 5 - 7)

print ("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print ("Oh,that's why it's False.")

print ("How about some more.")

print("Is it greater?",5 > -2)
print("Is it greater or equal?",5 >= -2)
print("Is it less or equal?",5 <= -2)





'''
知识卡：PEMDAS（Parentheses Exponents Multiplication Division Addition Subtration）
知识卡：关于模除
注意：%作为运算符的意思是：“取‘模’”而不是百分号。100除以（%，模除）16得6余4，那么这里结果就是4.
又可以写成 mod这个符号
运行后的结果：
itifadeMacBook-Pro:LP3THW yyy$ python ex3.py
I will now count my chickens:
Hens 30.0
Roosters 97
Now I will count the eggs:
6.75
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh,that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False


----
知识卡片：一些符号的英文：
#   [octothorpe 或者 pound character]
+   [plus]
/   [slash]
*   [asterisk]
%   [percent]
<   [less-than]
>   [greater-than]
<=  [less-than-equal]
>=  [greater-than-equal]
'''
