from django.shortcuts import render
from .models import HeroType, Hero, Kill
from django.http import HttpResponse


# Create your views here.


def index(request):
    '''
    接受用户请求，处理业务逻辑
    :param request:
    :return:
    '''

    '''
    找数据
    '''
    hts = HeroType.objects.all()  # 查询全部

    # 构造字典
    ctx = {
        'hts': hts
    }

    return render(request, 'index.html', ctx)


def show(request, id):
    '''

    :param request:
    :param id: 英雄类型的主键
    :return:
    select * from app_hero where ht_id = id
    '''
    heros = Hero.objects.filter(ht=id).all()

    # ctx = {
    #     'heros':heros
    # }
    return render(request, 'show.html', locals())


def kill(request, id):
    kills = Kill.objects.filter(hero=id).all()
    return render(request, 'kill.html', locals())
