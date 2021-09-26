#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    score_board.py
 @Function:    得分板
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/14
"""

import pygame
import constants


class ScoreBoard:
    """得分板类"""

    def __init__(self, window):
        """初始化得分板"""

        # 窗口对象
        self.window = window

        # 当前得分
        self.current_score = 0

        # 最高得分
        self.highest_score = self.read_highest_score()

        # 当前关数
        self.current_level = 1

        # 获得指定字体和指定字体大小的字体对象
        self.font_36 = pygame.font.Font("fonts/wawa.ttf", constants.FONT_SIZE_36)

    def draw_current_score(self):
        """在得分板中绘制当前得分"""

        # 当前得分的文本
        current_score_text = "当前得分：{}".format(self.current_score)

        # 获得当前得分文本对应的surface对象
        current_score_surface = self.font_36.render(current_score_text,
                                                    True,
                                                    constants.WHITE_COLOR)

        # 获得当前得分文本的矩形
        self.current_score_rect = current_score_surface.get_rect()

        # 将当前得分文本的矩形定位在窗口的左上角
        self.current_score_rect.left = constants.MARGIN
        self.current_score_rect.top = constants.MARGIN

        # 在窗口的左上角绘制当前得分
        self.window.blit(current_score_surface, self.current_score_rect)

    def draw_highest_score(self):
        """在得分板中绘制最高得分"""

        # 最高得分的文本
        highest_score_text = "最高得分：{}".format(self.highest_score)

        # 获得最高得分文本对应的surface对象
        highest_score_surface = self.font_36.render(highest_score_text,
                                                    True,
                                                    constants.WHITE_COLOR)

        # 获得最高得分文本的矩形
        self.highest_score_rect = highest_score_surface.get_rect()

        # 将最高得分文本的矩形定位在窗口的左上角当前得分的下面
        self.highest_score_rect.left = constants.MARGIN
        self.highest_score_rect.top = self.current_score_rect.bottom + constants.MARGIN

        # 在窗口的左上角当前得分的下面绘制最高得分
        self.window.blit(highest_score_surface, self.highest_score_rect)

    def draw_current_level(self):
        """在得分板中绘制当前关数"""

        # 当前关数的文本
        current_level_text = "当前关数：{}".format(self.current_level)

        # 获得当前关数文本对应的surface对象
        current_level_surface = self.font_36.render(current_level_text,
                                                    True,
                                                    constants.WHITE_COLOR)

        # 获得当前关数文本的矩形
        current_level_rect = current_level_surface.get_rect()

        # 将当前关数文本的矩形定位在窗口的左上角最高得分的下面
        current_level_rect.left = constants.MARGIN
        current_level_rect.top = self.highest_score_rect.bottom + \
            constants.MARGIN

        # 在窗口的左上角最高得分的下面绘制当前关数
        self.window.blit(current_level_surface, current_level_rect)

    def read_highest_score(self):
        """读取最高得分"""

        # 打开存放最高得分的文件
        with open('txts/highest_score.txt') as file:
            # 返回读取的最高得分
            return int(file.read())

    def save_highest_score(self):
        """保存当前得分"""

        # 打开存放最高得分的文件
        with open('txts/highest_score.txt', 'w') as file:
            file.write(str(self.current_score))

    def update_current_level(self):
        """根据当前得分更新当前关数"""

        # 如果当前得分大于关数1的得分最大值，并且当前关数是1
        if self.current_score > constants.LEVEL1_SCORE_MAX and \
                self.current_level == 1:
            # 将当前关数设为2
            self.current_level = 2
        # 如果当前得分大于关数2的得分最大值，并且当前关数是2
        elif self.current_score > constants.LEVEL2_SCORE_MAX and \
                self.current_level == 2:
            # 将当前关数设为3
            self.current_level = 3
        # 如果当前得分大于关数3的得分最大值，并且当前关数是3
        elif self.current_score > constants.LEVEL3_SCORE_MAX and \
                self.current_level == 3:
            # 将当前关数设为4
            self.current_level = 4
        # 如果当前得分大于关数4的得分最大值，并且当前关数是4
        elif self.current_score > constants.LEVEL4_SCORE_MAX and \
                self.current_level == 4:
            # 将当前关数设为5
            self.current_level = 5