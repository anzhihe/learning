from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import re
from .models import User
import hashlib
from datetime import datetime


# Create your views here.

def show_req(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.COOKIES)
    print(request.session)
    print(request.get_full_path())
    print(request.path_info)
    return HttpResponse('ok')


def index(request):
    '''
{'csrftoken': '009CPRXhQy4o0xfrc5Upzyj7HK95dgWhR1uMlo8CSUvDg7879hFtDA9Sy07RfoTl', 'uid': '3', 'islogin': '1'}

    :param request:
    :return:
    '''
    cookies = request.COOKIES
    uid = cookies.get('uid')
    islogin = cookies.get('islogin')
    user = None
    if islogin == '1':
        print('登录过')
        user = User.objects.filter(id=uid).first()
        return render(request, 'reqapp/index.html', locals())
    else:
        print('没有登录过')
        return render(request, 'reqapp/index.html', locals())


def show_get(request):
    return render(request, 'reqapp/test_get.html')


def check_phone(phone):
    return re.match(r'1[3456789]\d{9}', phone)


def get_spwd(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode())
    return md5.hexdigest()


def register(request):
    phone = request.GET.get('phone')

    pwd = request.GET.get('pwd')
    pwd1 = request.GET.get('pwd1')
    gender = request.GET.get('gender', default='男')
    # 如果是一键多值的话
    hobby = request.GET.getlist('hobby', default=[])
    # print(phone, pwd, pwd1, gender, hobby)

    user = User.objects.filter(phone=phone).all()
    if user:
        return HttpResponse('手机号已存在')

    if not phone or not check_phone(phone):
        return HttpResponse('手机号不合法')

    if not pwd or not pwd1:
        return HttpResponse('请传密码')

    if len(pwd) < 6 or len(pwd) > 16:
        return HttpResponse('密码不合法')
    if pwd != pwd1:
        return HttpResponse('两次密码不一样')

    if not gender or gender not in ['男', '女']:
        return HttpResponse('性别不合法')

    if not hobby:
        return HttpResponse('请传爱好')

    for h in hobby:
        if h not in ['喝酒', '抽烟', '烫头']:
            return HttpResponse('没有此项')

    User.objects.create(
        phone=phone,
        pwd=get_spwd(pwd),
        gender=gender,
        hobby=",".join(hobby)
    )
    '''
    定义模型类
    
    判断每个参数是否合法
    把接到这些值赋值模型类然后保存
    
    密码采用md5
    
    永远不要相信用户的输入
    
    '''
    return redirect('/reqapp/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'reqapp/test_post.html')
    else:
        phone = request.POST.get('phone')
        pwd = request.POST.get('pwd')
        if not phone or not check_phone(phone):
            return HttpResponse('手机号不合法')

        if len(pwd) < 6 or len(pwd) > 16:
            return HttpResponse('密码不合法')

        user = User.objects.filter(phone=phone).all()

        # ['objectxxdas12321'].
        if not user:
            return HttpResponse('未注册')

        if len(user) > 1:
            return HttpResponse('服务器错误')

        if user[0].pwd == get_spwd(pwd):
            '''
            在这往cookie里面塞东西
            '''
            response = redirect('/reqapp')

            # response.set_cookie('uid', user[0].id,max_age=10)
            # response.set_cookie('islogin', 1,max_age=10)

            response.set_cookie('uid', user[0].id, expires=datetime(2019, 12, 21))
            response.set_cookie('islogin', 1, expires=datetime(2019, 12, 21))

            return response
        else:
            return HttpResponse('密码错误')


def logout(request):
    response = redirect('/reqapp')
    response.delete_cookie('uid')
    response.delete_cookie('islogin')
    return response


'''
http://127.0.0.1:8000/reqapp/register/?phone=13888888888&pwd=123456&pwd1=123456&gender=%E7%94%B7&hobby=%E6%8A%BD%E7%83%9F&hobby=%E5%96%9D%E9%85%92&hobby=%E7%83%AB%E5%A4%B4
'''
