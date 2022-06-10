from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.ListView.as_view(), name='list'),
    path('detail/<int:id>/', views.DetailView.as_view(), name='detail'),
    path('category/<int:id>/', views.CategoryView.as_view(), name='category'),
    path('tag/<int:id>/', views.TagView.as_view(), name='tag'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.log_out, name='logout'),
    path('comment/', views.comment, name='comment'),
]
