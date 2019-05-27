#!/usr/bin/env python
# http://oscon.com/oscon2012/public/schedule/detail/24416

# twy_a.py (by Wesley Chun under CC-SA3.0 license)
from distutils.log import warn as printf
try:
    import twython
except ImportError:
    import twython3k as twython
import settings

printf('\n*** Get user status (authorization required)')
twitter = twython.Twython(
    twitter_token=settings.CONSUMER_KEY,
    twitter_secret=settings.CONSUMER_SECRET,
    oauth_token=settings.ACCESS_TOKEN,
    oauth_token_secret=settings.ACCESS_TOKEN_SECRET,
)
data = twitter.verifyCredentials()
status = data['status']
printf('''
    User: @%s
    Date: %s
    Tweet: %s''' % (data['screen_name'],
        status['created_at'], status['text'])
)
