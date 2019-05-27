# views.py
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from blog.models import BlogPost, BlogPostForm

def archive(request):
    posts = BlogPost.objects.all()[:10]
    return direct_to_template(request, 'archive.html',
        {'posts': posts, 'form': BlogPostForm()})

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')
