# urls.py
from django.conf.urls.defaults import *

urlpatterns = patterns('approver.views',
    (r'^$', 'list_tweets'),
    (r'^review/(?P<tweet_id>\d+)', 'review_tweet'),
)
