# poster/views.py
from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from myproject import settings
from models import Tweet

class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ('text', 'author_email')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }

def post_tweet(request, tweet_id=None):
    tweet = None
    if tweet_id:
        tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.state = 'pending'
            new_tweet.save()
            send_review_email()
            return HttpResponseRedirect('/post/thankyou/')
    else:
        form = TweetForm(instance=tweet)
    return direct_to_template(request, 'post_tweet.html',
        {'form': form})

def send_review_email(tweet):
    subject = 'Action required: review tweet'
    body = 'A new tweet has been submitted for approval '
        'Please review it as soon as possible.')
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
        [settings.TWEET_APPROVER_EMAIL])

def thank_you(request):
    tweets_in_queue = Tweet.objects.filter(
        state='pending').aggregate(Count('id')).values()[0]
    return direct_to_template(request, 'thank_you.html',
        {'tweets_in_queue': tweets_in_queue})
