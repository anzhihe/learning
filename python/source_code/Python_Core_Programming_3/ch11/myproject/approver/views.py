# approver/views.py
from datetime import datetime
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from twython import Twython
from myproject import settings
from myproject.poster.views import *
from myproject.poster.models import Tweet, Comment

@permission_required('poster.can_approve_or_reject_tweet',
    login_url='/login')
def list_tweets(request):
    pending_tweets = Tweet.objects.filter(
        state = 'pending').order_by('created_at')
    published_tweets = Tweet.objects.filter(
        state = 'published').order_by('-published_at')
    return render_to_response('list_tweets.html',
        {'pending_tweets': pending_tweets,
         'published_tweets': published_tweets})

class ReviewForm(forms.Form):
    new_comment = forms.CharField(max_length=300,
        widget=forms.Textarea(attrs = {'cols': 50, 'rows': 6}),
        required=False)
    APPROVAL_CHOICES = (
        ('approve', 'Approve this tweet and post it to Twitter'),
        ('reject',
         'Reject tweet and return to author with your comments'),
    )
    approval = forms.ChoiceField(
        choices = APPROVAL_CHOICES, widget = forms.RadioSelect)

@permission_required('poster.can_approve_or_reject_tweet',
    login_url='/login')
def review_tweet(request, tweet_id):
    reviewed_tweet = Tweet.objects.get(id=tweet_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_comment = form.cleaned_data['new_comment']
            if form.cleaned_data['approval'] == 'approve':
                publish_tweet(reviewed_tweet)
                send_approval_email(reviewed_tweet, new_comment)
                reviewed_tweet.published_at = datetime.now()
                reviewed_tweet.state = 'published'
            else:
                link = request.build_absolute_uri(
                    reverse(post_tweet, args = [reviewed_tweet.id]))
                send_rejection_email(reviewed_tweet, new_comment,
                    link)
                reviewed_tweet.state = 'rejected'
            reviewed_tweet.save()
            if new_comment:
                c = Comment(tweet=reviewed_tweet, text=new_comment)
                c.save()
            return HttpResponseRedirect('/approve/')
    else:
        form = ReviewForm()
    return direct_to_template(request, 'review_tweet.html', {
        'form': form, 'tweet': reviewed_tweet,
        'comments': reviewed_tweet.comment_set.all()})

def send_approval_email(tweet, new_comment):
    body = ['Your tweet (%r) was approved & published on Twitter.' \
        % tweet.text]
    if new_comment:
        body.append(
            'The reviewer gave this feedback: %r.' % new_comment)
    send_mail('Tweet published', '%s\r\n' % ' '.join(
        body), settings.DEFAULT_FROM_EMAIL, [tweet.author_email])

def send_rejection_email(tweet, new_comment, link):
    body = ['Your tweet (%r) was rejected. ' % tweet.text]
    if new_comment:
        body.append(
            'The reviewer gave this feedback: %r.' % new_comment)
    body.append('To edit your proposed tweet, go to %s.' % link)
    send_mail('Tweet rejected', '%s\r\n' % (' '.join(
        body), settings.DEFAULT_FROM_EMAIL, [tweet.author_email])

def publish_tweet(tweet):
    twitter = Twython(
        twitter_token=settings.TWITTER_CONSUMER_KEY,
        twitter_secret=settings.TWITTER_CONSUMER_SECRET,
        oauth_token=settings.TWITTER_OAUTH_TOKEN,
        oauth_token_secret=settings.TWITTER_OAUTH_TOKEN_SECRET
    )
    twitter.updateStatus(status=tweet.text.encode("utf-8"))
