# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy import log

class XiaomiAppstoreCrawlerPipeline(object):
    def __init__(self):
        #self.file = open('appstore.data', 'wb')
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]


    def process_item(self, item, spider):
        #import pudb; pu.db
        #val = "{0}\t{1}\t{2}\t{3}\t".format(item['appid'], item['title'], item['recommended'], item['intro'])
        #self.file.write('--------------------------------------------\n')
        #self.file.write(val)
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("new app added to MongoDB database!",
                    level=log.DEBUG, spider=spider)

        return item
