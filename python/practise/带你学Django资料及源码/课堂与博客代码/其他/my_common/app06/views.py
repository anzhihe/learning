from django.shortcuts import render

# Create your views here.
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        return render(request, 'app06/index.html')
    else:
        '''
        验证手机号合法
        密码合法不
        两次密码是否一样
        '''
        pass


# 用forms生成form表单
def login(request):
    loginform = LoginForm()
    return render(request, 'app06/login.html', locals())


'''
ModelForm
'''


def register(request):
    registerform = RegisterForm()
    if request.method == 'GET':
        return render(request, 'app06/register.html', locals())
    else:
        obj_post = RegisterForm(request.POST)
        if obj_post.is_valid():

            # 存数据库
            return HttpResponse("ok")
        else:
            return render(request, 'app06/register.html', locals())
