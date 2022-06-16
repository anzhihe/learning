### Django RESTFUL提供的认证

- BasicAuthentication：此身份验证方案使用[HTTP基本身份验证](https://tools.ietf.org/html/rfc2617)，根据用户的用户名和密码进行签名。基本身份验证通常仅适用于测试。
- TokenAuthentication：    此身份验证方案使用基于令牌的简单HTTP身份验证方案。令牌认证适用于客户端 - 服务器设置，例如本机桌面和移动客户端。
- SessionAuthentication：　此身份验证方案使用Django的默认会话后端进行身份验证。会话身份验证适用于与您的网站在同一会话上下文中运行的AJAX客户端。
-  RemoteUserAuthentication：此身份验证方案允许您将身份验证委派给Web服务器，该服务器设置`REMOTE_USER` 环境变量。



### BasicAuthentication

![](https://tva1.sinaimg.cn/large/0082zybply1gbx7g8b508j31y20gkdjl.jpg)



Http Basic 是一种比较简单的身份认证方式。 在 Http header 中添加键值对 Authorization:  Basic xxx （xxx 是 username:passowrd base64 值）。而Base64 的解码是非常方便的，如果不使用 [Https](http://geek.csdn.net/news/detail/48765) ，相当于是帐号密码直接暴露在请求中。

```
GET /auth/basic/ HTTP/1.1
Host: xxxxx
Authorization: Basic em1rOjEyMzQ1Ng==
```



### TokenAuthentication

- 配置

```python
# settings.py
INSTALLED_APPS = (
    ...
    'rest_framework.authtoken'
)

# 全局配置
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',  
        'rest_framework.authentication.TokenAuthentication'，
    ),
}

# 局部配置
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication

class XXXX(APIView):
			authentication_classes = [BasicAuthentication,TokenAuthentication,SessionAuthentication]
```

- 路由

```
from rest_framework.authtoken import views
path('api-token-auth/', views.obtain_auth_token)
```

- 传递方式

```
封装到请求头中，已下面的格式
Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
```



![](https://tva1.sinaimg.cn/large/0082zybply1gbx7iztgvsj31hc0eojtf.jpg)

token值在分布式系统中会有问题产生，并且没有过期时间，一旦被窃取，任何人都可以使用



### SessionAuthentication

![](https://tva1.sinaimg.cn/large/0082zybply1gbx97sdo67j31bi0e4410.jpg)





### 自定义验证

- 模型

```
class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)


class UserToken(models.Model):
    user = models.OneToOneField('User', models.CASCADE)
    token = models.CharField(max_length=64)

```

- 视图

```python
from rest_framework.views import APIView
from .models import User, UserToken
import hashlib
import time
from django.http import JsonResponse


def get_md5(user):
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


class AuthView(APIView):
    def post(self, request):
        ret = {'code': 1, 'msg': None, 'data': {}}
        user = request._request.POST.get('username')
        pwd = request._request.POST.get('password')
        obj = User.objects.filter(username=user, password=pwd).first()
        if not obj:
            ret['code'] = -1
            ret['msg'] = "用户名或密码错误"
        token = get_md5(user)
        UserToken.objects.update_or_create(user=obj, defaults={'token': token})
        ret['token'] = token
        return JsonResponse(ret)
```

- 实现类

```python
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class Authtication(BaseAuthentication):
    def authenticate(self, request):
      '''
      header key必须大写，前缀必须是"HTTP",后面如果连接符是横线“-”，要改成下划线“_”。例如你的header的key为api_auth，那在Django中应该使用request.META.get("HTTP_API_AUTH")来获取请求头的数据。
      '''
				token = request.META.get('HTTP_TOKEN')  # META 是请求头
        obj = UserToken.objects.filter(token=token).first()
        if not obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (obj.user, obj)
```

- 自定义权限

```

from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user:
            return False

        return True

```



### JWT验证

使用django-rest-framework开发api并使用json web token进行身份验证,使用django-rest-framework-jwt这个库来帮助我们简单的使用jwt进行身份验证。

### 安装

```
pip install djangorestframework-jwt
```

### 注册

```
INSTALLED_APPS = [
    ''''''
    'rest_framework',
    'rest_framework.authtoken',
]

```

### 配置

```
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 配置验证方式为Token验证
    ),
}
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Token 过期时间为一周
    'JWT_AUTH_HEADER_PREFIX': 'JWT',  # Token的头为：JWT adashkjdhaskjhd21312312
    'JWT_ALLOW_REFRESH': False,
}
```

### 路由

```
from rest_framework_jwt.views import obtain_jwt_token
path('api-token-auth/', obtain_jwt_token),
```

![](https://tva1.sinaimg.cn/large/006tNbRwly1gavc172whoj31hq0ouae9.jpg)

默认的返回值仅有token，通过修改该视图的返回值可以完成我们的需求。在应用中新建一个utils.py 文件：

```python
def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'token': token,
        'id': user.id,
        'username': user.username,
    }

```

```
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Token 过期时间为一周
    'JWT_ALLOW_REFRESH': False,
    'JWT_AUTH_HEADER_PREFIX': 'JWT',  # Token的头为：JWT adashkjdhaskjhd21312312
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'app06.utils.jwt_response_payload_handler',
}
```

![](https://tva1.sinaimg.cn/large/006tNbRwly1gavc3tccz9j31hy0rmq7v.jpg)

我们可以将JWT保存在cookie中，也可以保存在浏览器的本地存储里，我们保存在浏览器本地存储中,下次使用的时候带上即可。







### jwt的权限验证

![](https://tva1.sinaimg.cn/large/006tNbRwly1gavdf8n1nuj31i40u00xj.jpg)

```
from rest_framework_jwt.authentication import jwt_decode_handler
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        token = request.META.get('HTTP_AUTHORIZATION')[5:]
        token_user = jwt_decode_handler(token)
        if token_user:
            return obj.user.id == token_user.get('user_id')
        return False

```



### JWT优缺点

#### 优点

- 无状态
- 避免csrf
- 适合移动端

#### 缺点

- 注销登录后Token时效问题

