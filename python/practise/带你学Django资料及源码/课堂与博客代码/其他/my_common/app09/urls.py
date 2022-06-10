from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('index1', views.index1),
]
