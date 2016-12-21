import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from crawlimg.items import *

class Newmovie(CrawlSpider):
    name='woyaogexing'
    allowed_domains = ["woyaogexing.com"]
    start_urls = ["http://www.woyaogexing.com/touxiang/weixin/"]
    rules = [
            Rule(sle(allow=("/touxiang/weixin/2016/\d{6}.html$")),callback='parse_1'),
            ]
    def parse_1(self,response):
        img_urls=[]
        for url in response.xpath('//img[@width="200"]/@src').extract():
            img_urls.append(url)
        yield CrawlimgItem(image_urls=img_urls)


