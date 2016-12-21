# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from crawlimg.items import *

class Newmovie(CrawlSpider):
    name='woyaogexing'
    allowed_domains = ["woyaogexing.com"]
    start_urls = ["http://www.woyaogexing.com/touxiang/weixin/"]
    def start_requests(self):
        urls=[
                'http://www.woyaogexing.com/touxiang/weixin/index.html',
                'http://www.woyaogexing.com/touxiang/weixin/index_2.html',
                'http://www.woyaogexing.com/touxiang/weixin/index_3.html',
                'http://www.woyaogexing.com/touxiang/weixin/index_4.html',
                'http://www.woyaogexing.com/touxiang/weixin/index_5.html',
                'http://www.woyaogexing.com/touxiang/weixin/index_6.html',
                'http://www.woyaogexing.com/touxiang/weixin/index_7.html',
                ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for url in response.xpath('//a[@class="img"]/@href').extract():
            url='http://www.woyaogexing.com'+url
            yield scrapy.Request(url=url,callback=self.parse_1)

    def parse_1(self,response):
        img_urls=[]
        for url in response.xpath('//img[@width="200"]/@src').extract():
            img_urls.append(url)
        yield CrawlimgItem(image_urls=img_urls)
