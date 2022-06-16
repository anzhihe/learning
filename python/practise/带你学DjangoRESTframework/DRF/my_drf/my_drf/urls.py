"""my_drf URL Configuration

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
from django.urls import path, include
from app01 import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'groups', views.GroupViewSet)

'''
http://127.0.0.1:8000/api/students/
http://127.0.0.1:8000/api/students/1/


'''
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/users/', views.index),
    # path('api/', include(router.urls)),
    # path('api/', include(('app02.urls', 'app02'), namespace='app02')),
    # path('api/', include(('app03.urls', 'app03'), namespace='app03')),
    # path('api/', include(('app04.urls', 'app04'), namespace='app04')),
    # path('api/', include(('app05.urls', 'app05'), namespace='app05')),
    path('api/<str:version>/', include(('app06.urls', 'app06'), namespace='app06')),
    # path('api-token-auth/', obtain_auth_token),
    path('api-token-auth/', obtain_jwt_token),
    # path('docs/', include_docs_urls(title='测试平台接口文档'))
]
