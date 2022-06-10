from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import ContactForm


def index(request):
    if request.method == 'GET':
        contactform = ContactForm()
        return render(request, 'app07/index.html', locals())
    else:
        contactform = ContactForm(request.POST)

        if contactform.is_valid():
            return HttpResponse('ok')
        return render(request, 'app07/index.html', locals())
