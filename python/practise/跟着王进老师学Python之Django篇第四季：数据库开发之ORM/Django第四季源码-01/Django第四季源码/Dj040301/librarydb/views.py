from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.

def index(request):
    # 实例化一个对象
    # 获取BookType对象
    booktype_object = models.BookType.objects.get(id=1)
    # 获取Author的对象
    author_object = models.Author.objects.get(id=1001)
    # 获取Press的对象
    press_object = models.Press.objects.get(id=18001)

    book = models.Book(bookid=39001,bookname='Python从入门到精通', booktype = booktype_object, author = author_object,
                       press = press_object, price= 34.52, storagein=50)
    book.save()
    # 返回一个结果
    return HttpResponse("图书添加成功！")