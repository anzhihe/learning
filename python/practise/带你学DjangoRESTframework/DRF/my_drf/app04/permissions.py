from rest_framework import permissions

class IsOwnOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user




'''
这是学jwt的时候加的代码，如果你学到这，先不要加下面注释的代码，谢谢
'''
# from rest_framework.throttling import SimpleRateThrottle
#
# from rest_framework_jwt.authentication import jwt_decode_handler
#
#
# class IsOwnOrReadOnly(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         # if request.method in permissions.SAFE_METHODS:
#         #     return True
#
#         token = request.META.get('HTTP_AUTHORIZATION')[5:]  # token解析出来
#         token_user = jwt_decode_handler(token)  # 解析出来
#         if token_user:
#             return obj.user.id == token_user.get('user_id')  # 证明 当前jwt验证的用户就是数据创建者
#         return False
