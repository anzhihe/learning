from django.template import Library

register = Library()


@register.filter(is_safe=True)
def is_laowang(value):
    return value == '老王'


@register.filter(is_safe=True)
def add_arg(value, arg='我爱你'):
    return value + arg


