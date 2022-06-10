from django.shortcuts import render
from .models import News


# Create your views here.

def index(request):
    news = News.objects.all()
    return render(request, 'app03/index.html',locals())
