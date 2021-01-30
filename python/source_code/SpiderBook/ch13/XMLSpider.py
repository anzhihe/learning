#coding:utf-8
from scrapy.spiders import XMLFeedSpider


class XMLSpider(XMLFeedSpider):

    name = 'xmlspider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://feed.cnblogs.com/blog/u/269038/rss']
    iterator = 'html'  # This is actually unnecessary, since it's the default value
    itertag = 'entry'

    def adapt_response(self,response):
       return response

    def parse_node(self, response, node):
        print node.xpath('id/text()').extract()[0]
        print node.xpath('title/text()').extract()[0]
        print node.xpath('summary/text()').extract()[0]
