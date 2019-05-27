# urls.py
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^post/', include('poster.urls')), #(r'^post/', include('myproject.poster.urls')),
    (r'^$', include('poster.urls')),   #(r'^$', include('myproject.poster.urls')),
    (r'^approve/', include('approver.urls')), #(r'^approve/', include('myproject.approver.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^login', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    (r'^logout', 'django.contrib.auth.views.logout'),
)
