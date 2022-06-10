from django.urls import path
from . import views

urlpatterns = [
    # path('', views.show_req),
    path('', views.index),
    path('register1/', views.show_get),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),

]
