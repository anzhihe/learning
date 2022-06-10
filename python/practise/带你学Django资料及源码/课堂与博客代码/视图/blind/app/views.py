import random
import os
import re, hashlib
from datetime import datetime
from django.shortcuts import redirect, reverse, render
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from .models import User

'''
自己的模块
'''


# Create your views here.


def index(request):
    uid = request.session.get('uid')
    user = None
    if not uid:
        return render(request, 'marry.html', locals())
    else:
        user = User.objects.get(id=uid)
        all_users = User.objects.exclude(gender=user.gender)  # 跟你性别相反的人

        my_hobby = user.hobby.split(",")  # ['抽烟','喝酒']

        # '抽烟,烫头'
        hobbys_users = []
        for hobby in my_hobby:
            hobbys_users += all_users.filter(hobby__contains=hobby).all()
            print(hobbys_users)

        all_users = all_users.all()

        return render(request, 'marry.html', locals())


#
# def register(request):
#     if request.method == 'GET':
# ctx = {
# 'a':1
# }
#         return render(request, 'register.html')
#     else:
#         pass

def check_phone(phone):
    return re.match(r'1[3456789]\d{9}', phone)


def get_spwd(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode())
    return md5.hexdigest()


# 上传头像
def upload(pic):
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
    if pic.name.split('.')[-1] not in allow_upload:
        return HttpResponse('fail')

    with open(full_path + '/' + pic.name, 'wb') as f:
        for c in pic.chunks():  # 相当于切片
            f.write(c)

    # User.objects.create(name=name, avator=path + pic.name)

    # 图片的名字可以生产uuid
    return path + pic.name


class Register(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):

        phone = request.POST.get('phone')
        nickname = request.POST.get('nickname')
        pwd = request.POST.get('pwd')
        pwd1 = request.POST.get('pwd1')
        gender = request.POST.get('gender', default=0)
        hobby = request.POST.getlist('hobby', default=[])
        cover = request.FILES.get('avator')

        user = User.objects.filter(phone=phone).all()

        ctx = {
            'phone': phone,
            'nickname': nickname,
            'pwd': pwd,
            'pwd1': pwd1,
            'gender': gender,
            'error': ''
        }

        if user:
            ctx['error'] = '手机号已存在'
            return render(request, 'register.html', ctx)

        if not phone or not check_phone(phone):
            ctx['error'] = '手机号不合法'
            return render(request, 'register.html', ctx)

        if not nickname:
            ctx['error'] = '昵称不能为空'
            return render(request, 'register.html', ctx)

        if not pwd or not pwd1:
            ctx['error'] = '密码不能为空'
            return render(request, 'register.html', ctx)

        if len(pwd) < 6 or len(pwd) > 16:
            ctx['error'] = '密码位数不对'
            return render(request, 'register.html', ctx)
        if pwd != pwd1:
            ctx['error'] = '密码位数不对'
            return render(request, 'register.html', ctx)

        if not gender or gender not in ['0', '1']:
            ctx['error'] = '性别不合法'
            return render(request, 'register.html', ctx)

        if not hobby:
            ctx['error'] = '请传爱好'
            return render(request, 'register.html', ctx)

        for h in hobby:
            if h not in ['喝酒', '抽烟', '烫头']:
                ctx['error'] = '爱好不合法'
                return render(request, 'register.html', ctx)

        # 头像

        path = upload(cover)
        if not path:
            return HttpResponse('图片上传失败')

        User.objects.create(
            phone=phone,
            nickname=nickname,
            pwd=get_spwd(pwd),
            gender=gender,
            hobby=",".join(hobby),
            avator=path
        )
        return redirect(reverse("app:login"))


def login(request):
    # ctx = {
    # 'a':1
    # }

    if request.method == 'GET':
        captcha = str(random.randint(1000, 9999))
        request.session['captcha'] = captcha
        print(captcha)
        return render(request, 'login.html')
    else:
        phone = request.POST.get('phone')
        pwd = request.POST.get('pwd')
        code = request.POST.get('code')

        ctx = {
            'phone': phone,
            'pwd': pwd,
            'error': ''
        }
        if not phone or not check_phone(phone):
            ctx['error'] = '手机号不合法'
            return render(request, 'login.html', ctx)

        if not pwd:
            ctx['error'] = '密码不能为空'
            return render(request, 'login.html', ctx)

        if len(pwd) < 6 or len(pwd) > 16:
            ctx['error'] = '密码位数不对'
            return render(request, 'login.html', ctx)

        if code != request.session.get('captcha'):
            ctx['error'] = '验证码不对'
            return render(request, 'login.html', ctx)

        user = User.objects.filter(phone=phone).first()

        if not user:
            ctx['error'] = '没有该用户'
            return render(request, 'login.html', ctx)

        if user.pwd != get_spwd(pwd):
            ctx['error'] = '密码不对'
            return render(request, 'login.html', ctx)

        request.session['uid'] = user.id
        # 设置过期时间
        return redirect(reverse('app:index'))

        '''
        '''


def logout(request):
    request.session.flush()
    return redirect(reverse('app:index'))
