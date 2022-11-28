from django.shortcuts import redirect, reverse
from django.utils.deprecation import MiddlewareMixin
# 引入setting文件
from django.conf import settings
from django.http import HttpResponse

class Auth_Md(MiddlewareMixin):

    def process_request(self, request):
        # 获取当前请求的url
        current_url = request.path_info
        # 判断是否在白名单中
        for item in settings.UNAUTH_WHITE_URL:
            if item == current_url:
                return None

        # 获取session信息
        obj_user = request.session.get('user')
        # 判断是否存在
        if obj_user:
            request.user = obj_user
        else:
            return redirect(reverse('login'))


        # ======================== 获取当前session中存储的permisson_list,判断当前的请求url是否在permisson_list中==========

        # 1. 在session中获取
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        # 2. 遍历
        for item in permission_list:
            # 如果请求的URL和permission_list中某一个url完全匹配，直接放行
            if current_url == item:
                return None

            # 如果以item开头匹配也放行
            if current_url.startswith(item):
                return None

        # 没有匹配的，显示无权访问
        return HttpResponse('您无权访问当前页面！')
