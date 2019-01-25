from pandas import json
from scrapy.spiders import CrawlSpider
from scrapyProject.common.util import Util

source = 'toutiao'
class ToutiaoSpider(CrawlSpider):
    name = 'toutiao'
    allowed_domains = ['toutiao.com']
    start_urls = ['https://www.toutiao.com/api/pc/feed/?category=news_finance']

    def parse_start_url(self, response):
        print('----------爬取今日头条信息-----------')
        jsonResult = json.loads(response.text)
        dataArr = jsonResult['data']
        for data in dataArr:
            title = data['title']
            url = data['source_url']
            if "http" not in url:
                url = "https://www.toutiao.com"+url
                yield Util._item(title,url,source)

