#coding:utf-8
from APISpider.SpiderDataOutput import SpiderDataOutput
from APISpider.SpiderDownloader import SpiderDownloader
from APISpider.SpiderParser import SpiderParser


class SpiderMan(object):

    def __init__(self):
        self.downloader = SpiderDownloader()
        self.parser = SpiderParser()
        self.output = SpiderDataOutput()
    def crawl(self,root_url):
        content = self.downloader.download(root_url)
        for info in self.parser.get_kw_cat(content):
            print info
            cat_name = info['cat_name']
            detail_url = 'http://ts.kuwo.cn/service/getlist.v31.php?act=detail&id=%s'%info['id']
            content = self.downloader.download(detail_url)
            details = self.parser.get_kw_detail(content)
            print detail_url
            self.output.output_html(self.output.filepath,details)
        self.output.ouput_end(self.output.filepath)


if __name__ =="__main__":
    spider = SpiderMan()
    spider.crawl('http://ts.kuwo.cn/service/getlist.v31.php?act=cat&id=50')



