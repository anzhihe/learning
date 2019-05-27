#!/usr/bin/env python

from distutils.log import warn as printf
from unittest import TestCase, main
from tweet_auth import *

# set up supported APIs
CMDs = {
    'twython': {
        'search':               'searchTwitter', # None for 1.4.4+
        'verify_credentials':   None,
        'user_timeline':        'getUserTimeline',
        'update_status':        None,
    },
    'tweepy': dict.fromkeys((
        'search',
        'verify_credentials',
        'user_timeline',
        'update_status',
    )),
}
APIs = set(CMDs)

# remove unavailable APIs
remove = set()
for api in APIs:
    try:
        __import__(api)
    except ImportError:
        try:
            __import__('%s3k' % api)
        except ImportError:
            remove.add(api)

APIs.difference_update(remove)
if not APIs:
    raise NotImplementedError(
        'No Twitter API found; install one & add to CMDs!')

class Twitter(object):
    'Twitter -- Use available APIs to talk to Twitter'
    def __init__(self, api, auth=True):
        if api not in APIs:
            raise NotImplementedError(
                '%r unsupported; try one of: %r' % (api, APIs))

        self.api = api
        if api == 'twython':
            try:
                import twython
            except ImportError:
                import twython3k as twython
            if auth:
                self.twitter = twython.Twython(
                    twitter_token=consumer_key,
                    twitter_secret=consumer_secret,
                    oauth_token=access_token,
                    oauth_token_secret=access_token_secret,
                )
            else:
                self.twitter = twython.Twython()
        elif api == 'tweepy':
            import tweepy
            if auth:
                auth = tweepy.OAuthHandler(consumer_key,
                    consumer_secret)
                auth.set_access_token(access_token,
                    access_token_secret)
                self.twitter = tweepy.API(auth)
            else:
                self.twitter = tweepy.api

    def _get_meth(self, cmd):
        api = self.api
        meth_name = CMDs[api][cmd]
        if not meth_name:
            meth_name = cmd
            if api == 'twython' and '_' in meth_name:
                cmds = cmd.split('_')
                meth_name = '%s%s' % (cmds[0], cmds[1].capitalize())
        return getattr(self.twitter, meth_name)

    def search(self, q):
        api = self.api
        if api == 'twython':
            res = self._get_meth('search')(q=q)['results']
            return (ResultsWrapper(tweet) for tweet in res)
        elif api == 'tweepy':
            return (ResultsWrapper(tweet)
                for tweet in self._get_meth('search')(q=q))

    def verify_credentials(self):
        return ResultsWrapper(
            self._get_meth('verify_credentials')())

    def user_timeline(self):
        return (ResultsWrapper(tweet)
            for tweet in self._get_meth('user_timeline')())

    def update_status(self, s):
        return ResultsWrapper(
            self._get_meth('update_status')(status=s))

class ResultsWrapper(object):
    "ResultsWrapper -- makes foo.bar the same as foo['bar']"
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return str(self.obj)

    def __repr__(self):
        return repr(self.obj)

    def __getattr__(self, attr):
        if hasattr(self.obj, attr):
            return getattr(self.obj, attr)
        elif hasattr(self.obj, '__contains__') and attr in self.obj:
            return self.obj[attr]
        else:
            raise AttributeError(
                '%r has no attribute %r' % (self.obj, attr))

    __getitem__ = __getattr__

def _demo_search():
    for api in APIs:
        printf(api.upper())
        t = Twitter(api, auth=False)
        tweets = t.search('twython3k')
        for tweet in tweets:
            printf('----' * 10)
            printf('@%s' % tweet.from_user)
            printf('Status: %s' % tweet.text)
            printf('Posted at: %s' % tweet.created_at)
        printf('----' * 10)

def _demo_ver_creds():
    for api in APIs:
        t = Twitter(api)
        res = t.verify_credentials()
        status = ResultsWrapper(res.status)
        printf('@%s' % res.screen_name)
        printf('Status: %s' % status.text)
        printf('Posted at: %s' % status.created_at)
        printf('----' * 10)

def _demo_user_timeline():
    for api in APIs:
        printf(api.upper())
        t = Twitter(api)
        tweets = t.user_timeline()
        for tweet in tweets:
            printf('----' * 10)
            printf('Status: %s' % tweet.text)
            printf('Posted at: %s' % tweet.created_at)
        printf('----' * 10)

def _demo_update_status():
    for api in APIs:
        t = Twitter(api)
        res = t.update_status(
            'Test tweet posted to Twitter using %s' % api.title())
        printf('Posted at: %s' % res.created_at)
        printf('----' * 10)

# object wrapper unit tests
def _unit_dict_wrap():
    d = {'foo': 'bar'}
    wrapped = ResultsWrapper(d)
    return wrapped['foo'], wrapped.foo

def _unit_attr_wrap():
    class C(object):
        foo = 'bar'
    wrapped = ResultsWrapper(C)
    return wrapped['foo'], wrapped.foo

class TestSequenceFunctions(TestCase):
   def test_dict_wrap(self):
       self.assertEqual(_unit_dict_wrap(), ('bar', 'bar'))

   def test_attr_wrap(self):
       self.assertEqual(_unit_attr_wrap(), ('bar', 'bar'))

if __name__ == '__main__':
    printf('\n*** SEARCH')
    _demo_search()
    printf('\n*** VERIFY CREDENTIALS')
    _demo_ver_creds()
    printf('\n*** USER TIMELINE')
    _demo_user_timeline()
    printf('\n*** UPDATE STATUS')
    _demo_update_status()
    printf('\n*** RESULTS WRAPPER')
    main()
