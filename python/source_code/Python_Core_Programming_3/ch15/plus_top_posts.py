#!/usr/bin/env python

import datetime as dt
from apiclient.discovery import build

WIDTH = 40
MAX_DEF = 5
MAX_RES = 20
MAX_TOT = 60
UID = '102108625619739868700'
HR = '\n%s' % ('-' * WIDTH)
API_KEY = 'YOUR_KEY_FROM_CONSOLE_API_ACCESS_PAGE'

class PlusService(object):
    def __init__(self):
        self.service = build("plus", "v1",
            developerKey=API_KEY)

    def get_posts(self, q, oldest, maxp=MAX_TOT):
        posts = []
        cap = min(maxp, MAX_RES)
        cxn = self.service.activities()
        handle = cxn.search(maxResults=cap, query=q)
        while handle:
            feed = handle.execute()
            if 'items' in feed:
                for activity in feed['items']:
                    if oldest > activity['published']:
                        return posts
                    if q not in activity['title']:
                        continue
                    posts.append(PlusPost(activity))
                    if len(posts) >= maxp:
                        return posts
                handle = cxn.search_next(handle, feed)
            else:
                return posts
        else:
            return posts

    def get_user(self, uid):
        return self.service.people().get(userId=uid).execute()

scrub = lambda x: ' '.join(x.strip().split())

class PlusPost(object):
    def __init__(self, record):
        self.title = scrub(record['title'])
        self.post = scrub(record['object'].get(
            'originalContent', ''))
        self.link = record['url']
        self.when = dt.datetime.strptime(
            record['published'],
            "%Y-%m-%dT%H:%M:%S.%fZ")
        actor = record['actor']
        self.author = '%s (%s)' % (
            actor['displayName'], actor['id'])
        obj = record['object']
        cols = ('replies', 'plusoners', 'resharers')
        self.chatter = \
            sum(obj[col]['totalItems'] for col in cols)

def top_posts(query, maxp=MAX_DEF, ndays=7):
    print '''
*** Searching for the top %d posts matching \
%r over the past %d days...''' % (maxp, query, ndays)
    oldest = (dt.datetime.now()-dt.timedelta(ndays)).isoformat()
    posts = service.get_posts(query, oldest, maxp)
    if not posts:
        print '*** no results found... try again ***'
        return
    sorted_posts = sorted(posts, reverse=True,
        key=lambda post: post.chatter)
    for i, post in enumerate(sorted_posts):
        print '\n%d)' % (i+1)
        print 'From:', post.author
        print 'Date:', post.when.ctime()
        print 'Chatter score:', post.chatter
        print 'Post:', post.post if len(post.post) > \
            len(post.title) else post.title
        print 'Link:', post.link
        print HR

def find_top_posts(query=None, maxp=MAX_DEF):
    if not query:
        query = raw_input('Enter search term [python]: ')
    if not query:
        query = 'python'
    top_posts(query, maxp)
py_top_posts = lambda: find_top_posts('python')

def find_user():
    uid = raw_input('Enter user ID [%s]: ' % UID).strip()
    if not uid:
        uid = UID
    if not uid.isdigit():
        print '*** ERROR: Must enter a numeric user ID'
        return
    user = service.get_user(uid)
    print 'Name:', user['displayName']
    print 'URL:', user['url']
    print 'Pic:', user['image']['url']
    print 'About:', user.get('aboutMe', '')

def _main():
    menu = {
        't': ('Top 5 posts in past 7 days query', find_top_posts),
        'p': ('Top 5 Python posts in past 7 days', py_top_posts),
        'u': ('Fetch user profile (by ID)', find_user),
    }
    prompt = ['(%s) %s' % (item, menu[item][0]) for item in menu]
    prompt.insert(0, '%s\n%s%s' % (HR,
        'Google+ Command-Line Tool v0.4'.center(WIDTH), HR))
    prompt.append('\nEnter choice [QUIT]: ')
    prompt = '\n'.join(prompt)
    while True:
        ch = raw_input(prompt).strip().lower()
        if not ch or ch not in menu:
            break
        menu[ch][1]()

if __name__ == '__main__':
    service = PlusService()
    _main()
