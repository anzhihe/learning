#!/usr/bin/env python

# plus.py (by Wesley Chun under CC-SA3.0 license)
from apiclient import discovery

API_KEY = YOUR_KEY_FROM_CONSOLE_API_ACCESS_PAGE
service = discovery.build("plus", "v1", developerKey=API_KEY)
feed = service.activities().search(query='android').execute()
for record in feed['items']:
    post = ' '.join(record['title'].strip().split())
    if post:
        print '\nFrom:', record['actor']['displayName']
        print 'Post:', post
        print 'Date:', record['published']
