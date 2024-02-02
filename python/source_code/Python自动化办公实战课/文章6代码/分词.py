import jieba

# jieba是第三方库,需要使用pip3 install jieba 进行安装后使用

words1="速度快，包装好，看着特别好，喝着肯定不错！价廉物美"

words2 = jieba.cut(words1)
words3 = list(words2)
print("/".join(words3))
# 速度/快/，/包装/好/，/看着/特别/好/，/喝/着/肯定/不错/！/价廉物美

# words4 停止词
stop_words = ["，", "！"]
words4 =[x for x in words3 if x not in stop_words]
print(words4)
# ['速度', '快', '包装', '好', '看着', '特别', '好', '喝', '着', '肯定', '不错', '价廉物美']

# words5 基于词性移除标点符号
import jieba.posseg as psg  
words5 = [ (w.word, w.flag) for w in psg.cut(words1) ]
# 保留形容词
saved = ['a', 'l']
words5 =[x for x in words5 if x[1] in saved]
print(words5)
# [('快', 'a'), ('好', 'a'), ('好', 'a'), ('不错', 'a'), ('价廉物美', 'l')]


from snownlp import SnowNLP
words6 = [ x[0] for x in words5 ]
s1 = SnowNLP(" ".join(words3))
print(s1.sentiments)
# 0.99583439264303
positive = 0
negtive = 0
for word in words6:
    s2 = SnowNLP(word)

    if s2.sentiments > 0.7:
        positive+=1
    else:
        negtive+=1

    print(word,str(s2.sentiments))
print(f"正向评价数量:{positive}")
print(f"负向评价数量:{negtive}")
# 快 0.7164835164835165
# 好 0.6558628208940429
# 好 0.6558628208940429
# 不错 0.8612132352941176
# 价廉物美 0.7777777777777779
# 正向评价数量:3
# 负向评价数量:2