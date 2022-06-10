from django.shortcuts import render
from .models import *
from django.db.models import Sum
from django.db.models import Q


# Create your views here.

def index(request):
    # ctrl+shitf+u
    grades = Grades.objects.all()
    list = Student.objects.aggregate(Sum('age'))
    print(list)
    return render(request, 'index.html', locals())


def detail(request, id):
    stus = Student.objects.filter(grades=id).all()
    return render(request, 'detail.html', locals())
