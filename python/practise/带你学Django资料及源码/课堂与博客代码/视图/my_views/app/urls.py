from django.contrib import admin
from django.urls import path, register_converter, re_path
from . import views

from . import converters

# 注册转换器
register_converter(converters.YearConverters, 'year')
urlpatterns = [
    path('', views.index),  # 分发
    path('show/<int:id>/<str:name>/', views.show),  # 分发
    # path('show1/<path:arg>', views.show1),  # 分发
    # path('show1/<str:arg>', views.show1),  # 分发
    # path('show1/<uuid:arg>', views.show1),  # 分发
    # path('show1/<int:arg>', views.show1),  # 分发
    # path('show1/<year:arg>', views.show1),  # 分发
    path('show1/<uuid:arg>', views.show1),  # 分发
    # re_path(r'^show2/(\d{4})/', views.show2), # 用正则写法
    re_path(r'^show2/(?P<id>\d{4})/(?P<id1>\d{4})/$', views.show2)  # 用正则写法

]
