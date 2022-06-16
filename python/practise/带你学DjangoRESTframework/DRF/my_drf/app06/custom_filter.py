from django_filters import rest_framework as filters
from .models import Game


class GameFilter(filters.FilterSet):
    min_status = filters.NumberFilter(field_name='status', lookup_expr='gte')
    max_status = filters.NumberFilter(field_name='status', lookup_expr='lte')
    # 根据名字过滤忽略大小写
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Game
        fields = ('min_status', 'max_status')  # 允许精准查询的字段
        search_fields = ('name',)  # 允许模糊查询的字段
