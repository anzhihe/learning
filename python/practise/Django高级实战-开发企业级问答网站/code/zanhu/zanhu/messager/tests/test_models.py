#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from test_plus.test import TestCase

from zanhu.messager.models import Message


class MessagesModelsTest(TestCase):

    def setUp(self):
        self.user = self.make_user("user01")
        self.other_user = self.make_user("user02")
        self.first_message = Message.objects.create(
            sender=self.user,
            recipient=self.other_user,
            message="user01发送给user02的第一条消息"
        )
        self.second_message = Message.objects.create(
            sender=self.user,
            recipient=self.other_user,
            message="user01发送给user02的第二条消息"
        )
        self.third_message = Message.objects.create(
            sender=self.other_user,
            recipient=self.user,
            message="user02回复给user01的消息"
        )

    def test_object_instance(self):
        """测试对象是否为Message类型"""
        assert isinstance(self.first_message, Message)
        assert isinstance(self.second_message, Message)
        assert isinstance(self.third_message, Message)

    def test_return_values(self):
        """对象的返回值"""
        assert str(self.first_message) == "user01发送给user02的第一条消息"
        assert self.first_message.message == "user01发送给user02的第一条消息"

    def test_conversation(self):
        """私信功能"""
        conversation = Message.objects.get_conversation(self.user, self.other_user)
        assert conversation.last().message == "user02回复给user01的消息"

    def test_recent_conversation(self):
        """最近的私信互动"""
        active_user = Message.objects.get_most_recent_conversation(self.user)
        assert active_user == self.other_user

    def test_single_marking_as_read(self):
        self.first_message.mark_as_read()
        read_message = Message.objects.filter(unread=False)
        assert read_message[0] == self.first_message
