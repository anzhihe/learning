from django import template
from django.conf import settings


# 实例化一个模板库
register = template.Library()
@register.inclusion_tag('rbac/menu.html')
def menu(reqeust):
    """生成菜单"""
    menu_dict = reqeust.session.get(settings.MENU_SESSION_KEY)
    # 返回
    return {'menu_dict': menu_dict}