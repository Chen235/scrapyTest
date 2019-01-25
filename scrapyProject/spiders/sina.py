from scrapy.spiders import CrawlSpider
from scrapyProject.common.util import Util

source = 'sina'
class SinaSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['https://finance.sina.com.cn/']

    def parse_start_url(self, response):
        print('----------爬取新浪财经网站信息-----------')

        newsH3As = response.css('.m-hdline a')
        for newsH3A in newsH3As:
            yield Util._parse(newsH3A, source)
        print('---------------重点信息完毕----------------')

        newsUlLiAs = response.css('.m-list a')
        for newsUlLiA in newsUlLiAs:
            yield Util._parse(newsUlLiA, source)
        print('---------------次级重点信息完毕----------------')


