from django.middleware.clickjacking import XFrameOptionsMiddleware

from django.utils.deprecation import MiddlewareMixin


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):  # 从上往下
        print('process_request')
        return None

    def process_view(self, request, callback, callback_args, callback_kwargs):  # 从上往下
        print('process_view')
        return None

    def process_exception(self, request, exception):  # 如果视图函数出现异常  # 从下往上
        print('process_exception')
        return None

    def process_response(self, request, response):  # 从下下往上
        print('process_response')
        return response


class MyMiddleWare1(MiddlewareMixin):
    def process_request(self, request):
        print('process_request1')
        return None

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('process_view1')
        return None

    def process_exception(self, request, exception):
        print('process_exception1')
        return None

    def process_response(self, request, response):
        print('process_response1')
        return response


import time
from django.http import HttpResponse

ip_pools = {}


# d = {'127.0.0.1': ['3', '2:48:34', '3:08:32', "2:48:31"]}

class RequestBlockingMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print(request.META)
        ip = request.META.get('REMOTE_ADDR')

        now_time = time.time()
        # 如果不在字典
        if ip not in ip_pools:
            ip_pools[ip] = [now_time]
            return None

        # 历史访问记录 []
        history = ip_pools.get(ip)

        while history and now_time - history[-1] > 10:
            history.pop()

        if len(history) >= 3:
            return HttpResponse('对不起访问频率过快%s秒' % int(10 - (now_time - history[-1])))
        else:
            history.insert(0, now_time)
