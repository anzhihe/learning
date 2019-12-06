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
