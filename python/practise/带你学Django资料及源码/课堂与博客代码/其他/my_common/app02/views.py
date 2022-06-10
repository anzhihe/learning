from django.shortcuts import render
from .models import Cat
from pure_pagination import PageNotAnInteger, Paginator


# Create your views here.


def index(request):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    cats = Cat.objects.all()
    p = Paginator(object_list=cats, per_page=2, request=request)  # 返回paginator对象

    cats = p.page(page)  # 取第几页的数据

    return render(request, 'app02/index.html', locals())
