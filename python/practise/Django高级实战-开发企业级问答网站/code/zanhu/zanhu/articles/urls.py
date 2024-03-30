#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from django.urls import path
from django.views.decorators.cache import cache_page

from zanhu.articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='list'),
    path('write-new-article/', views.CreateArticleView.as_view(), name='write_new'),
    path('drafts/', views.DraftsListView.as_view(), name='drafts'),
    path('<str:slug>/', cache_page(60 * 5)(views.DetailArticleView.as_view()), name='article'),
    path('edit/<int:pk>/', views.EditArticleView.as_view(), name='edit_article'),
]
