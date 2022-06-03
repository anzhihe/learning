"""Dj040201 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views as student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_views.index, name='index'),
    path('view/', student_views.view, name='view_student'),
    path('modify/', student_views.modify, name='modify_student'),
    path('add/', student_views.add, name='add_student'),
    path('delete/', student_views.delete, name='delete_student'),
    path('add_many/', student_views.add_many, name='addmany_student'),
    path('read/', student_views.read, name='read'),
]
