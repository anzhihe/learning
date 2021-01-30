#coding:utf-8
from pymongo import MongoClient
from pyspider.libs.base_handler import *

class Handler(BaseHandler):
    crawl_config = {
    }
    mongo = MongoStore()

    headers ={'User-Agent':	'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer':'http://www.doubanMovie.com/'}
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://movie.doubanMovie.com/tag/', headers = self.headers,callback=self.index_page,validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.tagCol>tbody>tr>td>a').items():
            self.crawl(each.attr.href, headers = self.headers,callback=self.list_page,validate_cert=False)

    def list_page(self,response):
        for each in response.doc('.pl2>a').items():
            self.crawl(each.attr.href, headers = self.headers,callback=self.detail_page,validate_cert=False)
        for each in response.doc('.next>a').items():
            self.crawl(each.attr.href, headers = self.headers,callback=self.list_page,validate_cert=False)


    @config(priority=2)
    def detail_page(self, response):
        title = response.doc('#content>h1>span[property="v:itemreviewed"]').text()
        time  = response.doc('#content>h1>span[class="year"]').text()
        director = response.doc('.attrs>a[rel="v:directedBy"]').text()
        actor=[]
        genre=[]
        for each in response.doc('a[rel="v:starring"]').items():
            actor.append(each.text())
        for each in response.doc('#info>span[property="v:genre"]').items():
            genre.append(each.text())

        rating = response.doc('.ll.rating_num').text()

        return {
            "url": response.url,
            "title": title,
            "time":time,
            "director":director,
            "actor":actor,
            "genre":genre,
            "rating":rating
        }
    def on_result(self, result):
        self.mongo.insert(result)
        super(Handler, self).on_result(result)

class MongoStore(object):

    def __init__(self):
    #连接mongo数据库,并把数据存储
        client = MongoClient()#'mongodb://localhost:27017/'///'localhost', 27017///'mongodb://tanteng:123456@localhost:27017/'
        db = client.douban
        self.movies = db.movies

    def insert(self,result):
        self.movies.insert(result)
