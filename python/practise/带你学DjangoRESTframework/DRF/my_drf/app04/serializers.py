from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        # exclude = ('user',)

        extra_kwargs = {
            "user": {"read_only": True}
        }

    # def validate_name(self, name):
    #     if name == '吃鸡10':
    #         raise serializers.ValidationError('名字不合法')
    #
    # def validate_desc(self, desc):
    #
    #     if desc == '哈哈':
    #         raise serializers.ValidationError('描述不合法')
    #
    # def validate(self, attrs):
    #     raise serializers.ValidationError('无缘无故异常')
    #     return attrs
