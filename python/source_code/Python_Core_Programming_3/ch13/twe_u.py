#!/usr/bin/env python
# http://oscon.com/oscon2012/public/schedule/detail/24416

# twe_u.py (by Wesley Chun under CC-SA3.0 license)
import tweepy

print '\n*** Search for "python" (authorization NOT required)'
data = tweepy.api.search(q='python')
for tweet in data:
    print '''
    User: @%s
    Date: %s
    Tweet: %s''' % (tweet.from_user, tweet.created_at, tweet.text)
