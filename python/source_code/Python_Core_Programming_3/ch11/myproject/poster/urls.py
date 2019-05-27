from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.poster.views',
    (r'^$', 'post_tweet'),
    (r'^thankyou', 'thank_you'),
    (r'^edit/(?P<tweet_id>\d+)', 'post_tweet'),
)
