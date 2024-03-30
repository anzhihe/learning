#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from django.test import Client
from django.urls import reverse
from test_plus.test import TestCase

from zanhu.notifications.models import Notification


class NotificationsViewsTest(TestCase):

    def setUp(self):
        self.user = self.make_user("user01")
        self.other_user = self.make_user("user02")
        self.client = Client()
        self.other_client = Client()
        self.client.login(username="user01", password="password")
        self.other_client.login(username="user02", password="password")
        # user01赞了user02
        self.first_notification = Notification.objects.create(
            actor=self.user,
            recipient=self.other_user,
            verb="L"
        )
        # user01评论了user02
        self.second_notification = Notification.objects.create(
            actor=self.user,
            recipient=self.other_user,
            verb="C"
        )
        # user02回答了user01
        self.third_notification = Notification.objects.create(
            actor=self.other_user,
            recipient=self.user,
            verb="A"
        )

    def test_notification_list(self):
        response = self.client.get(reverse("notifications:unread"))
        assert response.status_code == 200
        assert self.third_notification in response.context["notification_list"]

    def test_mark_all_as_read(self):
        """user01收到的所有通知标为已读"""
        response = self.client.get(reverse("notifications:mark_all_read"), follow=True)
        assert '/notifications/' in str(response.context["request"])
        assert Notification.objects.unread().count() == 2

    def test_mark_as_read(self):
        """user01收到的某个通知标为已读，传递slug参数"""
        response = self.client.get(reverse("notifications:mark_as_read",
                                           kwargs={"slug": self.first_notification.slug}))
        assert response.status_code == 302
        assert Notification.objects.unread().count() == 2

    def test_latest_notifications(self):
        """user02最近收到的通知"""
        response = self.other_client.get(reverse("notifications:latest_notifications"))
        assert response.status_code == 200
        assert self.first_notification in response.context["notifications"]
        assert self.second_notification in response.context["notifications"]
