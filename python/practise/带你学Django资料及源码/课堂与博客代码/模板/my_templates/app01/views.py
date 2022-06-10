from django.shortcuts import render


# Create your views here.


def son1(request):
    return render(request, 'app01/son1.html')


def son2(request):
    return render(request, 'app01/son2.html')


# 转义
def escape(request):
    ctx = {

        'content': '<h1>哈哈</h1>'
    }
    return render(request, 'app01/escape.html', ctx)


# 反向解析

def center(request):
    return render(request, 'app01/center.html')


def center1(request):
    return render(request, 'app01/center1.html')


def center2(request, id):
    return render(request, 'app01/center2.html')
