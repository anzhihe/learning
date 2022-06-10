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

    # 验证码字段
    captcha = CaptchaField(required=True, error_messages={'invalid': '验证码错误'})
