#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    bullet.py
 @Function:    定义子弹
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/3
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹类"""

    def __init__(self, window, my_plane):
        """初始化子弹"""

        # 调用父类Sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象
        self.window = window

        # 加载子弹图片
        self.image = pygame.image.load("images/bullet.png")

        # 获得子弹的矩形
        self.rect = self.image.get_rect()

        # 获得我方飞机的矩形
        self.my_plane_rect = my_plane.rect

        # 设置子弹的矩形的初始位置为：我方飞机的矩形的顶部居中位置
        self.rect.midtop = self.my_plane_rect.midtop

        # 子弹每次移动时的偏移量
        self.offset = 50

    def update(self):
        """更新子弹的位置"""

        # 减少子弹的矩形的属性top以向上移动
        self.rect.top -= self.offset