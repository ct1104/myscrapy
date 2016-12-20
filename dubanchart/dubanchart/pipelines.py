# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from collections import OrderedDict
class SortbyScorePipeline(object):
    def __init__(self):
        self.file=codecs.open('data_utf8.json','w',encoding='utf-8')
        self.itemlist=[]

    def process_item(self,item,spider):
        item['score']=float(item['score'])
        self.itemlist.append(item)
        return item

    def close_spider(self,spider):
        self.itemlist.sort(lambda x,y:-cmp(x['score'],y['score']))
        for item in self.itemlist:
            line=json.dumps(OrderedDict(item),ensure_ascii=False,sort_keys=False)+'\n'
            self.file.write(line)
        self.file.close()


class DubanchartPipeline(object):
    def __init__(self):
        self.file=codecs.open('data_utf8.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        line=json.dumps(OrderedDict(item),ensure_ascii=False,sort_keys=False)+'\n'
        self.file.write(line)
        return item

    def close_spider(self,spider):
        self.file.close()
