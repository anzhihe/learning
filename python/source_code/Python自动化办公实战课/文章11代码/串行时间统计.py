from multiprocessing import Pool
import os
import time


# 用于计算平方
def f(x):
    return x*x

list1 = []

time1 = time.time()
for i in range(1, 10001):
    list1.append(f(i))
time2 = time.time()

print(str(time2-time1))
