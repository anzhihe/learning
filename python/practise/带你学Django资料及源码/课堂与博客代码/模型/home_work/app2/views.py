from django.shortcuts import render
from .models import NavCategory
# Create your views here.

def index(request):
    navcategorys = NavCategory.objects.filter(is_show=True).order_by('-position').all()
    return render(request,'app2/index.html',locals())