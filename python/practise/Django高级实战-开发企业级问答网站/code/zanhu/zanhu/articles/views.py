#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from django_comments.signals import comment_was_posted

from zanhu.articles.models import Article
from zanhu.articles.forms import ArticleForm
from zanhu.helpers import AuthorRequiredMixin
from zanhu.notifications.views import notification_handler


class ArticlesListView(LoginRequiredMixin, ListView):
    """已发布的文章列表"""
    model = Article
    paginate_by = 20
    context_object_name = "articles"
    template_name = "articles/article_list.html"  # 可省略

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        context['popular_tags'] = Article.objects.get_counted_tags()
        return context

    def get_queryset(self, **kwargs):
        return Article.objects.get_published()


class DraftsListView(ArticlesListView):
    """草稿箱文章列表"""

    def get_queryset(self, **kwargs):
        # 当前用户的草稿
        return Article.objects.filter(user=self.request.user).get_drafts()


@method_decorator(cache_page(60 * 60), name='get')  # get是小写
class CreateArticleView(LoginRequiredMixin, CreateView):
    """创建文章"""
    model = Article
    message = "您的文章已创建成功！"  # Django框架中的消息机制
    form_class = ArticleForm
    template_name = 'articles/article_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateArticleView, self).form_valid(form)

    def get_success_url(self):
        """创建成功后跳转"""
        messages.success(self.request, self.message)  # 消息传递给下一次请求
        return reverse('articles:list')


class DetailArticleView(LoginRequiredMixin, DetailView):
    """文章详情"""
    model = Article
    template_name = 'articles/article_detail.html'

    def get_queryset(self):
        return Article.objects.select_related('user').filter(slug=self.kwargs['slug'])


class EditArticleView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):  # 注意类的继承顺序
    """编辑文章"""
    model = Article
    message = "您的文章编辑成功！"
    form_class = ArticleForm
    template_name = 'articles/article_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EditArticleView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse('articles:list')


def notify_comment(**kwargs):
    """文章有评论时通知作者"""
    actor = kwargs['request'].user
    obj = kwargs['comment'].content_object

    notification_handler(actor, obj.user, 'C', obj)


comment_was_posted.connect(receiver=notify_comment)
