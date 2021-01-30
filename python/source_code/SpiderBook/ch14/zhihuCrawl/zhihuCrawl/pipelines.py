# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from zhihuCrawl.items import UserInfoItem


class ZhihucrawlPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'zhihu')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):

        if isinstance(item,UserInfoItem):
            self._process_user_item(item)
        else:
            self._process_relation_item(item)
        return item

    def _process_user_item(self,item):
        self.db.UserInfo.insert(dict(item))


    def _process_relation_item(self,item):
        self.db.Relation.insert(dict(item))

class ZhuhuiImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):#重写ImagesPipeline   get_media_requests方法


        '''
        :param item:
        :param info:
        :return:
        在工作流程中可以看到，
        管道会得到文件的URL并从项目中下载。
        为了这么做，你需要重写 get_media_requests() 方法，
        并对各个图片URL返回一个Request:
        '''
        if isinstance(item,UserInfoItem):
            if item['user_image_url']:
                    yield scrapy.Request(item['user_image_url'])
            else:
                super(ZhuhuiImagePipeline, self).get_media_requests(item, info)


    def item_completed(self, results, item, info):
        '''

        :param results:
        :param item:
        :param info:
        :return:
        当一个单独项目中的所有图片请求完成时（要么完成下载，要么因为某种原因下载失败），
         item_completed() 方法将被调用。
        '''
        if isinstance(item,UserInfoItem):
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
        return item