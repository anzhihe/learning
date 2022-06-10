from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse
import time


def send(request):
    # 耗时的操作

    time.sleep(10)
    res = send_mail('元旦放假已通知',
                    '元旦放假一天',
                    '18622881126@163.com',
                    ['18622881126@163.com'],
                    fail_silently=False)
    # 值1：邮件标题
    # 值2：邮件内容
    # 值3：发件人
    # 值4：收件人
    # 值5：如果失败，是否抛出错误

    '''
    celery  处理耗时操作和定时任务
    '''
    if res == 1:
        return HttpResponse('邮件发送成功')
    else:
        return HttpResponse('邮件发送失败')

    ###  发送多封
    # message1 = ('元旦放假已通知',
    #             '元旦放假一天',
    #             '18622881126@163.com',
    #             ['496155678@qq.com', '18622881126@qq.com'])
    #
    # message2 = ('元旦放假已通知？',
    #             '元旦放假一天',
    #             '18622881126@163.com',
    #             ['496155678@qq.com', '496155678@qq.com'])
    # res = send_mass_mail((message1, message2))
    # if res == 2:
    #     return HttpResponse('多封邮件发送成功')
    # else:
    #     return HttpResponse('多封邮件发送失败')
