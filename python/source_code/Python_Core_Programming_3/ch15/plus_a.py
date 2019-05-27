#!/usr/bin/env python
# http://oscon.com/oscon2012/public/schedule/detail/24416

# plus_a.py (by Wesley Chun under CC-SA3.0 license)
import os
import httplib2
from apiclient import discovery
from oauth2client import file as storage, client, tools

store = storage.Storage(settings.AUTH_FILE)
credz = store.get() if os.path.exists(settings.AUTH_FILE) else None

if not credz:
    flow = client.OAuth2WebServerFlow(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        scope=settings.SCOPE,
        user_agent=settings.USER_AGENT,
    )
    credz = tools.run(flow, store)

access = credz.authorize(httplib2.Http())
service = discovery.build('plus', 'v1', http=access)

print '\n*** Get user status (authorization required)'
data = service.activities().list(userId='me', maxResults=1,
    collection='public').execute()['items'][0]
print '''
    User: %s
    Date: %s
    Post: %s''' % (
        data['actor']['displayName'], data['updated'],
        ' '.join(data['title'].strip().split())
    )
