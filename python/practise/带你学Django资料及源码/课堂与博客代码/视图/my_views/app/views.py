from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    '''
    处理业务逻辑
    :param request:
    :return:
    '''
    return HttpResponse('哈哈哈')


'''

http://127.0.0.1:8000/show/1/h/
'''


def show(request, *args, **kwargs):
    # print(id, name)
    print(args)
    print(kwargs.get('name'))
    print(kwargs.get('id'))
    return HttpResponse('ok')


def show1(request, *args, **kwargs):
    # print(id, name)
    print(args)
    print(type(kwargs.get('arg')))
    print(kwargs.get('arg'))

    return HttpResponse('ok')


def show2(request, *args, **kwargs):
    print(args)
    print(kwargs)
    print(1 / 0)
    return HttpResponse('正则')
