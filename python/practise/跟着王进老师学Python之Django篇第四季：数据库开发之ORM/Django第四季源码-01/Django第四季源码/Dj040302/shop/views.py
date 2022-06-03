from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.

def index(request):

    # 写数据到数据库
    # position = models.Position(positionname='入库员', description='负责商品的入库')
    # position.save()
    # return HttpResponse("添加成功！")
    # 读取数据库中的数据
    product = models.Product.objects.get(productid='6005004003004')
    str = "商品编号：%s 条形码：%s 商品名称：%s" %(product.productid,product.barcode,product.productname)
    return HttpResponse(str)