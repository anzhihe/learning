# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import pymongo
from yunqiCrawl.items import YunqiBookListItem


class YunqicrawlPipeline(object):

    def __init__(self, mongo_uri, mongo_db,replicaset):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.replicaset = replicaset

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'yunqi'),
            replicaset = crawler.settings.get('REPLICASET')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri,replicaset=self.replicaset)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        if isinstance(item,YunqiBookListItem):
            self._process_booklist_item(item)
        else:
            self._process_bookeDetail_item(item)
        return item



    def _process_booklist_item(self,item):
        '''
        处理小说信息
        :param item:
        :return:
        '''
        self.db.bookInfo.insert(dict(item))





    def _process_bookeDetail_item(self,item):
        '''
        处理小说热度
        :param item:
        :return:
        '''
        #需要对数据进行一下清洗，类似：总字数：10120，提取其中的数字
        pattern = re.compile('\d+')
        #去掉空格和换行
        item['novelLabel'] = item['novelLabel'].strip().replace('\n','')

        match = pattern.search(item['novelAllClick'])
        item['novelAllClick'] = match.group() if match else item['novelAllClick']

        match = pattern.search(item['novelMonthClick'])
        item['novelMonthClick'] = match.group() if match else item['novelMonthClick']

        match = pattern.search(item['novelWeekClick'])
        item['novelWeekClick'] = match.group() if match else item['novelWeekClick']

        match = pattern.search(item['novelAllPopular'])
        item['novelAllPopular'] = match.group() if match else item['novelAllPopular']

        match = pattern.search(item['novelMonthPopular'])
        item['novelMonthPopular'] = match.group() if match else item['novelMonthPopular']

        match = pattern.search(item['novelWeekPopular'])
        item['novelWeekPopular'] = match.group() if match else item['novelWeekPopular']

        match = pattern.search(item['novelAllComm'])
        item['novelAllComm'] = match.group() if match else item['novelAllComm']

        match = pattern.search(item['novelMonthComm'])
        item['novelMonthComm'] = match.group() if match else item['novelMonthComm']

        match = pattern.search(item['novelWeekComm'])
        item['novelWeekComm'] = match.group() if match else item['novelWeekComm']

        self.db.bookhot.insert(dict(item))
