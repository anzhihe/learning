from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from cnblogSpider.spiders.cnblogs_spider import CnblogsSpider

if __name__=='__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('cnblogs')
    process.start()
