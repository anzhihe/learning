from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('son1/', views.son1),
    path('son2/', views.son2),
    path('escape/', views.escape),
    path('center/', views.center, name='center'),
    path('center1/', views.center1, name='center1'),
    # path('center2/<int:id>/', views.center2, name='center2'),
    # re_path(r'^center2/(?P<id>\d+)/', views.center2, name='center2'),

    re_path(r'^center2/(\d+)/', views.center2, name='center2'),

]
