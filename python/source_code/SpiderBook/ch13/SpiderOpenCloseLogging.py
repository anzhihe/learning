import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured

logger = logging.getLogger(__name__)

class SpiderOpenCloseLogging(object):

    def __init__(self, item_count):
        self.item_count = item_count

        self.items_scraped = 0

    @classmethod
    def from_crawler(cls, crawler):
        #首先检查一下是否存在相应的配置，如果不存在则抛出NotConfigured异常
        if not crawler.settings.getbool('MYEXT_ENABLED'):

            raise NotConfigured

        ## 从setting中获取MYEXT_ITEMCOUNT的值

        item_count = crawler.settings.getint('MYEXT_ITEMCOUNT', 1000)

        # 初始化扩展实例
        ext = cls(item_count)

        # 将扩展中的spider_opened，spider_closed和item_scraped连接到相应信号处，进行触发。

        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)

        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)

        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)

        ##扩展实例返回
        return ext

    def spider_opened(self, spider):
        logger.info("opened spider %s", spider.name)

    def spider_closed(self, spider):
        logger.info("closed spider %s", spider.name)

    def item_scraped(self, item, spider):
        self.items_scraped += 1
        if self.items_scraped % self.item_count == 0:
            logger.info("scraped %d items", self.items_scraped)
