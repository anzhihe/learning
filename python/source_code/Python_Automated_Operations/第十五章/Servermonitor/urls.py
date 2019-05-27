# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    #(r'^push/',index),
    url(r'^$','webmonitor.views.index'),
    url(r'^webmonitor/', include('webmonitor.urls')),
)
