import os
import pymongo
import datetime
import hashlib
import logging as log

from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

checkFile = "isRunning.txt"

class MongoPipeline(object):

    def open_spider(self, spider):
        settings = get_project_settings();
        collDate = datetime.datetime.now().strftime('%Y%m%d')
        collName = settings['MONGODB_COLLECTION'] + collDate;
        self.mongoClient = pymongo.MongoClient(
            'mongodb://' + str(settings['MONGODB_HOST']) + ':' + str(settings['MONGODB_PORT']) + '/')
        self.mydb = self.mongoClient[settings['MONGODB_DB']]
        self.newsColl = self.mydb[collName]
        self.md5Coll = self.mydb[settings['MONGODB_MD5_COLL']]

        f = open(checkFile, "w")  # 创建一个文件，代表爬虫在运行中
        f.close()

    def close_spider(self, spider):
        self.mongoClient.close()
        isFileExsit = os.path.isfile(checkFile)
        if isFileExsit:
            os.remove(checkFile)

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            url = item['url']
            if url:
                md5Value = hashlib.md5(url.encode("utf8"))
                md5Str = md5Value.hexdigest()
                md5Query = {"md5": md5Str}
                md5Count = self.md5Coll.find(md5Query).count()
                if md5Count == 0:
                    self.newsColl.insert(dict(item))
                    self.md5Coll.insert(dict(md5Query))
            # log.msg("Question added to MongoDB database!",
            #         level=log.DEBUG, spider=spider)
        return item