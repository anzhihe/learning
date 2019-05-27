from django.conf.urls.defaults import *

urlpatterns = patterns('webmonitor.views',
    (r'^$','index'),
    (r'add_do/','adddo'),
    (r'add/','add'),
    (r'monitorlist/','monitorlist'),
)