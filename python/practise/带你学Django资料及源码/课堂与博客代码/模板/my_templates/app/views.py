from django.shortcuts import render

from .models import Dog


# Create your views here.

def index(request):
    '''
    加载
    渲染
    :param request:
    :return:
    '''

    dog = Dog.objects.get(id=1)  # 单个对象
    dogs = Dog.objects.all()
    ctx = {
        'name': '老王',
        'age': 12,
        # 'dict': {"name": "男"},
        # 'dict': dog,
        'dict': ['a', 'b', 'c'],
        'dogs': dogs,
        # 'dogs': [],
        'hobby': '桑拿',
        'dog': dog,
        'name1': "老王"
    }
    return render(request, 'index.html', ctx)
