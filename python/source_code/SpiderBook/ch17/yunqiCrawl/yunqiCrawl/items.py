# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YunqiBookListItem(scrapy.Item):
    novelId = scrapy.Field()
    novelName = scrapy.Field()
    novelLink = scrapy.Field()
    novelAuthor = scrapy.Field()
    novelType = scrapy.Field()
    novelStatus = scrapy.Field()
    novelUpdateTime = scrapy.Field()
    novelWords = scrapy.Field()
    novelImageUrl = scrapy.Field()

class YunqiBookDetailItem(scrapy.Item):
    novelId = scrapy.Field()
    novelLabel  =scrapy.Field()
    novelAllClick = scrapy.Field()
    novelMonthClick = scrapy.Field()
    novelWeekClick = scrapy.Field()
    novelAllPopular = scrapy.Field()
    novelMonthPopular = scrapy.Field()
    novelWeekPopular = scrapy.Field()
    novelCommentNum = scrapy.Field()
    novelAllComm = scrapy.Field()
    novelMonthComm = scrapy.Field()
    novelWeekComm = scrapy.Field()

