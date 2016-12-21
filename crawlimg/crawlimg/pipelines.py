# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class CrawlimgPipeline(object):
    def __init__(self):
        self.file=open('url.txt','w')
    def process_item(self, item, spider):
        line=json.dumps(dict(item))+'\n'
        self.file.write(line)
        return item
    def close_spider(self,spider):
        self.file.close()
