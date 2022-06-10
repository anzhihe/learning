from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
import os
from django.shortcuts import redirect, reverse
import hashlib







# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'myupload/index.html', locals())


def upload(request):
    if request.method == 'GET':
        return render(request, 'myupload/upload.html')
    else:
        name = request.POST.get('name')
        pic = request.FILES.get('avator')

        media_root = settings.MEDIA_ROOT  # media
        allow_upload = settings.ALLOW_UPLOAD  # ALLOW_UPLOAD
        path = 'upload/{}/{}/{}/'.format(datetime.now().year, datetime.now().month, datetime.now().day)
        full_path = media_root + '/' + path

        # full_path = 'media/upload/2019/12/20'
        if not os.path.exists(full_path):  # 判断路径是否存在
            os.makedirs(full_path)  # 创建此路径

        # 要不要改图片的名字 生成hash
        # 这块要不要判断图片类型  .jpg  .png .jpeg
        # '/../../../myviews/setting.py'
        print(pic)
        if pic.name.split('.')[-1] not in allow_upload:
            return HttpResponse('fail')

        with open(full_path + '/' + pic.name, 'wb') as f:
            for c in pic.chunks():  # 相当于切片
                f.write(c)

        User.objects.create(name=name, avator=path + pic.name)
        return redirect('myupload:index')
