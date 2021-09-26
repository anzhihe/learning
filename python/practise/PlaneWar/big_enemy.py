#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    big_enemy.py
 @Function:    大型敌机
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/6
"""

import random
import pygame
from pygame.sprite import Sprite
import constants


class BigEnemy(Sprite):
    """大型敌机类"""

    # 大型敌机每次移动时的偏移量
    offset = constants.BIG_ENEMY_OFFSET

    def __init__(self, window):
        """初始化大型敌机"""

        # 调用父类Sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象
        self.window = window

        # 加载大型敌机的相关图片
        self._load_images()

        # 获得大型敌机的矩形
        self.rect = self.image.get_rect()

        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()

        # 设置大型敌机的矩形的初始位置为：窗口的矩形的顶部一个随机的水平位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width -
                                        self.rect.width)

        # 标记大型敌机没有在切换爆炸图片
        self.is_switching_explode_image = False

        # 标记大型敌机没有在切换被击中图片
        self.is_switching_hit_image = False

        # 切换大型敌机爆炸图片的计数器
        self.switch_explode_counter = 0

        # 切换大型敌机被击中图片的计数器
        self.switch_hit_counter = 0

        # 切换大型敌机图片的计数器
        self.switch_counter = 0

        # 大型敌机的初始能量
        self.energy = constants.BIG_ENEMY_INITIAL_ENERGY

    def _load_images(self):
        """加载大型敌机的相关图片"""

        # 加载大型敌机的第1张图片
        self.image = self.big_image1 = pygame.image.load("images/big_enemy1.png")

        # 加载大型敌机的第2张图片
        self.big_image2 = pygame.image.load("images/big_enemy2.png")

        # 加载大型敌机爆炸的图片
        for image_num in range(1, 7):
            exec('self.explode_image%d = pygame.image.load("images/big_enemy_explode%d.png")' \
                 % (image_num, image_num))

        # 加载大型敌机被击中的图片
        self.hit_image = pygame.image.load("images/big_enemy_hit.png")

    def update(self):
        """更新大型敌机的位置"""

        # 增大大型敌机的矩形的属性top以向下移动
        self.rect.top += BigEnemy.offset

    @classmethod
    def update_offset(cls, pixels):
        """更新大型敌机每次移动的偏移量"""

        # 大型敌机每次移动时的偏移量增加指定的像素数
        BigEnemy.offset += pixels

    def play_explode_sound(self):
        """播放大型敌机爆炸的声音"""

        # 加载大型敌机爆炸的声音文件
        explode_sound = pygame.mixer.Sound("sounds/big_enemy_explode.wav")

        # 设置爆炸声音的音量
        explode_sound.set_volume(constants.EXPLODE_SOUND_VOLUME)

        # 播放爆炸的声音
        explode_sound.play()

    def switch_explode_image(self):
        """切换大型敌机爆炸的图片"""

        # 切换大型敌机爆炸图片的计数器加1
        self.switch_explode_counter += 1

        # 如果计数器回到指定的值，才切换一次大型敌机爆炸的图片
        if self.switch_explode_counter == constants.BIG_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY:
            # 如果是大型敌机的图片
            if self.image == self.big_image1 or self.image == self.big_image2:
                # 切换到爆炸的第1张图片
                self.image = self.explode_image1
            # 如果是爆炸的第1张图片
            elif self.image == self.explode_image1:
                # 切换到爆炸的第2张图片
                self.image = self.explode_image2
            # 如果是爆炸的第2张图片
            elif self.image == self.explode_image2:
                # 切换到爆炸的第3张图片
                self.image = self.explode_image3
            # 如果是爆炸的第3张图片
            elif self.image == self.explode_image3:
                # 切换到爆炸的第4张图片
                self.image = self.explode_image4
            # 如果是爆炸的第4张图片
            elif self.image == self.explode_image4:
                # 切换到爆炸的第5张图片
                self.image = self.explode_image5
            # 如果是爆炸的第5张图片
            elif self.image == self.explode_image5:
                # 切换到爆炸的第6张图片
                self.image = self.explode_image6
            # 如果是爆炸的第6张图片
            elif self.image == self.explode_image6:
                # 将大型敌机从所有分组中删除
                self.kill()

            # 计数器重置为0
            self.switch_explode_counter = 0

    def switch_hit_image(self):
        """切换大型敌机被击中的图片"""

        # 切换大型敌机被击中图片的计数器加1
        self.switch_hit_counter += 1

        # 如果计数器回到指定的值，才切换一次大型敌机被击中的图片
        if self.switch_hit_counter == constants.BIG_ENEMY_SWITCH_HIT_IMAGE_FREQUENCY:
            # 如果是大型敌机的图片
            if self.image == self.big_image1 or self.image == self.big_image2:
                # 切换到大型敌机被击中的图片
                self.image = self.hit_image
            # 如果是大型敌机被击中的图片
            elif self.image == self.hit_image:
                # 切换到大型敌机的第1张图片
                self.image = self.big_image1
                # 标记大型敌机没有在切换被击中图片
                self.is_switching_hit_image = False

            # 计数器重置为0
            self.switch_hit_counter = 0

    def draw_energy_lines(self):
        """在大型敌机的尾部上方绘制能量线"""

        # 在大型敌机的尾部上方绘制一条白色线段
        pygame.draw.line(self.window, (255, 255, 255),
                         (self.rect.left, self.rect.top),
                         (self.rect.right, self.rect.top),
                         5)

        # 剩余能量 / 初始化能量
        energy_left_ratio = self.energy / constants.BIG_ENEMY_INITIAL_ENERGY

        # 如果大型敌机还有能量(if self.energy != 0)
        if energy_left_ratio != 0:
            # 在大型敌机的尾部上方绘制一条红色线段
            pygame.draw.line(self.window, (255, 0, 0),
                             (self.rect.left, self.rect.top),
                             (self.rect.left + self.rect.width *
                              energy_left_ratio, self.rect.top),
                             5)

    def switch_image(self):
        """切换大型敌机的图片"""

        # 切换大型敌机图片的计数器加1
        self.switch_counter += 1

        # 如果计数器加到指定的值，才切换一次大型敌机的图片
        if self.switch_counter == constants.BIG_ENEMY_SWITCH_IMAGE_FREQUENCY:
            # 如果是第1张图片
            if self.image == self.big_image1:
                # 切换到第2张图片
                self.image = self.big_image2
            # 如果是第2张图片
            elif self.image == self.big_image2:
                # 切换到第1张图片
                self.image = self.big_image1

            # 计数器重置为0
            self.switch_counter = 0