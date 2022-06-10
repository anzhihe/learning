"""my_common URL Configuration

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
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('app01/', include(('app01.urls', 'app01'), namespace='app01')),
                  path('app02/', include(('app02.urls', 'app02'), namespace='app02')),
                  path('app03/', include(('app03.urls', 'app03'), namespace='app03')),
                  path('app04/', include(('app04.urls', 'app04'), namespace='app04')),
                  path('app05/', include(('app05.urls', 'app05'), namespace='app05')),
                  path('app06/', include(('app06.urls', 'app06'), namespace='app06')),
                  path('app07/', include(('app07.urls', 'app07'), namespace='app07')),
                  path('app08/', include(('app08.urls', 'app08'), namespace='app08')),
                  path('app09/', include(('app09.urls', 'app09'), namespace='app09')),
                  path('captcha/', include('captcha.urls')),
                  path('search/', include('haystack.urls')),

                  path('ueditor/', include('DjangoUeditor.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
