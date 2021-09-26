#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    my_plane.py
 @Function:    定义我方飞机
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/3
"""

import pygame
from pygame.sprite import Sprite
import constants


class MyPlane(Sprite):
    """我方飞机类"""

    def __init__(self, window):
        """初始化我方飞机"""

        # 调用父类Sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象
        self.window = window

        # 加载我方飞机的第1张图片
        self.image1 = pygame.image.load('images/my_plane1.png')

        # 我方飞机的初始图片是第1张图片
        self.image = self.image1

        # 加载我方飞机的第2张图片
        self.image2 = pygame.image.load('images/my_plane2.png')

        # 获得我方飞机的矩形
        self.rect = self.image.get_rect()

        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()

        # 设置我方飞机的矩形的初始位置为：窗口的底部居中位置
        self.rect.midbottom = self.window_rect.midbottom

        # 标记我方飞机不向上移动
        self.is_move_up = False

        # 标记我方飞机不向下移动
        self.is_move_down = False

        # 标记我方飞机不向左移动
        self.is_move_left = False

        # 标记我方飞机不向右移动
        self.is_move_right = False

        # 我方飞机每次移动时的偏移量
        self.offset = 20

        # 切换我方飞机图片的计数器
        self.switch_counter = 0

        # 我方飞机的初始生命数
        self.life_number = 3

        # 我方飞机的生命图片
        self.life_image = pygame.transform.scale(self.image1,
                                (round(self.rect.width / 2), (round(self.rect.height /2))))

        # 我方飞机的生命图片矩形的列表
        self.life_rect_list = []

        # 根据我方飞机的初始生命数，将对应数量的生命图片矩形定位在窗口中
        for life_num in range(self.life_number):
            # 获得我方飞机的生命图片矩形
            life_rect = self.life_image.get_rect()

            # 设置我方飞机的生命图片矩形的初始位置
            life_rect.bottom = self.window_rect.height - constants.MARGIN
            life_rect.right = self.window_rect.width - constants.MARGIN - (
                life_rect.width + constants.MARGIN) * life_num

            # 将我方飞机的生命图片矩形添加到列表中
            self.life_rect_list.append(life_rect)

        # 标记我方飞机不处于无敌状态
        self.is_invincible = False

    def update(self):
        """更新我方飞机的位置"""

        # 如果我方飞机被标记为向上移动，并且向上移动后不会超出窗口的上边缘

        if self.is_move_up and self.rect.top - self.offset > 0:
            # 减少我方飞机的矩形的属性top以向上移动
            self.rect.top -= self.offset
        # 如果我方飞机被标记为向下移动，并且向下移动后不会超出窗口的下边缘
        if self.is_move_down and self.rect.bottom + self.offset < \
            self.window_rect.height:
            # 增大我方飞机的矩形的属性bottom以向下移动
            self.rect.bottom += self.offset
        # 如果我方飞机被标记为向左移动，并且向左移动后不会超出窗口的左边缘
        if self.is_move_left and self.rect.left - self.offset > 0:
            # 减少我方飞机的矩形的属性left以向左移动
            self.rect.left -= self.offset
        # 如果我方飞机被标记为向右移动，并且向右移动后不会超出窗口的右边缘
        if self.is_move_right and self.rect.right + self.offset < self.window_rect.width:
            # 增大我方飞机的矩形的属性right以向右移动
            self.rect.right += self.offset

    def draw(self):
        """在窗口中绘制我方飞机"""

        # 在窗口的指定位置绘制一架我方飞机
        self.window.blit(self.image, self.rect)

    def switch_image(self):
        """切换我方飞机的图片"""

        # 切换我方飞机图片的计数器加1
        self.switch_counter += 1

        # 如果计数器加到3，才切换一次我方飞机的图片
        if self.switch_counter == constants.MY_PLANE_SWITCH_IMAGE_FREQUENCY:
            # 如果是第1张图片
            if self.image == self.image1:
                # 切换到第2张图片
                self.image = self.image2
            # 如果是第2张图片
            elif self.image == self.image2:
                # 切换到第1张图片
                self.image = self.image1

            # 计数器重置为0
            self.switch_counter = 0

    def reset_position(self):
        """重置我方飞机的位置"""

        # 设置我方飞机的矩形的初始位置为：窗口的底部居中位置
        self.rect.midbottom = self.window_rect.midbottom