from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_parent/', views.get_parent),
    path('get_area/<int:id>/', views.get_area),
]
