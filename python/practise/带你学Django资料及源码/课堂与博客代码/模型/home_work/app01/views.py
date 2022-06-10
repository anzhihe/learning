from django.shortcuts import render

from .models import Person


# Create your views here.

def index(request):
    persons = Person.objects.all()
    return render(request, 'app01/index.html', locals())


def show(request, id):
    person = Person.objects.filter(pk=id).first()
    # person = Person.objects.get(id=id)

    return render(request, 'app01/resume.html', locals())
