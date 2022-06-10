from django import forms
from django.core.exceptions import ValidationError
import re
from .models import BlogUser


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', required=True, min_length=6, max_length=15,
                               error_messages={"required": '此字段必填', 'min_length': '用户名是6位'},
                               widget=forms.TextInput(attrs={"class": 'form-control', "placeholder": "请输入用户名"}))

    pwd = forms.CharField(label='密码', required=True, min_length=6, max_length=16,
                          error_messages={"required": '此字段必填', 'min_length': '最小6位'},
                          widget=forms.PasswordInput(attrs={"class": 'form-control', "placeholder": "请输入密码"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        count = BlogUser.objects.filter(username=username).count()
        if not count:
            raise ValidationError('用户不存在')

        return username


def check_phone(phone):
    result = re.match(r'1[3456789]\d{9}$', phone)
    if result:
        return True
    else:
        raise ValidationError("手机号不合法")


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', required=True, min_length=6, max_length=15,
                               error_messages={"required": '此字段必填', 'min_length': '用户名是6位'},
                               widget=forms.TextInput(attrs={"class": 'form-control', "placeholder": "请输入用户名"}))

    phone = forms.CharField(label='手机号', max_length=11, min_length=11,
                            required=True, validators=[check_phone, ],
                            error_messages={"required": '此字段必填'},
                            widget=forms.TextInput(attrs={"class": 'form-control', "placeholder": "请输入手机号"}))

    pwd = forms.CharField(label='密码', required=True, min_length=6, max_length=16,
                          error_messages={"required": '此字段必填', 'min_length': '最小6位'},
                          widget=forms.PasswordInput(attrs={"class": 'form-control', "placeholder": "请输入密码"}))

    pwd1 = forms.CharField(label='重复密码', required=True, min_length=6, max_length=16,
                           error_messages={"required": '此字段必填', 'min_length': '最小6位'},
                           widget=forms.PasswordInput(attrs={"class": 'form-control', "placeholder": "请再次输入密码"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        count = BlogUser.objects.filter(username=username).count()
        if count:
            raise ValidationError('用户名重复')

        return username

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        count = BlogUser.objects.filter(phone=phone).count()
        if count:
            raise ValidationError('手机号以被注册')

        return phone

    # 最后调用
    def clean(self):
        cleaned_data = self.cleaned_data
        pwd1 = cleaned_data.get('pwd1')
        pwd = cleaned_data.get('pwd')

        if pwd1 != pwd:
            raise ValidationError('两次密码不一样')

        return cleaned_data
