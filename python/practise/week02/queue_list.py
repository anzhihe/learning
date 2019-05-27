#!/usr/bin/env python
# coding: utf8

'''
    从命令行接收输入
    如果输入为add,再进行接收，并将接收的工作内容加入到works后面
    如果输入为do,就打印works最前面的内容，并进行移除
        如果works没有工作内容，提示没有工作内容
    如果输入的是exit
       检查works中是否有工作内容，如果有工作内容则提示，如果没有工作内容则退出
'''

works = []

while True:
    _action = raw_input("请输入你要执行的操作（add => 添加，do => 执行）：")
    if _action == 'add':
        _work = raw_input("请输入工作内容：")
        works.append(_work)
    elif _action == 'do':
        if len(works) == 0: #if not works:
            print "没有工作内容！"
        else:
            print '工作内容：%s' % works.pop(0)
    elif _action == 'exit':
        if works: #if len(works) != 0:
            print '还有工作尚未完成，请完成！'
        else:
            break
    else:
        print '输入有误，请重新输入'
