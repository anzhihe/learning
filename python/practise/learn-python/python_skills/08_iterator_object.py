#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    08_iterator_object.py
 @Function:    实现可迭代对象和迭代器对象
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/26
"""


"""如何实现可迭代对象和迭代器对象？"""

"""
实际案例：
    某软件要求，从网络抓取各个城市气温信息,并依次显示:
    北京: 15~20
    天津: 17~22
    长春: 12~18
    ......
    如果一次抓取所有城市天气再显示，显示第一个城市气温时,有很高
    的延时，并且浪费存储空间.我们期望以"用时访问"的策略,并且能把
    所有城市气温封装到一个对象里，可用for语句进行迭代.如果解决?
"""

"""
解决方案：
    Step1: 实现一个迭代器对象WeatherIterator，next方法每次返回一个城市气温
    Step2: 实现一个可迭代对象WeatherIterable，__iter__方法返回一个迭代器对象
"""

"""
    如果一个对象同时实现了特殊方法__iter__()和__next__()，那么该对象也被称为迭代器对象。如果
将该对象用于for-in语句，for-in语句首先会调用特殊方法__iter__()返回一个可迭代对象，然后不断调用
该可迭代对象的特殊方法__next__()返回下一次迭代的值，直到遇到StopIteration时退出循环
"""

from collections import Iterable, Iterator
import requests

class WeatherIterator(Iterator):
    """构建天气迭代器，继承Iterator"""

    # 定义构造器，返回传入城市的天气信息
    def __init__(self, cities):
        # 传入城市字符串的列表
        self.cities = cities
        # 迭代的位置
        self.index = 0

    def get_weather(self, city):
        """获取城市天气信息"""

        res = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = res.json()['data']['forecast'][0]
        return '%s: %s , %s' % (city, data['low'], data['high'])

    def __next__(self):
        """每次返回一个城市天气的迭代信息"""

        # 全部迭代完后抛出异常
        if self.index == len(self.cities):
            raise StopIteration

        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


class WeatherIterable(Iterable):
    """构建天气可迭代对象，继承Iterable"""

    def __init__(self, cities):
        """定义构造器"""

        self.cities = cities

    def __iter__(self):
        """实现可迭代接口，返回WeatherIterator"""

        return WeatherIterator(self.cities)

if __name__ == '__main__':

    # 实例化天气可迭代对象，返回城市列表的天气信息
    for x in WeatherIterable([u'北京', u'上海', u'广州', u'长春']):
        print(x)