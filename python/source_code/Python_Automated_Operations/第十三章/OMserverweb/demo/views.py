from django.utils.log import logger
from django.http import HttpResponse  

def index(request):
    logger.error('Test Django Logging')
    return HttpResponse("Hello world Django.")
