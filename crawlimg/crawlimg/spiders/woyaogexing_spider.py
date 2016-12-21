import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from dubanchart.items import DubanchartItem

class Newmovie(CrawlSpider):
    name='woyaogexing'
    allowed_domains = ["woyaogexing.com"]
    start_urls = ["http://www.woyaogexing.com/touxiang/weixin/"]
    rules = [
            Rule(sle(allow=("/subject/\d+/")), callback='parse_1'),
            ]
    def parse_1(self,response):
        mitem=DubanchartItem()
        mitem['moviename']=response.xpath('//*[@id="content"]/h1/span[1]')[0].xpath('./text()').extract()[0]
        mitem['score']=response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong')[0].xpath('./text()').extract()[0]
        yield mitem


