from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('search/', views.search),
    path('detail/<int:id>', views.detail,name='detail'),
]
