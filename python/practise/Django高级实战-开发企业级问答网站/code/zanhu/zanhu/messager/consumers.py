#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MessagesConsumer(AsyncWebsocketConsumer):
    """处理私信应用中WebSocket请求"""

    async def connect(self):
        if self.scope['user'].is_anonymous:
            # 未登录的用户拒绝连接
            await self.close()
        else:
            await self.channel_layer.group_add(self.scope['user'].username, self.channel_name)
            await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        """接收私信"""
        await self.send(text_data=json.dumps(text_data))

    async def disconnect(self, code):
        """离开聊天组"""
        await self.channel_layer.group_discard(self.scope['user'].username, self.channel_name)


"""
# event loop/event handler/sync/async

from channels.consumer import SyncConsumer, AsyncConsumer


class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        # 同步逻辑
        import requests
        requests.get("url")
        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        user = self.scope["user"]
        path = self.scope["path"]  # Request请求的路径，HTTP, WebSocket
        self.scope["headers"]
        self.scope["method"]  # Http

        self.send({
            "type": "websocket.send",
            "text": event["text"]
        })


class EchoAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        # 改成异步逻辑
        import aiohttp

        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        # ORM 同步的代码
        user = User.objects.get(username=username)

        # ORM语句同步变异步，方式一
        from channels.db import database_sync_to_async
        user = await database_sync_to_async(User.objects.get(username=username))

        # ORM语句同步变异步，方式二
        @database_sync_to_async
        def get_username(username):
            return User.objects.get(username=username)

        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })


# 什么时候使用sync或async

# scope, 在ASGI接口规范中定义了

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class MyConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        # 自定义的子协议
        self.accept(subprotocol='you protocol')
        self.close(code=403)

    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data="imooc.com")
        self.send(bytes_data="imooc.com")  # 把字符串转换成二进制的帧返回

        self.close()

    def disconnect(self, code):
        pass


class MyAsyncConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        # 自定义的子协议
        await self.accept(subprotocol='you protocol')
        await self.close(code=403)

    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data="imooc.com")
        await self.send(bytes_data="imooc.com")  # 把字符串转换成二进制的帧返回

        await self.close()

    async def disconnect(self, code):
        pass
"""
