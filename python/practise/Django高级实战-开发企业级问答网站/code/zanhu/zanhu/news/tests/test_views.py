#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from django.test import Client
from django.urls import reverse
from test_plus.test import TestCase

from zanhu.news.models import News


class NewsViewsTest(TestCase):

    def setUp(self):
        self.user = self.make_user("user01")
        self.other_user = self.make_user("user02")

        self.client = Client()
        self.other_client = Client()

        self.client.login(username="user01", password="password")
        self.other_client.login(username="user02", password="password")

        self.first_news = News.objects.create(
            user=self.user,
            content="第一条动态"
        )

        self.second_news = News.objects.create(
            user=self.user,
            content="第二条动态"
        )

        self.third_news = News.objects.create(
            user=self.other_user,
            content="第一条动态的评论",
            reply=True,
            parent=self.first_news
        )

    def test_news_list(self):
        """测试动态列表页功能"""
        response = self.client.get(reverse("news:list"))
        assert response.status_code == 200
        assert self.first_news in response.context["news_list"]
        assert self.second_news in response.context["news_list"]
        assert self.third_news not in response.context["news_list"]

    def test_delete_news(self):
        """删除动态"""
        initial_count = News.objects.count()
        response = self.client.post(reverse("news:delete_news", kwargs={"pk": self.second_news.pk}))  # 删除第二条动态
        assert response.status_code == 302
        assert News.objects.count() == initial_count - 1

    def test_post_news(self):
        """发送动态"""
        initial_count = News.objects.count()
        response = self.client.post(
            reverse("news:post_news"), {"post": "我是慕男神"},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"  # 表示发送Ajax Request请求
        )
        assert response.status_code == 200
        assert News.objects.count() == initial_count + 1

    def test_like_news(self):
        """点赞"""
        response = self.client.post(
            reverse("news:like_post"), {"news": self.first_news.pk},  # 让user01给自己的动态点赞
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        assert response.status_code == 200
        assert self.first_news.count_likers() == 1  # 点赞后数量为1
        assert self.user in self.first_news.get_likers()  # user01在get_liker()获取的点赞用户中
        assert response.json()["likes"] == 1

    def test_get_thread(self):
        """获取动态的评论"""
        response = self.client.get(
            reverse("news:get_thread"), {"news": self.first_news.pk},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        assert response.status_code == 200
        assert response.json()["uuid"] == str(self.first_news.pk)
        assert "第一条动态" in response.json()["news"]
        assert "第一条动态的评论" in response.json()["thread"]

    def test_post_comments(self):
        """发表评论"""
        response = self.client.post(
            reverse("news:post_comments"),
            {
                "reply": "第二条动态的评论",
                "parent": self.second_news.pk
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        assert response.status_code == 200
        assert response.json()["comments"] == 1
