from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=140)
    author_email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    STATE_CHOICES = (
        ('pending',    'pending'),
        ('published',  'published'),
        ('rejected',   'rejected'),
    )
    state = models.CharField(max_length=15, choices=STATE_CHOICES)

    def __unicode__(self):
        return self.text

    class Meta:
        permissions = (
            ("can_approve_or_reject_tweet",
            "Can approve or reject tweets"),
        )

class Comment(models.Model):
    tweet = models.ForeignKey(Tweet)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
