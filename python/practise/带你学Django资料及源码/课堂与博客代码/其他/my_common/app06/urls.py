from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('send/', views.send),
    path('login/', views.login),
    path('register/', views.register),
]
