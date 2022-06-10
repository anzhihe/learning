from django.shortcuts import render
from .models import Category, News
from django.http import HttpResponse
from django.shortcuts import redirect  # 重定向


# Create your views here.
def index(request):
    categorys = Category.objects.filter(isdelete=False).order_by('-position').all()
    return render(request, 'index.html', locals())


def detail(request, id):
    # News.objects.filter(id=id).all() # 返回的列表
    news = News.objects.get(id=id)  # 返回的对象
    return render(request, 'detail.html', locals())


def delete(request, id):
    news = News.objects.filter(id=id).first()
    if news:
        # news.delete()
        news.isdelete = True
        news.save()
        return redirect('/')  # 首页

    else:
        return HttpResponse('数据不存在')
