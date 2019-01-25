from scrapy.spiders import CrawlSpider
from scrapyProject.common.util import Util

source = 'caixin'
class CaiXinSpider(CrawlSpider):
    name = 'caixin'
    allowed_domains = ['caixin.com']
    start_urls = ['http://www.caixin.com/']

    def parse_start_url(self, response):
        print('----------爬取财新网信息-----------')

        toutiaoNews = response.css(".toutiao_box .demolNews a")
        for toutiaoNew in toutiaoNews:
            yield Util._parse(toutiaoNew,source)
        print('---------------重点信息完毕----------------')
        #
        scrollNews = response.css(".scrollnews li a")
        for scrollNew in scrollNews:
            yield Util._parse(scrollNew, source)
        print('---------------滚动信息完毕----------------')

        listNews = response.css(".news_list p a")
        for listNew in listNews:
            yield Util._parse(listNew, source)
        print('---------------列表信息完毕----------------')

        guandianNews = response.css(".guandian_box p a")
        for guandianNew in guandianNews:
            yield Util._parse(guandianNew, source)
        print('---------------观点信息完毕----------------')

        topNews = response.css(".top10 dd a")
        for topNew in topNews:
            yield Util._parse(topNew, source)
        print('---------------Top信息完毕----------------')
