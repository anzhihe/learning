#!/usr/bin/env python
# http://oscon.com/oscon2012/public/schedule/detail/24416

# plus_u.py (by Wesley Chun under CC-SA3.0 license)
from apiclient import discovery
import settings

service = discovery.build('plus', 'v1', developerKey=settings.API_KEY)

print '\n*** Search for "python" (authorization NOT required)'
feed = service.activities().search(query='python').execute()
for data in feed['items']:
    post = ' '.join(data['title'].strip().split())
    if post:
        print '''
    User: %s
    Date: %s
    Post: %s''' % (data['actor']['displayName'],
        data['published'], post)
