#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    constants.py
 @Function:    定义常量
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/5
"""

import pygame


# 在水平方向上，窗口尺寸占电脑屏幕尺寸的比例
SCALE_HORIZONTAL = 2 / 5
# 在竖直方向上，窗口尺寸占电脑屏幕尺寸的比例
SCALE_VERTICAL = 4 / 5

# 动画的最大帧率
MAX_FRAMERATE = 30

# 我方飞机的初始生命数
MY_PLANE_INITIAL_LIFE_NUMBER = 3
# 炸弹的初始数量
BOMB_INITIAL_NUMBER = 3

# 小型敌机每次移动时的偏移量
SMALL_ENEMY_OFFSET = 6
# 中型敌机每次移动时的偏移量
MID_ENEMY_OFFSET = 5
# 大型敌机每次移动时的偏移量
BIG_ENEMY_OFFSET = 2
# 子弹补给每次移动时的偏移量
BULLET_SUPPLY_OFFSET = 5
# 炸弹补给每次移动时的偏移量
BOMB_SUPPLY_OFFSET = 5

# 自定义事件"创建子弹"的id
ID_OF_CREATE_BULLET = pygame.USEREVENT
# 自定义事件"创建子弹补给"的id
ID_OF_CREATE_BULLET_SUPPLY = pygame.USEREVENT + 5
# 自定义事件"创建双发子弹"的id
ID_OF_CREATE_DOUBLE_BULLET = pygame.USEREVENT + 6
# 自定义事件"创建炸弹补给"的id
ID_OF_CREATE_BOMB_SUPPLY = pygame.USEREVENT + 7
# 自定义事件"创建小型敌机"的id
ID_OF_CREATE_SMALL_ENEMY = pygame.USEREVENT + 1
# 自定义事件"创建中型敌机"的id
ID_OF_CREATE_MID_ENEMY = pygame.USEREVENT + 2
# 自定义事件"创建大型敌机"的id
ID_OF_CREATE_BIG_ENEMY = pygame.USEREVENT + 3
# 自定义事件"解除我方飞机的无敌状态"的id
ID_OF_CANCEL_INVINCIBLE = pygame.USEREVENT + 4

# 自定义事件"创建子弹"的时间间隔
INTERVAL_OF_CREATE_BULLET = 500
# 自定义事件"创建双发子弹"的时间间隔
INTERVAL_OF_CREATE_DOUBLE_BULLET = 500
# 自定义事件"创建子弹补给"的时间间隔
INTERVAL_OF_CREATE_BULLET_SUPPLY = 25000
# 自定义事件"创建炸弹补给"的时间间隔
INTERVAL_OF_CREATE_BOMB_SUPPLY = 40000
# 自定义事件"创建小型敌机"的时间间隔
INTERVAL_OF_CREATE_SMALL_ENEMY = 2000
# 自定义事件"创建中型敌机"的时间间隔
INTERVAL_OF_CREATE_MID_ENEMY = 3600
# 自定义事件"创建大型敌机"的时间间隔
INTERVAL_OF_CREATE_BIG_ENEMY = 18000
# 自定义事件"解除我方飞机的无敌状态"的时间间隔
INTERVAL_OF_CANCEL_INVINCIBLE = 5000

# 爆炸声音的音量
EXPLODE_SOUND_VOLUME = 0.8
# 碰撞声音的音量
COLLIDE_SOUND_VOLUME = 0.8
# 背景音乐的音量
BGM_SOUND_VOLUME = 0.3

# 切换我方飞机图片的频率
MY_PLANE_SWITCH_IMAGE_FREQUENCY = 3
# 切换大型敌机图片的频率
BIG_ENEMY_SWITCH_IMAGE_FREQUENCY = 3
# 切换小型敌机爆炸图片的频率
SMALL_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 8
# 切换中型敌机爆炸图片的频率
MID_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 8
# 切换大型敌机爆炸图片的频率
BIG_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 6
# 切换中型敌机被击中图片的频率
MID_ENEMY_SWITCH_HIT_IMAGE_FREQUENCY = 3
# 切换大型敌机被击中图片的频率
BIG_ENEMY_SWITCH_HIT_IMAGE_FREQUENCY = 3

# 中型敌机的初始能量
MID_ENEMY_INITIAL_ENERGY = 4
# 大型敌机的初始能量
BIG_ENEMY_INITIAL_ENERGY = 8

# 间距
MARGIN = 10

# 36号字体大小
FONT_SIZE_36 = 36
# 48号字体大小
FONT_SIZE_48 = 48
# 96号字体大小
FONT_SIZE_96 = 96

# 白色
WHITE_COLOR = (255, 255, 255)
# 灰色
GRAY_COLOR = (128, 128, 128)

# 双发子弹在水平方向上距离我方飞机中心的偏移量
DOUBLE_BULLET_OFFSET = 32

# 双发子弹计数器的最大值
DOUBLE_BULLET_COUNTER_MAX = 16

# 摧毁小型敌机后的得分
DESTROY_SMALL_ENEMY_SCORE = 10
# 摧毁中型敌机后的得分
DESTROY_MID_ENEMY_SCORE = 50
# 摧毁大型敌机后的得分
DESTROY_BIG_ENEMY_SCORE = 100

# 关数1的得分最大值
LEVEL1_SCORE_MAX = 500
# 关数2的得分最大值
LEVEL2_SCORE_MAX = 1000
# 关数3的得分最大值
LEVEL3_SCORE_MAX = 1500
# 关数4的得分最大值
LEVEL4_SCORE_MAX = 2000