# -*- coding: utf-8 -*-
import json
import os
import re
from urllib import urlencode

import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from zhihuCrawl.items import  UserInfoItem, RelationItem
from scrapy.http import Request, FormRequest



class ZhihuComSpider(CrawlSpider):
    name = 'zhihu.com'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/tombkeeper']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    def __init__(self, *args, **kwargs):
        super(ZhihuComSpider, self).__init__(*args, **kwargs)
        self.xsrf = ''
        self.cookies = ''

# if os.path.exists('session.txt'):
#         with open('session.txt','rb') as f:
#             import pickle
#             self.cookies = pickle.load(f)
#             self.xsrf = self.cookies['_xsrf']
#             return [Request(
#             self.start_urls[0],
#             cookies=self.cookies,
#             meta={'cookiejar': 1},
#             callback=self.parse_user_info,
#             errback=self.parse_err,
#         )]
    def start_requests(self):

        #首先进入登录界面
        return [Request('https://www.zhihu.com/#signin',
                   callback=self.start_login,
                   meta={'cookiejar':1})
                ]

    def start_login(self,response):
        #开始登录
        self.xsrf = Selector(response).xpath(
            '//input[@name="_xsrf"]/@value'
        ).extract_first()
        return [FormRequest(
            'https://www.zhihu.com/login/phone_num',
            method='POST',
            meta={'cookiejar': response.meta['cookiejar']},
            formdata={
                '_xsrf': self.xsrf,
                'phone_num': 'xxxxxx',
                'password': 'xxxxxx',
                'captcha_type': 'cn'},
            callback=self.after_login
        )]



    def after_login(self,response):
        if json.loads(response.body)['msg'].encode('utf8') == "登录成功":
            self.logger.info(str(response.meta['cookiejar']))
            return [Request(
            self.start_urls[0],
            meta={'cookiejar':response.meta['cookiejar']},
            callback=self.parse_user_info,
            errback=self.parse_err,
        )]
        else:
            self.logger.error('登录失败')
            return

# if not os.path.exists('session.txt'):
#     with open('session.txt','wb') as f:
#         import pickle
#         cookies = response.request.headers['cookie']
#         cookieDict={}
#         for cookie in cookies.split(';'):
#             key,value = cookie[0:cookie.find('=')], cookie[cookie.find('=')+1:]
#             cookieDict[key]=value
#         pickle.dump(cookieDict,f)

    def parse_user_info(self,response):
        '''
        解析用户信息
        :param response:
        :return:
        '''

        user_id = os.path.split(response.url)[-1]
        user_image_url = response.xpath("//img[@class='Avatar Avatar--l']/@src").extract_first()
        name = response.xpath("//*[@class='title-section']/span/text() | //*[@class='title-section']/a/text()").extract_first()
        location = response.xpath("//*[@class='location item']/@title").extract_first()
        business = response.xpath("//*[@class='business item']/@title").extract_first()
        gender = response.xpath("//*[@class='item gender']/i/@class").extract_first()
        if gender and u"female" in gender:
            gender = u"female"
        else:
            gender = u"male"
        employment = response.xpath("//*[@class='employment item']/@title").extract_first()
        position = response.xpath("//*[@class='position item']/@title").extract_first()
        education = response.xpath("//*[@class='education item']/@title").extract_first()
        #//div[@class='Profile-followStatusValue']
        try:
            followees_num,followers_num = tuple(response.xpath("//div[@class='zm-profile-side-following zg-clear']/a[@class='item']/strong/text()").extract())
            relations_url = response.xpath("//*[@class='zm-profile-side-following zg-clear']/a/@href").extract()
        except Exception,e:
            followees_num,followers_num = tuple(response.xpath("//div[@class='Profile-followStatusValue']/text()").extract())
            relations_url =response.xpath("//a[@class='Profile-followStatus']/@href").extract()

        user_info_item = UserInfoItem(user_id=user_id,user_image_url=user_image_url,
                                      name=name,location=location,business=business,
                                      gender=gender,employment=employment,position=position,
                                      education=education,followees_num=int(followees_num),
                                      followers_num=int(followers_num))
        yield user_info_item
       # 关注我和我关注的人的列表的链接

        for url in relations_url:
            if u"followees" in url:
                relation_type = u"followees"
            else:
                relation_type = u"followers"
            yield Request(response.urljoin(url=url),
                          meta={
                              'user_id':user_id,
                              'relation_type':relation_type,
                                'cookiejar': response.meta['cookiejar'],
                              'dont_merge_cookies': True
                                },
                          errback=self.parse_err,
                          callback=self.parse_relation
                          )


    def parse_relation(self,response):
        '''
        解析和我有关系的人,这个只处理前20
        :param response:
        :return:
        '''
        user_id = response.meta['user_id']
        relation_type = response.meta['relation_type']
        relations_url = response.xpath("//*[@class='zh-general-list clearfix']/div/a/@href").extract()
        relations_id = [os.path.split(url)[-1] for url in  relations_url]
        yield RelationItem(user_id=user_id,
                           relation_type=relation_type,
                           relations_id=relations_id)
        #提出post所需的参数和和我有关系的人数
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        users_num = response.xpath("//*[@class='zm-profile-section-name']/text()").extract_first()
        users_num = int(re.search(r'\d+', users_num).group())if users_num else len(relations_url)
        #提取要post出去的参数
        # data-init="{"params": {"offset": 0, "order_by": "created", "hash_id": "fbbe3c439118fddec554b03734f9da99"}, "nodename": "ProfileFollowersListV2"}"
        data_init = response.xpath("//*[@class='zh-general-list clearfix']/@data-init").extract_first()
        try:
            nodename =json.loads(data_init)['nodename']
            params = json.loads(data_init)['params']
            post_url = 'https://www.zhihu.com/node/%s'% nodename


            #下面获取剩余的数据post
            if users_num > 20:
                params['offset'] = 20
                payload = {
                    'method':'next',
                    'params':params
                }
                post_header={
                    'Host': 'www.zhihu.com',
                    'Connection': 'keep-alive',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                    'X-Xsrftoken':self.xsrf
                }
                yield Request(url=post_url,method='POST',
                              headers=post_header,
                              body=urlencode(payload),
                              cookies=self.cookies,
                              meta={'user_id':user_id,
                                    'relation_type':relation_type,
                                    'offset':20,
                                    'payload':payload,
                                    'users_num':users_num,
                                    'cookiejar': response.meta['cookiejar']
                                    },
                              callback=self.parse_next_relation,
                              errback=self.parse_err,
                              priority=100
                              )
        except Exception,e:
            self.logger.warning('no second post--'+str(data_init)+'--'+str(e))


        for url in relations_url:
            yield Request(response.urljoin(url=url),
                          meta={'cookiejar': response.meta['cookiejar']},
                          callback=self.parse_user_info,
                          errback=self.parse_err)


    def parse_next_relation(self,response):
        '''
        解析和我有关的人的剩余部分
        :param response:
        :return:
        '''
        user_id = response.request.meta['user_id']
        relation_type = response.request.meta['relation_type']
        payload =  response.request.meta['payload']
        relations_id=[]



        offset = response.request.meta['offset']
        users_num = response.request.meta['users_num']
        body = json.loads(response.body)
        user_divs = body.get('msg', [])

        for user_div in user_divs:
            selector = Selector(text=user_div)

            user_url = selector.xpath('//a[@class="zm-item-link-avatar"]/@href').extract_first()
            relations_id.append(os.path.split(user_url)[-1])
            #发送请求
            yield Request(response.urljoin(url=user_url),
                          meta={'cookiejar': response.meta['cookiejar']},
                          callback=self.parse_user_info,
                          errback=self.parse_err)
        #捕获到的关系数据发送
        yield RelationItem(user_id=user_id,
                           relation_type=relation_type,
                           relations_id=relations_id)
        #判断是否还有更多的数据
        if offset + 20 < users_num:
            payload['params']['offset'] = offset+20
            more_post = response.request.copy()
            more_post = more_post.replace(
                body=urlencode(payload),
                meta={'user_id':user_id,
                        'relation_type':relation_type,
                        'offset':offset+20,
                        'users_num':users_num,
                        'cookiejar': response.meta['cookiejar']})
            yield more_post




    def parse_err(self,response):
        self.logger.error('crawl %s fail'%response.url)
