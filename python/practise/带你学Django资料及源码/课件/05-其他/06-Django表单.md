## 表单

一般我们在前端会手动写一个表单像前端传递数据

```
<form action="/login/" method="post">
    <input type="text" name="name" >
    <input type="submit" value="OK">
</form>
```

我们可以用Django的表单类来简化我们的表单书写,在应用下新建一个forms文件。

```
from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)

```

## 编写视图

```python
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # 判断数据是否合法
        if form.is_valid():
            # 处理业务
            name = form.cleaned_data['name']
            return HttpResponse('登录成功')

    # 如果是GET方法，返回一个空的表单
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

```

## 编写模板

```html
<form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>
```

## 效果如下

![](http://tp.jikedaohang.com/20191215144933_ZHr6kh_Screenshot.jpeg)

## 表单类型

- BooleanField
- CharField
- ChoiceField
- TypedChoiceField
- DateField
- DateTimeField
- DecimalField
- DurationField
- EmailField
- FileField
- FilePathField
- FloatField
- ImageField
- IntegerField
- GenericIPAddressField
- MultipleChoiceField
- TypedMultipleChoiceField
- NullBooleanField
- RegexField
- SlugField
- TimeField
- URLField
- UUIDField
- ComboField
- MultiValueField
- SplitDateTimeField
- ModelChoiceField
- ModelMultipleChoiceField

# 高级写法

Django表单提供了一些验证方法，如果不能满足，我们还可以自定义。



## 编写表单

```python
from django import forms
from django.core.exceptions import ValidationError
import re


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')r
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class LoginForm(forms.Form):
    user = forms.CharField(required=True, error_messages={'required': '用户名不能为空.'})
    pwd = forms.CharField(required=True,
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"}, widget=forms.PasswordInput())

    pwd2 = forms.CharField(required=True,
                           min_length=6,
                           max_length=10,
                           error_messages={'required': '密码不能为空.', 'min_length': "至少6位"},
                           widget=forms.PasswordInput(attrs={'class': 'pwd pwd1'}))

    num = forms.IntegerField(error_messages={'required': '数字不能空.', 'invalid': '必须输入数字'})

    phone = forms.CharField(validators=[mobile_validate, ], )

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if user == '123456':
            raise forms.ValidationError('用户名是我的!')

        return user

    def clean(self):
        cleaned_data = self.cleaned_data
        pwd = cleaned_data['pwd']

        pwd2 = cleaned_data['pwd2']
        if pwd != pwd2:
            raise forms.ValidationError('二次输入密码不匹配')
        return cleaned_data  # 注意此处一定要return clean_data,否则会报错

```

### 验证流程

![](https://tva1.sinaimg.cn/large/006tNbRwly1ga91h6helsj30c90b00t2.jpg)

```
函数full_clean()依次调用每个field的clean()函数，该函数针对field的max_length，unique等约束进行验证，如果验证成功则返回值，否则抛出ValidationError错误。如果有值返回，则放入form的cleaned_data字典中。

如果每个field的内置clean()函数没有抛出ValidationError错误，则调用以clean_开头，以field名字结尾的自定义field验证函数。验证成功和失败的处理方式同步骤1。

最后，调用form的clean()函数——注意，这里是form的clean(),而不是field的clean()——如果clean没有错误，那么它将返回cleaned_data字典。

如果到这一步没有ValidationError抛出，那么cleaned_data字典就填满了有效数据。否则cleaned_data不存在，form的另外一个字典errors填上验证错误。在template中，每个field获取自己错误的方式是：{{ form.username.errors }}。

最后，如果有错误is_valid()返回False，否则返回True。

注意一点:自定义验证机制时:clean()和clean_&()的最后必须返回验证完毕或修改后的值.
```



### 编写视图

```python

def login(request):
    if request.POST:
        objPost = LoginForm(request.POST)
        ret = objPost.is_valid()
        if ret:
            print(objPost.clean())
        else:
            from django.forms.utils import ErrorDict
            print(objPost.non_field_errors())

            pass
        return render(request, 'login.html', {'obj1': objPost})
    else:
        objGet = LoginForm()
        return render(request, 'login.html', {'obj1': objGet})
```

编写模板

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style>
        .error_msg{
            color: red;
        }
    </style>
</head>
<body>
    <form action="/login/" method="POST">
        <div>用户名:
            {{ obj1.user }}
            {%  if obj1.errors.user %}
                <span class="error_msg">{{ obj1.errors.user.0 }}</span>
            {% endif %}
        </div>
        <div>密码:
            {{ obj1.pwd }}
            {%  if obj1.errors.pwd %}
                <span class="error_msg">{{ obj1.errors.pwd.0 }}</span>
            {% endif %}
        </div>
        <div>确认密码:
            {{ obj1.pwd2 }}
            {%  if obj1.errors.pwd2 %}
                <span class="error_msg">{{ obj1.errors.pwd2.0 }}</span>
            {% endif %}
        </div>
        <div>数字:
            {{ obj1.num }}
            {%  if obj1.errors.num %}
                <span class="error_msg">{{ obj1.errors.num.0 }}</span>
            {% endif %}
        </div>
        <div>电话:
            {{ obj1.phone }}
            {%  if obj1.errors.phone %}
                <span class="error_msg">{{ obj1.errors.phone.0 }}</span>
            {% endif %}
        </div>
        <div>
            {%  if obj1.non_field_errors %}
                {% for item in obj1.non_field_errors %}
                    <span class="error_msg">{{ item }}</span>
                {% endfor %}
            {% endif %}
        </div>
        <input type="submit" value="提交"/>

    </form>


</body>
</html>
```

> 1. 函数full_clean()依次调用每个field的clean()函数，该函数针对field的max_length，unique等约束进行验证，如果验证成功则返回值，否则抛出ValidationError错误。如果有值返回，则放入form的cleaned_data字典中。
> 2. 如果每个field的内置clean()函数没有抛出ValidationError错误，则调用以clean_开头，以field名字结尾的自定义field验证函数。验证成功和失败的处理方式同步骤1。
> 3. 最后，调用form的clean()函数——注意，这里是form的clean(),而不是field的clean()——如果clean没有错误，那么它将返回cleaned_data字典。
> 4. 如果到这一步没有ValidationError抛出，那么cleaned_data字典就填满了有效数据。否则cleaned_data不存在，form的另外一个字典errors填上验证错误。在template中，每个field获取自己错误的方式是：{{ form.username.errors }}。
> 5. 最后，如果有错误is_valid()返回False，否则返回True。
>
> 　　**注意一点:自定义验证机制时:clean()和clean_<field>&()的最后必须返回验证完毕或修改后的值.**

### 手动渲染表单字段

直接`{{ form }}`虽然好，啥都不用操心，但是往往并不是你想要的，比如你要使用CSS和JS，比如你要引入Bootstarps框架，这些都需要对表单内的input元素进行额外控制，那怎么办呢？手动渲染字段就可以了。

可以通过`{{ form.name_of_field }}`获取每一个字段，然后分别渲染，如下例所示：

```python
<div class="fieldWrapper">
    {{ form.subject.errors }}
    {{ form.subject.label_tag }}
    {{ form.subject }}
</div>
```

