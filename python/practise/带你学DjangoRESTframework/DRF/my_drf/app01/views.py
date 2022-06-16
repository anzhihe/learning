from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.

def index(request):
    ctx = {
        "code": 1,
        "msg": "ok",
        "data": {
            "users": [
                {
                    "name": "老王",
                    "age": 12,
                },
                {
                    "name": "老王",
                    "age": 32,
                },
                {
                    "name": "老王",
                    "age": 22,
                }
            ]
        }
    }

    return JsonResponse(ctx)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()  # 要序列化的数据
    serializer_class = GroupSerializer  # 要是哪个序列化类
