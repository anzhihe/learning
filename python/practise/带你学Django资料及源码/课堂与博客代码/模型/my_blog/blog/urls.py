from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cat/<int:id>/', views.list),
    path('tag/<int:id>/', views.tlist)
]
