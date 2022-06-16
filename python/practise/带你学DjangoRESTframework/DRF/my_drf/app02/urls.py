from django.contrib import admin
from django.urls import path, include
from app02 import views

urlpatterns = [
    path('articles/', views.article_list, name='article-list'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),

    path('categorys/', views.category_list, name='category-list'),
    path('categorys/<int:id>/', views.category_detail, name='category-detail'),

    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<int:id>/', views.tag_detail, name='tag-detail'),

]
