from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework.authentication import BaseAuthentication, BasicAuthentication, TokenAuthentication, \
    SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from .models import User, UserToken
from .throttlings import VisitThrottling
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.
import time
import hashlib
from django.http import HttpResponse


def get_md5(user):
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1, 'msg': None, 'data': {}}
        # user = request._request.POST.get('username')
        # user = request._request.POST.get('username')
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = User.objects.filter(username=user, password=pwd).first()
        if not obj:
            ret['code'] = -1
            ret['msg'] = "用户名或密码错误"
        token = get_md5(user)
        UserToken.objects.update_or_create(user=obj, defaults={'token': token})
        ret['token'] = token
        return JsonResponse(ret)


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        obj = UserToken.objects.filter(token=token).first()
        if not obj:
            raise exceptions.AuthenticationFailed('验证失败')
        else:
            return (obj.user, obj)


class CartView(APIView):
    #  都是局部的

    # 基于什么登录认证的
    # authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]

    # 自己写的认证类
    # authentication_classes = [MyAuthentication]

    # 基于jwt验证
    # authentication_classes = [JSONWebTokenAuthentication]

    # 只有登录才能访问
    # permission_classes = [IsAuthenticated]

    # 自己的权限
    # permission_classes = [MyPermission]

    # 节流 局部
    throttle_classes = [VisitThrottling]

    def get(self, request, *args, **kwargs):
        ctx = {
            "code": 1,
            "msg": "ok",
            "data": {
                "goods": [
                    {
                        "name": "苹果",
                        "price": 12
                    },
                    {
                        "name": "苹果1",
                        "price": 13
                    },
                ]
            }
        }
        return JsonResponse(ctx)

    def put(self, request, *args, **kwargs):
        return HttpResponse('ok')


class VersionView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.version)

        if request.version == 'v1':
            ctx = {"code": 1, "msg": "ok", "data": {}}
            return JsonResponse(ctx)
        else:
            ctx = {"code": 2, "msg": "ok", "data": {}}
            return JsonResponse(ctx)
