from rest_framework import serializers
from .models import User
import re

from collections import OrderedDict


class ChoiceDisplayField(serializers.Field):
    """Custom ChoiceField serializer field."""

    def __init__(self, choices, **kwargs):
        """init."""
        self._choices = OrderedDict(choices)
        super(ChoiceDisplayField, self).__init__(**kwargs)

    # 返回可读性良好的字符串而不是 1，-1 这样的数字
    def to_representation(self, obj):
        """Used while retrieving value for the field."""
        return self._choices[obj]

    def to_internal_value(self, data):
        """Used while storing value for the field."""
        for i in self._choices:
            # 这样无论用户POST上来但是CHOICES的 Key 还是Value 都能被接受
            if i == data or self._choices[i] == data:
                return i
        raise serializers.ValidationError("Acceptable values are {0}.".format(list(self._choices.values())))


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11, min_length=11, required=True, error_messages={"required": "手机号必填"})

    pwd1 = serializers.CharField(write_only=True)

    # gender = serializers.CharField(source='get_gender_display')

    # 支持可读可写
    GENDERS = (
        (1, '男'), (2, "女")
    )
    gender = ChoiceDisplayField(choices=GENDERS)

    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            "pwd": {"write_only": True}
        }

    # def to_representation(self, instance):
    #     representation = super(UserSerializer, self).to_representation(instance)
    #     representation['gender'] = instance.get_gender_display()
    #     return representation

    def validate_phone(self, phone):  # 单独的验证函数
        if not re.match(r'1[3456789]\d{9}', phone):
            raise serializers.ValidationError('手机号不合法')

        if User.objects.filter(phone=phone).all():
            raise serializers.ValidationError('手机号以被注册')

        return phone  # 一定要有返回值

    def validate(self, attrs):

        if attrs.get('pwd1') != attrs.get('pwd'):
            print(attrs.get('pwd1'))
            raise serializers.ValidationError('两次密码不一样')
        attrs.pop('pwd1')  # 验证后 在pop掉
        return attrs
