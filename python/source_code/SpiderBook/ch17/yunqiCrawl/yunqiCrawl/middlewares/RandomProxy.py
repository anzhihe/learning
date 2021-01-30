#coding:utf-8
import random


'''
这个类主要用于产生随机代理
'''
class RandomProxy(object):


    def __init__(self,http_proxy):#初始化一下数据库连接
        self.http_proxy = http_proxy

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.get('HTTP_PROXY'))

    def process_request(self, request, spider):
        '''
        在请求上添加代理
        :param request:
        :param spider:
        :return:
        '''
        request.meta['proxy'] =self.http_proxy

