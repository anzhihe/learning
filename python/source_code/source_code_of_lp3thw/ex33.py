i = 0
numbers = [] #定义了一个变量number，这个变量是一个list列表
# 思考list和array的区别联系：list是列表,可以通过索引查找数值，但是不能对整个列表进行数值运算array是数组，也可以通过索引值查找数据，但是能对整个数组进行数值运算
while i < 6 :
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i +1
    print("Numbers now:", numbers)#注意：print中的变量用法。可以在“”外面加逗号和变量。
    print(f"At the bottom i is {i}")


print("The numbers:")

for num in numbers:
    print(num)

'''
# 运行后的结果：

bogon:LP3THW yyy$ python ex33.py
At the top i is 0
Numbers now: [0]
At the bottom i is 1
At the top i is 1
Numbers now: [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now: [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now: [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now: [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now: [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers:
0
1
2
3
4
5

'''
