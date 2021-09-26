#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    bullet_supply.py
 @Function:    子弹补给
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/9
"""

import random
import pygame
from pygame.sprite import Sprite
import constants


class BulletSupply(Sprite):
    """子弹补给类"""

    # 子弹补给每次移动时的偏移量
    offset = constants.BULLET_SUPPLY_OFFSET

    def __init__(self, window):
        """初始化子弹补给"""

        # 调用父类Sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象
        self.window = window

        # 加载子弹补给图片
        self.image = pygame.image.load("images/bullet_supply.png")

        # 获得子弹补给的矩形
        self.rect = self.image.get_rect()

        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()

        # 设置子弹补给的矩形的初始位置为：窗口的矩形的顶部一个随机的水平位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width -
                                        self.rect.width)

        # 子弹补给每次移动时的偏移量
        self.offset = 5

    def update(self):
        """更新子弹补给的位置"""

        # 增大子弹补给的矩形的属性top以向下移动
        self.rect.top += BulletSupply.offset

    @classmethod
    def update_offset(cls, pixels):
        """更新子弹补给每次移动的偏移量"""

        # 子弹补给每次移动时的偏移量增加指定的像素数
        BulletSupply.offset += pixels

    def play_collide_sound(self):
        """播放子弹补给和我方飞机碰撞的声音"""

        # 加载子弹补给碰撞的声音文件
        collide_sound = pygame.mixer.Sound("sounds/bullet_supply_collide.wav")

        # 设置碰撞声音的音量
        collide_sound.set_volume(constants.COLLIDE_SOUND_VOLUME)

        # 播放碰撞的声音
        collide_sound.play()