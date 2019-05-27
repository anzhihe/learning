#!/usr/bin/env python
# http://oscon.com/oscon2012/public/schedule/detail/24416

# twe_a.py (by Wesley Chun under CC-SA3.0 license)
import tweepy
import settings

print '\n*** Get user status (authorization required)'
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
data = tweepy.API(auth).verify_credentials()
status = data.status
print '''
    User: @%s
    Date: %s
    Tweet: %s''' % (data.screen_name, status.created_at, status.text)
