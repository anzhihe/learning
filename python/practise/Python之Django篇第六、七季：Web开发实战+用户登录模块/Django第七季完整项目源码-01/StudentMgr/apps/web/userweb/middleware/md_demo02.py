from django.utils.deprecation import MiddlewareMixin


class MiddleWare02(MiddlewareMixin):

    def process_request(self, request):
        # request方法--- 在匹配URL路由前自动运行
        print("demo02_request")

    def process_response(self, request, response):
        print("demo02_response")
        return response