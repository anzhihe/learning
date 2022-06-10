from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def search(request):
    return render(request, 'app08/search.html')


def detail(request, id):
    return HttpResponse(id)
