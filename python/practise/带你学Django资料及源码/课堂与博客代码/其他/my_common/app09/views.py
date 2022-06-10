from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(15 * 60)
def index(request):
    return HttpResponse('ok1100000')


def index1(request):
    return render(request, 'app09/index.html')
