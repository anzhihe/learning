from django import forms
from django.core.exceptions import ValidationError
import re


class LoginForm(forms.Form):
    phone = forms.CharField(label='手机号',
                            required=True, min_length=11, max_length=15,
                            error_messages={"required": '此字段必填', 'min_length': '手机号必须是11位'})


def check_phone(phone):
    result = re.match(r'1[3456789]\d{9}$', phone)
    if result:
        return True
    else:
        raise ValidationError("手机号不合法")


class RegisterForm(forms.Form):
    user = forms.CharField(label='用户名', required=True, min_length=6, max_length=15,
                           error_messages={"required": '此字段必填', 'min_length': '用户名是6位'})

    phone = forms.CharField(label='手机号',
                            required=True, validators=[check_phone, ],
                            error_messages={"required": '此字段必填'})

    pwd = forms.CharField(label='密码', required=True, min_length=6, max_length=16,
                          error_messages={"required": '此字段必填', 'min_length': '最小6位'},
                          widget=forms.PasswordInput(attrs={'class': 'pwd'}))

    pwd1 = forms.CharField(label='重复密码', required=True, min_length=6, max_length=16,
                           error_messages={"required": '此字段必填', 'min_length': '最小6位'},
                           widget=forms.PasswordInput(attrs={'class': 'pwd pwd1'}))

    # clean_字段名 这个方法自己会调用
    def clean_user(self):
        user = self.cleaned_data.get('user')

        if user == '123456':
            raise ValidationError('用户名不能是123456')
        return user

    # 最后调用
    def clean(self):
        cleaned_data = self.cleaned_data
        pwd1 = cleaned_data.get('pwd1')
        pwd = cleaned_data.get('pwd')

        if pwd1 != pwd:
            raise ValidationError('两次密码不一样')

        return cleaned_data
