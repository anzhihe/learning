#coding:utf-8
import random


class RandomUserAgent(object):

    def __init__(self,agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls,crawler):
        #从Settings中加载USER_AGENTS的值
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self,request,spider):
        #在process_request中设置User-Agent的值
        request.headers.setdefault('User-Agent', random.choice(self.agents))
