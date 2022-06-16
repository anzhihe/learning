from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('users/', views.user_list, name='user-list'),
    path('users/', views.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', views.user_detail, name='user-detail'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

]
