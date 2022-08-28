from django.shortcuts import redirect, reverse
from django.utils.deprecation import MiddlewareMixin
# 引入setting文件
from django.conf import settings

class Auth_Md(MiddlewareMixin):

    def process_request(self, request):
        # 获取当前请求的url
        current_url = request.path_info
        # 判断是否在白名单中
        for item in settings.WHITE_URL_LIST:
            if item == current_url:
                return None

        # 获取session信息
        obj_user = request.session.get('user')
        # 判断是否存在
        if obj_user:
            request.user = obj_user
        else:
            return redirect(reverse('login'))