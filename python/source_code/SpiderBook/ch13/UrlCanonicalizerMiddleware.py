from scrapy.http import Request
from scrapy.utils.url import canonicalize_url

class UrlCanonicalizerMiddleware(object):
    def process_spider_output(self, response, result, spider):
        for r in result:
            if isinstance(r, Request):
                curl = canonicalize_url(r.url)
                if curl != r.url:
                    r = r.replace(url=curl)
            yield r
