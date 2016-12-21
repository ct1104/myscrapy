import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from filedownload.items import *
class MySpider(CrawlSpider):
    name = 'filedownload'
    allowed_domains = ['networkradius.com']
    start_urls = ['http://networkradius.com/freeradius-documentation/']
    def parse(self,response):
        urls=[]
        for url in response.xpath('//a/@href').re('.*\.pdf$'):
            urls.append('http://networkradius.com'+url)
        yield FiledownloadItem(file_urls=urls)
