from django.shortcuts import render
from .models import *
from django.views.generic import View
from django.http import HttpResponse
from pure_pagination.paginator import Paginator, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, reverse
from .forms import LoginForm, RegisterForm


# Create your views here.

# 类视图
class BaseView(View):
    def get(self, request, *arg, **kwargs):
        # 找到最新评论
        comments = Comment.objects.filter(is_delete=False).all()[:10]
        # [3,2,1]
        # [1,2,1]

        # [1,2]

        art_ids = []  # [1,2]
        new_comments = []  # 装过滤后的评论
        for comment in comments:
            if comment.article.id not in art_ids:
                art_ids.append(comment.article.id)
                new_comments.append(comment)

        return new_comments


class IndexView(BaseView):

    def get(self, request, *arg, **kwargs):
        new_comments = super().get(request, *arg, **kwargs)

        banners = Banner.objects.filter(is_delete=False).all()
        top_articles = Article.objects.filter(is_delete=False, is_top=True).all()
        '''
        todo objects 可以自定义
        '''
        categorys = Category.objects.filter(is_delete=False).all()
        all_articles = Article.objects.filter(is_delete=False).all()[:10]
        fks = FriendLink.objects.filter(is_delete=False).all()

        count = Article.objects.count()
        return render(request, 'index.html', locals())


# 列表页视图
class ListView(BaseView):
    def get(self, request, *arg, **kwargs):
        new_comments = super().get(request, *arg, **kwargs)
        all_articles = Article.objects.filter(is_delete=False).all()
        tags = Tag.objects.filter(is_delete=False).all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_articles, per_page=1, request=request)

        # 注意点跟前端遍历一样
        all_articles = p.page(page)

        return render(request, 'list.html', locals())


# 详情页
class DetailView(BaseView):
    def get(self, request, *arg, **kwargs):
        count = Article.objects.count()
        id = kwargs.get('id')
        new_comments = super().get(request, *arg, **kwargs)
        try:
            article = Article.objects.get(id=id)
            article.vnum = article.vnum + 1
            article.save()
            # 先找到这篇文章的标签
            tags = article.tag.all()
            # ["游戏","手游"]

            recommend_articles = []  # [[],[],[]]
            for tag in tags:
                recommend_articles.extend(tag.article_set.all())  # 为什么不用append
            recommend_articles = list(set(recommend_articles))[:10]  # 去重

            comments = article.comment_set.all()
            return render(request, 'show.html', locals())
        except Article.DoesNotExist:
            return render(request, '404.html')


# 分类
class CategoryView(BaseView):
    def get(self, request, *arg, **kwargs):
        id = kwargs.get('id')
        new_comments = super().get(request, *arg, **kwargs)
        tags = Tag.objects.filter(is_delete=False).all()
        try:
            category = Category.objects.get(id=id)
            all_articles = category.article_set.all()
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_articles, per_page=1, request=request)

            # 注意点跟前端遍历一样
            all_articles = p.page(page)

            return render(request, 'list.html', locals())
        except Category.DoesNotExist:
            return render(request, '404.html')


# 标签
class TagView(BaseView):
    def get(self, request, *arg, **kwargs):
        id = kwargs.get('id')
        new_comments = super().get(request, *arg, **kwargs)
        tags = Tag.objects.filter(is_delete=False).all()
        try:
            tag = Tag.objects.get(id=id)
            all_articles = tag.article_set.all()
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_articles, per_page=1, request=request)

            # 注意点跟前端遍历一样
            all_articles = p.page(page)

            return render(request, 'list.html', locals())
        except Category.DoesNotExist:
            return render(request, '404.html')


class SearchView(BaseView):
    def get(self, request, *arg, **kwargs):
        kw = request.GET.get('kw')
        # distinct 去重
        all_articles = Article.objects.filter(Q(title__icontains=kw) | Q(content__icontains=kw)).distinct()
        tags = Tag.objects.filter(is_delete=False).all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_articles, per_page=1, request=request)

        # 注意点跟前端遍历一样
        all_articles = p.page(page)
        return render(request, 'list.html', locals())


class LoginView(View):
    def get(self, request, *args, **kwargs):
        login_form = LoginForm()

        return render(request, 'login.html', locals())

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():  # 验证成功

            username = login_form.cleaned_data.get('username')
            pwd = login_form.cleaned_data.get('pwd')

            user = authenticate(request=request, username=username, password=pwd)  # 验证有这个有用户
            if user:
                login(request, user)  # django 内置的登录函数
            return redirect(reverse('blog:index'))
        else:
            return render(request, 'login.html', locals())


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        reg_form = RegisterForm()
        return render(request, 'register.html', locals())

    def post(self, request, *args, **kwargs):
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():  # 验证成功
            phone = reg_form.cleaned_data.get('phone')
            username = reg_form.cleaned_data.get('username')
            pwd = reg_form.cleaned_data.get('pwd')
            BlogUser.objects.create_user(phone=phone, username=username, password=pwd)
            return redirect(reverse('blog:login'))
        else:
            return render(request, 'register.html', locals())


def log_out(request):
    logout(request)  # django 内置的登出函数
    return redirect(reverse("blog:index"))


@require_http_methods(['POST'])
@login_required
def comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        id = request.POST.get('id')  # 评论文章id
        if not content:
            return redirect(reverse('blog:detail', kwargs={"id": id}))
        user = request.user
        try:
            article = Article.objects.get(id=id)

            Comment.objects.create(content=content, article=article, users=user)
            return redirect(reverse('blog:detail', kwargs={"id": id}))
        except Exception as e:
            return render(request, '404.html')
