from django.contrib import admin
from django.urls import path, register_converter, re_path
from . import views

urlpatterns = [
    path('login/', views.login),  # 分发
    path('get_json/', views.get_json),  # 返回json数据
    path('show/', views.show, name='show'),  # 重定向
    path('show1/', views.show1, name='show1'),  # 重定向


    # path('show2/<int:id>/', views.show2, name='show2'),  # 重定向关键参数
    # path('show3/', views.show3, name='show3'),  # 重定向关键字参数
    re_path(r'^show2/(?P<id>\d+)/$', views.show2, name='show2'),  # 重定向关键字参数


    re_path(r'^show2/(\d+)/$', views.show2, name='show2'),  # 重定向位置参数
    re_path(r'^show3/$', views.show3, name='show3'),  # 重定向位置参数

]
