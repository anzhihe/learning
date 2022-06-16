from rest_framework import serializers
from .models import Article, Category, Tag


# # 普通序列化
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100, required=True)
#     vum = serializers.IntegerField(required=True)
#     content = serializers.CharField()
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.vum = validated_data.get('vum', instance.vum)
#         instance.content = validated_data.get('title', instance.content)
#         instance.save()
#         return instance


# 模型序列化
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         # fields = ('id', 'vum', 'content', 'title')
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         # fields = ('id', 'vum', 'content', 'title')
#         fields = '__all__'


# StringRelatedField

# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles')

# PrimaryKeyRelatedField

# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.PrimaryKeyRelatedField(read_only=True)
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles')

# HyperlinkedRelatedField

#
# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.HyperlinkedRelatedField(
#         view_name='app02:category-detail',
#         read_only=True,
#         lookup_field='id'
#
#     )
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.HyperlinkedRelatedField(
#         view_name='app02:article-detail',
#         read_only=True,
#         many=True  # 很重要
#     )
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles')


# SlugRelatedField

# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='name'
#
#     )
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='content',
#         many=True
#
#     )
#
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles')


# HyperlinkedIdentityField

# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.HyperlinkedIdentityField(
#         view_name='app02:category-detail',
#         lookup_field='id'
#     )
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.HyperlinkedIdentityField(
#         view_name='app02:article-detail',
#         many=True,
#     )
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles')


# HyperlinkedModelSerializer

# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#         extra_kwargs = {
#             'url': {'view_name': 'app02:article-detail', 'lookup_field': 'pk'},
#             'category': {'view_name': 'app02:category-detail', 'lookup_field': 'id'},
#         }
#
#
# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles', 'url')
#
#         extra_kwargs = {
#             'url': {'view_name': 'app02:category-detail', 'lookup_field': 'id'},
#             'articles': {'view_name': 'app02:article-detail', 'lookup_field': 'pk'},
#         }


# 序列嵌套
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = ArticleSerializer(many=True)
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles')


# depth
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         depth = 2
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles')
#         depth = 2  # 建议写到2-3
#

# SerializerMethodField

# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     count = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles', 'count')
#
#     def get_count(self, obj):
#         return obj.articles.count()


# # source
#
# class MyCharField(serializers.CharField):
#     def to_representation(self, value):
#         data_list = []
#         for val in value:
#             data_list.append({"title": val.title, "content": val.content})
#         return data_list
#
#
# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.CharField(source='category.name')
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     # arts = serializers.CharField(source='articles.all')
#     arts = MyCharField(source='articles.all')
#
#     # arts = serializers.CharField(source='article_set.all') #如果没有related_name
#
#     '''
#     get_xx_display
#     '''
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'arts')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # depth = 2

    # 决定每个字段的返回值
    def to_representation(self, instance):
        representation = super(ArticleSerializer, self).to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        representation['tags'] = TagSerializer(instance.tags, many=True).data
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = Tag
        fields = '__all__'
