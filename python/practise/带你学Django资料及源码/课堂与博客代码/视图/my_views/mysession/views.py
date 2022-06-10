from django.shortcuts import render
import random
from django.http import HttpResponse, JsonResponse
import json
from django.shortcuts import redirect, reverse


# Create your views here.

def login(request):
    if request.method == 'GET':
        captcha = str(random.randint(1000, 9999))
        print(captcha)
        response = render(request, 'mysession/mysession.html')
        # response.set_cookie('captcha', captcha)
        request.session['captcha'] = captcha
        # request.session.set_expiry(15 * 60)
        # request.session.clear()  # 删除值
        request.session.flush()  # 全部删除
        # del request.session['captcha']
        return response
    else:
        print('大会授课计划登记卡山东矿机哈加快点哈科技')
        '''
        接受参数
        验证参数
        '''
        code = request.POST.get('code')  # 前端发过验证码
        # code1 = request.COOKIES.get('captcha')

        code1 = request.session.get('captcha')

        print(code1, code)
        if code == code1:
            return HttpResponse('OK')
        else:
            return HttpResponse('fail')


def get_json(request):
    ctx = {'code': 1, 'msg': "成功", 'data': {
        'users': [
            {
                'name': 'laowang',
                'age': 12
            },
            {
                'name': 'laosong',
                'age': 15
            },
        ]
    }
           }

    return JsonResponse(ctx, safe=True)


# 重定向
def show(request):
    return HttpResponse('ok')


def show1(request):
    return redirect(reverse('mysession:show'))


# 重定向参数


def show2(request, id):
    return HttpResponse(id)

def show3(request):
    # return redirect(reverse('mysession:show2', kwargs={'id': 1})) # 关键字参数
    return redirect(reverse('mysession:show2', args=(1,)))  # 位置参数
