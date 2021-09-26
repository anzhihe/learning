#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    bomb_supply.py
 @Function:    炸弹补给
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/13
"""

import random
import pygame
from pygame.sprite import Sprite
import constants


class BombSupply(Sprite):
    """炸弹补给类"""

    # 炸弹补给每次移动时的偏移量
    offset = constants.BOMB_SUPPLY_OFFSET

    def __init__(self, window):
        """初始化炸弹补给"""

        # 调用父类Sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象
        self.window = window

        # 加载炸弹补给图片
        self.image = pygame.image.load("images/bomb_supply.png")

        # 获得炸弹补给的矩形
        self.rect = self.image.get_rect()

        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()

        # 设置炸弹补给的矩形的初始位置为：窗口的矩形的顶部一个随机的水平位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width -
                                        self.rect.width)

    def update(self):
        """更新炸弹补给的位置"""

        # 增大炸弹补给的矩形的属性top以向下移动
        self.rect.top += BombSupply.offset

    @classmethod
    def update_offset(cls, pixels):
        """更新炸弹补给每次移动的偏移量"""

        # 炸弹补给每次移动时的偏移量增加指定的像素数
        BombSupply.offset += pixels

    def play_collide_sound(self):
        """播放炸弹补给和我方飞机碰撞的声音"""

        # 加载炸弹补给碰撞的声音文件
        collide_sound = pygame.mixer.Sound("sounds/bomb_supply_collide.wav")

        # 设置碰撞声音的音量
        collide_sound.set_volume(constants.COLLIDE_SOUND_VOLUME)

        # 播放碰撞的声音
        collide_sound.play()