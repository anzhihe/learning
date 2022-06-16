from rest_framework.throttling import SimpleRateThrottle


class VisitThrottling(SimpleRateThrottle):
    scope = '未认证用户'

    def get_cache_key(self, request, view):
        return self.get_ident(request)  # 拿ip当做key


class UserThrottling(SimpleRateThrottle):
    scope = '已认证用户'

    def get_cache_key(self, request, view):
        return request.user  # 当前登录的用户当做key
