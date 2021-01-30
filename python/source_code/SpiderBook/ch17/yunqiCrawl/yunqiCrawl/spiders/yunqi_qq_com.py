# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from yunqiCrawl.items import YunqiBookListItem, YunqiBookDetailItem
from scrapy.http import Request

class YunqiQqComSpider(CrawlSpider):
    name = 'yunqi.qq.com'
    allowed_domains = ['yunqi.qq.com']
    start_urls = ['http://yunqi.qq.com/bk/so2/n30p1']

    rules = (
        Rule(LinkExtractor(allow=r'/bk/so2/n30p\d+'), callback='parse_book_list', follow=True),
    )

    def parse_book_list(self,response):
        books = response.xpath(".//div[@class='book']")
        for book in books:
            novelImageUrl = book.xpath("./a/img/@src").extract_first()
            novelId = book.xpath("./div[@class='book_info']/h3/a/@id").extract_first()
            novelName =book.xpath("./div[@class='book_info']/h3/a/text()").extract_first()
            novelLink = book.xpath("./div[@class='book_info']/h3/a/@href").extract_first()
            novelInfos = book.xpath("./div[@class='book_info']/dl/dd[@class='w_auth']")
            if len(novelInfos)>4:
                novelAuthor = novelInfos[0].xpath('./a/text()').extract_first()
                novelType = novelInfos[1].xpath('./a/text()').extract_first()
                novelStatus = novelInfos[2].xpath('./text()').extract_first()
                novelUpdateTime = novelInfos[3].xpath('./text()').extract_first()
                novelWords  = novelInfos[4].xpath('./text()').extract_first()
            else:
                novelAuthor=''
                novelType =''
                novelStatus=''
                novelUpdateTime=''
                novelWords=0
            bookListItem = YunqiBookListItem(novelId=novelId,novelName=novelName,
                              novelLink=novelLink,novelAuthor=novelAuthor,
                              novelType=novelType,novelStatus=novelStatus,
                              novelUpdateTime=novelUpdateTime,novelWords=novelWords,
                              novelImageUrl=novelImageUrl)
            yield bookListItem
            request = scrapy.Request(url=novelLink,callback=self.parse_book_detail)
            request.meta['novelId'] = novelId
            yield request




    def parse_book_detail(self,response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        novelId = response.meta['novelId']
        novelLabel = response.xpath("//div[@class='tags']/text()").extract_first()

        novelAllClick = response.xpath(".//*[@id='novelInfo']/table/tr[2]/td[1]/text()").extract_first()
        novelAllPopular = response.xpath(".//*[@id='novelInfo']/table/tr[2]/td[2]/text()").extract_first()
        novelAllComm = response.xpath(".//*[@id='novelInfo']/table/tr[2]/td[3]/text()").extract_first()

        novelMonthClick = response.xpath(".//*[@id='novelInfo']/table/tr[3]/td[1]/text()").extract_first()
        novelMonthPopular = response.xpath(".//*[@id='novelInfo']/table/tr[3]/td[2]/text()").extract_first()
        novelMonthComm = response.xpath(".//*[@id='novelInfo']/table/tr[3]/td[3]/text()").extract_first()

        novelWeekClick = response.xpath(".//*[@id='novelInfo']/table/tr[4]/td[1]/text()").extract_first()
        novelWeekPopular = response.xpath(".//*[@id='novelInfo']/table/tr[4]/td[2]/text()").extract_first()
        novelWeekComm = response.xpath(".//*[@id='novelInfo']/table/tr[4]/td[3]/text()").extract_first()
        novelCommentNum = response.xpath(".//*[@id='novelInfo_commentCount']/text()").extract_first()
        bookDetailItem = YunqiBookDetailItem(novelId=novelId,novelLabel=novelLabel,novelAllClick=novelAllClick,novelAllPopular=novelAllPopular,
                            novelAllComm=novelAllComm,novelMonthClick=novelMonthClick,novelMonthPopular=novelMonthPopular,
                            novelMonthComm=novelMonthComm,novelWeekClick=novelWeekClick,novelWeekPopular=novelWeekPopular,
                            novelWeekComm=novelWeekComm,novelCommentNum=novelCommentNum)
        yield bookDetailItem



