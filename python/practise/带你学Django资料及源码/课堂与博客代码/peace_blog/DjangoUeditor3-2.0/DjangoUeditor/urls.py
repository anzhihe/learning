#coding:utf-8
from .views import get_ueditor_controller
from django.urls import  path


urlpatterns = [
    path('controller/',get_ueditor_controller),
]