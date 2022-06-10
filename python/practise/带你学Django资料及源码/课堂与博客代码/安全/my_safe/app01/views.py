from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.views import View

from django.utils.decorators import method_decorator


# Create your views here.

def index(request):
    return render(request, 'app01/index.html')


@csrf_exempt
def transfer(request):
    if request.method == 'POST':
        '''
        验证登录
        '''
        account = request.POST.get('account')
        money = request.POST.get('money')
        print('向对方{}，转了{}'.format(account, money))
        return HttpResponse('OK')


@method_decorator(csrf_exempt, name='dispatch')
class Transfer(View):
    def post(self, request, *args, **kwargs):
        '''
        验证登录
        '''
        account = request.POST.get('account')
        money = request.POST.get('money')
        print('向对方{}，转了{}'.format(account, money))
        return HttpResponse('OK')
