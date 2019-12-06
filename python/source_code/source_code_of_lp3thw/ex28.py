'''
# 以下是测试结果：

bogon:LP3THW yyy$ python
Python 3.6.4 |Anaconda custom (64-bit)| (default, Jan 16 2018, 12:04:33)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> True and True
True
>>> true and false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> True and False
False
>>> 1==1 and 2==1
False
>>> "test"=="test"
True
>>> 1==1 or 2!=1
True
>>> True and 1==1
True
>>> False and 0!=0
False
>>> True or 1==1
True
>>> "test" =="testing"
False
>>> 1!=0 and 2==1
False
>>> "test"!="testing"
True
>>> "test"==1
False
>>> not(Ture and False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Ture' is not defined
>>> not (True and False)
True
>>> not(1==1 and 0!=1)
False
>>> not(10==1 or 1000==1000)
False
>>> not(1 != 10 or 3 == 4)
False
>>> not("testing"=="testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and not("testing" ==1 or 1==0)
True
>>> "chunky"== "bacon" and not(3==4 or 3==3)
False
>>> 3==3 and not ("testing" == "testing" or "Python"=="Fun")
False
>>>
'''
