from django.conf.urls.defaults import *

urlpatterns = patterns('omaudit.views',
    (r'^$','index'),
    (r'omaudit_pull/$','omaudit_pull'),
    (r'omaudit_run/$','omaudit_run'),
)
