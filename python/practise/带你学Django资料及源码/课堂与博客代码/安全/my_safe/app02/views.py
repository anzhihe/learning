from django.shortcuts import render
from .models import Comment
from django.shortcuts import redirect
from bleach.sanitizer import ALLOWED_TAGS, ALLOWED_ATTRIBUTES

import bleach


# Create your views here.
def index(request):
    comments = Comment.objects.all()
    return render(request, 'app02/index.html', locals())


def add_comment(request):
    content = request.POST.get('content')
    # 验证

    tags = ALLOWED_TAGS + ['img']  # img也是合法
    attributes = {**ALLOWED_ATTRIBUTES, 'img': ['src']}  # src属性合法

    content = bleach.clean(content, tags, attributes)
    Comment.objects.create(content=content)
    return redirect('/app02/')
