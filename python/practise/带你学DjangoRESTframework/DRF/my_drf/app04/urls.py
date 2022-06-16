from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game-detail'),
    path('games/', views.GameList.as_view(), name='game-list'),

]
