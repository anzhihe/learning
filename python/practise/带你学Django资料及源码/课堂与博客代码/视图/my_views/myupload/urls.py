from django.contrib import admin
from django.urls import path, register_converter, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 上传首页
    path('upload/', views.upload),  # 上传图片

]
