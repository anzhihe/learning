"""Dj040501 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # 模块
from django.urls import path
from library import views as library_views

urlpatterns = [
    path('admin/', admin.site.urls),  # 登录后台的URL
    path('', library_views.index, name='index'),
    path('selectclick/', library_views.select_click, name='select'),
    path('get_keyword/', library_views.get_keyword, name='keyword'),
    path('get_all/', library_views.get_all_book, name='getall'),
    path('order', library_views.get_order_number, name='order'),
]
