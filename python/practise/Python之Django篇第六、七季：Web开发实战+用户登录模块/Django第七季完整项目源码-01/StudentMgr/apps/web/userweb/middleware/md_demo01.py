from django.utils.deprecation import MiddlewareMixin


class MiddleWare01(MiddlewareMixin):

    def process_request(self, request):
        # request方法--- 在匹配URL路由前自动运行
        print("demo01_request")


    def process_response(self, request, response):
        print("demo01_response")
        return response