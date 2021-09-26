#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    pause_button.py
 @Function:    暂停按钮
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/15
"""

import pygame
import constants


class PauseButton:
    """暂停按钮类"""

    def __init__(self, window):
        """初始化暂停按钮"""

        # 加载鼠标没有移至状态的暂停图片
        self.image_pause_not_mouseover = pygame.image.load(
            'images/pause_not_mouseover.png')

        # 加载鼠标移至状态的暂停图片
        self.image_pause_mouseover = pygame.image.load(
            'images/pause_mouseover.png')

        # 加载鼠标没有移至状态的继续图片
        self.image_resume_not_mouseover = pygame.image.load(
            'images/resume_not_mouseover.png')

        # 加载鼠标移至状态的继续图片
        self.image_resume_mouseover = pygame.image.load(
            'images/resume_mouseover.png')

        # 设置暂停按钮的初始图片是鼠标没有移至状态的暂停图片
        self.image = self.image_pause_not_mouseover

        # 获得暂停按钮的矩形
        self.rect = self.image.get_rect()

        # 设置暂停按钮的矩形的初始位置
        self.rect.top = constants.MARGIN
        self.rect.right = window.get_rect().right - constants.MARGIN

        # 标记游戏不处于暂停状态
        self.is_pause = False

    def switch_image(self, event):
        """切换暂停按钮的图片"""

        # 如果游戏不处于暂停状态
        if not self.is_pause:
            # 如果鼠标没有移动到暂停按钮上
            if not self.rect.collidepoint(event.pos):
                # 设置暂停按钮的图片是正常状态的暂停图片
                self.image = self.image_pause_not_mouseover
            # 如果鼠标移动到暂停按钮上
            else:
                # 设置暂停按钮的图片是鼠标移至状态的暂停图片
                self.image = self.image_pause_mouseover
        # 如果游戏处于暂停状态
        else:
            # 如果鼠标没有移动到暂停按钮上
            if not self.rect.collidepoint(event.pos):
                # 设置暂停按钮的图片是正常状态的继续图片
                self.image = self.image_resume_not_mouseover
            # 如果鼠标移动到暂停按钮上
            else:
                # 设置暂停按钮的图片是鼠标移至状态的继续图片
                self.image = self.image_resume_mouseover
