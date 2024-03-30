#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from functools import wraps

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest
from django.views.generic import View


def ajax_required(f):
    """验证是否为AJAX请求"""

    @wraps(f)
    def wrap(request, *args, **kwargs):
        #  request.is_ajax() 方法判断是否是 ajax 请求
        # 参考:https://code.ziqiangxuetang.com/django/django-ajax.html
        if not request.is_ajax():
            return HttpResponseBadRequest("不是AJAX请求！")
        return f(request, *args, **kwargs)

    return wrap


class AuthorRequiredMixin(View):
    """
    验证是否为原作者，用于状态删除、文章编辑；
    个人中心模块中更新信息不要验证是否为原作者，因为UserUpdateView返回的是当前登录用户的form
    """

    def dispatch(self, request, *args, **kwargs):
        # 状态和文章实例有user属性
        if self.get_object().user.username != self.request.user.username:
            raise PermissionDenied

        return super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)
