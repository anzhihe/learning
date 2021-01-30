# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserInfoItem(scrapy.Item):
    # define the fields for your item here like:
    #id
    user_id = scrapy.Field()
    #头像img
    user_image_url = scrapy.Field()
    #姓名
    name = scrapy.Field()
    #居住地
    location = scrapy.Field()
    #技术领域
    business = scrapy.Field()
    #性别
    gender = scrapy.Field()
    #公司
    employment = scrapy.Field()
    #职位
    position = scrapy.Field()
    #教育经历
    education = scrapy.Field()
    #我关注的人数
    followees_num = scrapy.Field()
    #关注我的人数
    followers_num = scrapy.Field()

class RelationItem(scrapy.Item):
    #用户id
    user_id =scrapy.Field()
    #relation 类型
    relation_type =scrapy.Field()
    #和我有关系人的id列表
    relations_id = scrapy.Field()


