from django.shortcuts import render,redirect,reverse
from . import models
from django.http import HttpResponse
from django.db.models import Count, Max, Min, Sum, Avg
from django.db.models import F, Q
import random

# Create your views here.

active_dict = {'course': '全部', 'price':'全部', 'difficult': '全部', 'author':'全部'}
list_dict = {
    'course':['全部', '计算机', '法律', '外语', '经济', '健康与养生', '物理', '化学','生理',
              '会计学', '社会学','小说','文艺','青春文学','动漫','童书','人文社科','投资励志'],
    'price':['全部','0-20元','20-30元','30-40元','40-50元','50-60元','60-70元','70-80元','80元以上'],
    'difficult':['全部', '初级', '中级', '高级'],
    'author':['全部', '谢荣','刘军' ,'李明', '戴有炜','张天桥','程国伟','郑新强','刘明波']
}

Tips = [
        ("凤凰自营","有凤凰传媒自己出版和经营的图书"),
        ("热销图书","本周销售前100名的图书"),
        ("满99减20","所有标注满99减20商品才销售满减"),
        ("限时抢","在每天中午12:00有优惠"),
        ('提供电子书',"购买图书即送对应的电子书"),
        ]


def index(request):
    # 获取所有图书信息
    books = models.Book.objects.all().values()

    for book in books:
        # 准备图图片路径
        book['img'] = "../static/img/icon/" + str(book['bookid']) + ".jpg"
        # 准备Tip
        book['tip'] = Tips[random.randint(0, len(Tips)-1)]
        # 准备作者
        author = models.Author.objects.filter(book__bookid=book['bookid']).values()
        print("获取的作者：", author)
        print(author[0]['authorname'])
        book['author'] = author[0]['authorname']
    # 传递
    return render(request, 'index.html', context={'items': list_dict,
                                                  'active': active_dict,
                                                  'books':books
                                                  })

def select(request):
    # 获取值
    type = request.GET.get('type')
    course = request.GET.get('course')
    # 修改值
    active_dict[type]=course

    return redirect(reverse('index'))
