# urls.py
from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'archive'),
    url(r'^create/', 'create_blogpost'),
)
