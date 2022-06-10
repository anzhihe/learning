from django.shortcuts import render
from .models import *

from django.http import HttpResponse
from django.db.models import F, Q, Sum, Avg


# Create your views here.
def index(request):
    # articls = Artcile.objects.filter(id=10).all()
    # articls = Artcile.objects.filter(pk=1).all()
    # articls = Artcile.objects.filter(pk=10).first()

    # articls = Artcile.objects.get(id=1)
    # try:
    #     articls = Artcile.objects.get(id=10) # get找不到会报错
    # except Artcile.DoesNotExist:
    #     print('模型类不存在')
    # print(articls)

    # articls = Artcile.objects.filter(title__contains='py').all()  # 模糊查询

    # articls = Artcile.objects.filter(title__endswith='言').all()  # 以什么结尾

    # articls = Artcile.objects.filter(title__in=['python是最好的语言', '今天去泰国美美哒']).all()  # 在这个范围内
    # articls = Artcile.objects.filter(id__in=[1, 2, 4]).all()  # 在这个范围内

    # articls = Artcile.objects.filter(id__lte=3).all()

    # articls = Artcile.objects.exclude(id=3).all() # 取id不等于3的
    # articls = Artcile.objects.exclude(title='今天去泰国美美哒').all()  # 取id不等于3的

    # created_time__day

    '''

    todo
    :param request:
    :return:
    '''
    # articls = Artcile.objects.filter(created_time__day=16).all()

    # 两个属性做比较 F 对象
    # articls = Artcile.objects.filter(cnum__gt=F('vnum')).all()  # 取评论量大于浏览量
    # articls = Artcile.objects.filter(cnum__gt=F('vnum')*2).all()  # 取评论量大于浏览量*2

    # Artcile.objects.filter(id=2,title='哈哈吧',content='').all()# 多个条件
    # Artcile.objects.filter(id=2).filter(title="哈哈").filter(content="").all() # 多个条件
    # Artcile.objects.filter(Q(id=2)&Q(title='哈哈哈吧')).all() # 一般不会用Q去做并且 直接用filter()
    # articls = Artcile.objects.filter(Q(id__lt=2)|Q(title__contains='浅谈')).all() # 或者查询

    # result = Artcile.objects.aggregate(Sum('vnum'))  # 聚合函数
    '''
    {'vnum__sum': 201}

  
    '''  # print(result)

    # count = Artcile.objects.count()  # 去所有文章个数
    # print(count)
    # articls = Artcile.objects.filter(cat_id__lt=2)# 取分类id大于3的文章

    # print(articls)

    # articls = Artcile.objects.all()

    # 关联查询
    # article = Artcile.objects.get(id=1)
    # print(article.cat) # 多查一

    # category = Category.objects.get(id=1)
    # articls = category.artcile_set.all() # 一查多

    # article = Artcile.objects.get(id=1)
    # print(article.tag.all())  # 查询一篇所有标签

    # tag = Tag.objects.get(id=2)
    # print(tag)
    # print(tag.artcile_set.all())  # 查询一个标签下所有文章

    # print(tag.artcile_set.all()[:10])  # 支持切片

    categorys = Category.objects.all()

    return render(request, 'index1.html', locals())


def list(request, id):
    # cat = Category.objects.filter(id=2).values()
    # print(cat)

    #创建方法
    # Category.objects.create(name='哈哈')

    # 删除
    Category.objects.filter(id=4).delete()


    try:
        cat = Category.objects.get(id=id)
        # articles = cat.artcile_set.all()

        articles = cat.articles.all()

        # articles = Artcile.objects.filter(cat=id).all()
        ctx = {
            'articles': articles
        }

        return render(request, 'list.html', ctx)
    except Category.DoesNotExist:
        return HttpResponse('没有该分类')


def tlist(request, id):
    tag = Tag.objects.filter(id=id).first()

    if tag:
        articles = tag.artcile_set.all()
        ctx = {
            'articles': articles
        }
        return render(request, 'list.html', ctx)

    else:
        return HttpResponse('没有该标签')


from .models import Artcile


def find(request):
    list = Artcile.objects.all()  # 惰性查询特点
    # 不缓存
    [article.id for article in Artcile.objects.all()]
    [article.id for article in Artcile.objects.all()]

    # 缓存
    articles = Artcile.objects.all()
    [article.id for article in articles]
    [article.id for article in articles]
