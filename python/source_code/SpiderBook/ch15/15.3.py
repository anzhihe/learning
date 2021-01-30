#coding:utf-8
from scrapy.dupefilters import RFPDupeFilter
class URLFilter(RFPDupeFilter):
      """根据url过滤"""
      def __init__(self, path=None,debug=False):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path)
      def request_seen(self, request):
        if request.url in self.urls_seen:
              return True
        else:
              self.urls_seen.add(request.url)

'''
from scrapy.dupefilters import RFPDupeFilter
from w3lib.util.url import canonicalize_url
class URLSha1Filter(RFPDupeFilter):
      """根据urlsha1过滤"""
      def __init__(self, path=None,debug=False):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path)
      def request_seen(self, request):
		fp = hashlib.sha1()
		fp.update(canonicalize_url(request.url))
		url_sha1 = fp.hexdigest()
        if url_sha1 in self.urls_seen:
              return True
        else:
              self.urls_seen.add(url_sha1)

'''

'''
class URLBloomFilter(RFPDupeFilter):
      """根据urlhash_bloom过滤"""
      def __init__(self, path=None,debug=False):
        self.urls_sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
        RFPDupeFilter.__init__(self, path)

      def request_seen(self, request):
        fp = hashlib.sha1()
        fp.update(canonicalize_url(request.url))
        url_sha1 = fp.hexdigest()
        if url_sha1 in self.urls_sbf:
              return True
        else:
              self.urls_sbf.add(url_sha1)

'''