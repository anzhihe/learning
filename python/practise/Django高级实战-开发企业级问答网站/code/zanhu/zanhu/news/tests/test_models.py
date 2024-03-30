#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from test_plus.test import TestCase

from zanhu.news.models import News


class NewsModelsTest(TestCase):
    def setUp(self):
        self.user = self.make_user("user01")
        self.other_user = self.make_user("user02")
        self.first_news = News.objects.create(
            user=self.user,
            content="第一条动态")
        self.second_news = News.objects.create(
            user=self.user,
            content="第二条动态"
        )
        self.third_news = News.objects.create(
            user=self.other_user,
            content="评论第一条动态",
            reply=True,
            parent=self.first_news
        )

    def test__str__(self):
        self.assertEqual(self.first_news.__str__(), "第一条动态")

    def test_reply_this(self):
        """测试回复功能"""
        initial_count = News.objects.count()
        self.first_news.reply_this(self.other_user, "A second answer.")
        assert News.objects.count() == initial_count + 1
        assert self.first_news.comment_count() == 2
        assert self.third_news in self.first_news.get_thread()

    def test_switch_like(self):
        """测试点赞和取消赞的功能"""
        self.first_news.switch_like(self.user)
        assert self.first_news.count_likers() == 1
        assert self.user in self.first_news.get_likers()
