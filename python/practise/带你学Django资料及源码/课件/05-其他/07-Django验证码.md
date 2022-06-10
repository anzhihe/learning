### 验证码

验证码主要的作用是为了验证作用，现在验证码也有很多类型，比如滑动、点击、倒立点击特别多，这些都是为了加强网站的安全。

### 安装

```
pip install django-simple-captcha
```

### 配置

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha'
]
```

### 配置路由

```

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('captcha/', include('captcha.urls')),
              ] 

```

### 创建表单

在应用下创建forms.py文件，内容为

```
from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from django.forms import widgets
import re


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class ContactForm(forms.Form):
    name = forms.CharField(required=True, error_messages={'required': '姓名不能为空.'},
                           widget=widgets.Input(attrs={"class": 'contactFormText', 'placeholder': '请填写姓名'}))
    phone = forms.CharField(validators=[mobile_validate],
                            widget=widgets.TextInput(attrs={"class": 'contactFormText', 'placeholder': '请填写手机号码'}))
    captcha = CaptchaField(required=True, error_messages={'invalid': '验证码错误'})

```

### 迁移文件

```
python manage.py miragte
```



### 编写视图

```
def contact(request):
    contactform = ContactForm()
    if request.method == 'GET':
        return render(request, 'contact.html', {'contactform': contactform})
    else:
        obj = ContactForm(request.POST)
        if obj.is_valid():
            data = obj.clean()
            return HttpResponse('OK')
        else:
            return render(request, 'contact.html', {'contactform': contactform, 'obj': obj})


```

### 编写模板

```html
<form id="contactForm" action="/contact/" method="post">
                        {% csrf_token %}
                        <h3>在线表单</h3>
                        <div class="contactFormItem">
                            <div class="contactFormField">
                                <span class="contactFormLabel">姓名</span>
                                {{ contactform.name }}
                                {% if obj.errors.name %}
                                    <span class="error_msg">{{ obj.errors.name }}</span>
                                {% endif %}
                            </div>
                        </div>
                        <div class="contactFormItem">
                            <div class="contactFormField">
                                <span class="contactFormLabel">手机</span>
                                {{ contactform.phone }}
                            </div>
                            {% if obj.errors.phone %}
                                <span class="error_msg">{{ obj.errors.phone }}</span>
                            {% endif %}
                        </div>

                        <div class="contactFormItem">
                            {{ contactform.captcha }}

                        </div>
                        {% if obj.errors.captcha %}
                            <span class="error_msg">{{ obj.errors.captcha }}</span>
                        {% endif %}
                        <div class="contactFormSubmit">
                            <input type="submit" value="提交" class="contactFormSubmitBtn">
                        </div>
                    </form>
```

### 刷新验证码

```js
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
<script>
    $('.captcha').click(function () {
        $.getJSON("/captcha/refresh/", function (result) {
            $('.captcha').attr('src', result['image_url']);
            $('#id_captcha_0').val(result['key'])
        });

    });
</script>
```

