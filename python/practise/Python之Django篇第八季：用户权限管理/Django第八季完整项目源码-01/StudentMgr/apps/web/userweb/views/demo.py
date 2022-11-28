# ---- 引入django-redis ======
from django_redis import get_redis_connection
from django.shortcuts import HttpResponse

# =----- 导入django自带的邮件模块 ========
from django.core.mail import send_mail


def set_redis(request):
    """向redis数据库中写入数据"""
    # 实例化一个连接池的对象
    redis_obj = get_redis_connection("default")
    # 设置
    redis_obj.set('name', 'alice', 10)
    # 返回
    return HttpResponse("redis设置成功")


def get_redis(request):
    # 实例化一个连接池的对象
    redis_obj = get_redis_connection("default")
    # 设置(取到的值是Byte类型)
    rec = redis_obj.get('name')
    # 判断是否有值
    if rec:
        return HttpResponse("name:" + rec.decode('utf-8'))
    else:
        # 返回
        return HttpResponse("redis上的值过期")


def send_email(request):
    """发送邮件"""

    res = send_mail("重置密码","验证码为：1234","651205558@qq.com",['13482034096@163.com'])
    if res == 1:
        return HttpResponse("邮件发送成功！")
    else:
        return HttpResponse("邮件发送失败！")