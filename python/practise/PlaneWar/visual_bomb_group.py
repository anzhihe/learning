#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    visual_bomb_group.py
 @Function:    可视化炸弹组
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/13
"""

import pygame
import constants


class VisualBombGroup:
    """可视化炸弹组"""

    def __init__(self, window):
        """初始化可视化炸弹组"""

        # 获得窗口对象
        self.window = window

        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()

        # 炸弹的初始数量
        self.bomb_number = 3

        # 加载炸弹图片
        self.bomb_image = pygame.image.load("images/bomb.png")

        # 炸弹图片矩形的列表
        self.bomb_rect_list = []

        # 根据炸弹的初始数量，将对应数量的炸弹图片矩形定位在窗口中
        for i in range(self.bomb_number):
            # 获得炸弹的图片矩形
            bomb_rect = self.bomb_image.get_rect()

            # 设置炸弹的图片矩形的初始位置
            bomb_rect.bottom = self.window_rect.height - constants.MARGIN
            bomb_rect.right = (constants.MARGIN + bomb_rect.width) * (i + 1)

            # 将炸弹的图片矩形添加到列表中
            self.bomb_rect_list.append(bomb_rect)

    def play_explode_sound(self):
        """播放炸弹爆炸的声音"""

        # 加载炸弹爆炸的声音文件
        explode_sound = pygame.mixer.Sound("sounds/bomb_explode.wav")

        # 设置爆炸声音的音量
        explode_sound.set_volume(constants.EXPLODE_SOUND_VOLUME)

        # 播放爆炸的声音
        explode_sound.play()