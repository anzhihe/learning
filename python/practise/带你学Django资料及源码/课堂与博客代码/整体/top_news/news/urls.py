from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news/<int:id>/', views.detail),
    path('del/<int:id>/', views.delete),
]
