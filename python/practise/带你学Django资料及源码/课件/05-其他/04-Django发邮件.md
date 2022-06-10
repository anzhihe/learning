### 发送邮件 

注册163邮箱，登录后设置。

![](https://tva1.sinaimg.cn/large/006tNbRwly1ga83gloi1rj31ny0u0n4j.jpg)



测试授权码是abc1234567

### 设置配置

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = '18622881126@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'abc1234567'
# 设置是否启用安全链接
EMAIL_USER_TLS = True

```
### 编写视图
```python
from django.shortcuts import render
from pure_pagination import Paginator, PageNotAnInteger
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse



def send(request):

    res = send_mail('元旦放假已通知',
                    '元旦放假一天',
                    '18622881126@163.com',
                    ['496155678@qq.com'],
                    fail_silently=False)
    # 值1：邮件标题   
    # 值2：邮件主人  
    # 值3：发件人  
    # 值4：收件人  
    # 值5：如果失败，是否抛出错误
    if res == 1:
        return HttpResponse('邮件发送成功')
    else:
        return HttpResponse('邮件发送失败')

```

```python
from django.shortcuts import render
from pure_pagination import Paginator, PageNotAnInteger
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse



def send(request):
    message1 = ('元旦放假已通知',
                '元旦放假一天',
                '18622881126@163.com',
                ['496155678@qq.com', '18622881126@qq.com'])

    message2 = ('元旦放假已通知？',
                '元旦放假一天',
                '18622881126@163.com',
                ['496155678@qq.com', '496155678@qq.com'])
    res = send_mass_mail((message1, message2))
    if res == 2:
        return HttpResponse('多封邮件发送成功')
    else:
        return HttpResponse('多封邮件发送失败')


```



### 路由配置

```python
path('send/',views.send),
```

