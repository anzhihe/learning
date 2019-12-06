def break_words(stuff):
    """This function will break up words for us."""#break up 拆散 结束
    words = stuff.split(' ')# 请注意这里有一个split()方法-分裂劈开
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)#sort分类挑选整理

def print_first_word(words):
    """Prints the first word agter popping it off."""
    word = words.pop(0)#pop突然意外出现。请注意，这里有一个pop()方法。
    print(word)

def print_last_word(words):
    """Prints the last word after poping it off."""
    word = words.pop(-1)#pop突然意外出现。请注意，这里有一个pop()方法。
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and return the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
# prompt 提示符>

'''
# 第1种运行结果：
新建立了一个文件名为ex25n.py,内容为：
import ex25
sentence = "All good things come to those who wait."
#words = break_words(sentence)
words = ex25.break_words(sentence)
words #
sorted_words = ex25.sort_words(words)
sorted_words #
ex25.print_first_word(words)#打印了个All
ex25.print_last_word(words) #打印了个wait.
words #
ex25.print_first_word(sorted_words)#打印了个All。
ex25.print_last_word(sorted_words)# 打印了个who
sorted_words #
sorted_words= ex25.sort_sentence(sentence)
sorted_words #
ex25.print_first_and_last(sentence)#C： 打印第一个All和最后一个字wait。
ex25.print_first_and_last_sorted(sentence) # D 打印第一个All和最后一个sorted的句子who。
print("-------- THE END ----------")
print("---------下面是采用了from ex25 import *")
from ex25 import *
sentence = "All good things come to those who wait."
#words = break_words(sentence)
words = break_words(sentence)
words #
sorted_words = sort_words(words)
sorted_words #
print_first_word(words)#打印了个All
print_last_word(words) #打印了个wait.
words #
print_first_word(sorted_words)#打印了个All。
print_last_word(sorted_words)# 打印了个who
sorted_words #
sorted_words= sort_sentence(sentence)
sorted_words #
print_first_and_last(sentence)#C： 打印第一个All和最后一个字wait。
print_first_and_last_sorted(sentence) # D 打印第一个All和最后一个sorted的句子who。
print("-------- THE END ----------")
-----
运行结果为：
bogon:LP3THW yyy$ python ex25n.py
All
wait.
All
who
All
wait.
All
who
-------- THE END ----------
---------下面是采用了from ex25 import *
All
wait.
All
who
All
wait.
All
who
-------- THE END ----------
#  第2种运行结果：
>>> import ex25
>>> sentence="All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words=ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>>

-------------------------
# from ex25 import *

bogon:LP3THW yyy$ import ex25
-bash: import: command not found
bogon:LP3THW yyy$ python
Python 3.6.4 |Anaconda custom (64-bit)| (default, Jan 16 2018, 12:04:33)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from ex25 import *
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ex25' is not defined
>>> words = break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words= sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> print_first_word(words)
All
>>> print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> print_first_word(words)
good
>>> words
['things', 'come', 'to', 'those', 'who']
>>> print_first_word(sorted_words)
All
>>> print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> print_first_and_last(sentence)
All
wait.
>>> print_first_and_last_sorted(sentence)
All
who
>>>




'''
