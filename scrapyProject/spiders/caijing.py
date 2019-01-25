from scrapy.spiders import CrawlSpider
from scrapyProject.common.util import Util

source = 'caijing';
class CaiJingSpider(CrawlSpider):
    name = 'caijing'
    allowed_domains = ['caijing.com.cn']
    start_urls = ['http://www.caijing.com.cn/']

    def parse_start_url(self, response):
        print('----------爬取财经网信息-----------')

        toutiaoNews = response.css(".fir_jrtt a")
        for toutiaoNew in toutiaoNews:
            yield Util._parse(toutiaoNew,source)
        print('---------------头条信息完毕----------------')

        marqNews = response.css(".marq_ul a")
        for marqNew in marqNews:
            yield Util._parse(marqNew, source)
        print('---------------滚动信息完毕----------------')

        yaowenNews = response.css(".yaowen_ul a")
        for yaowenNew in yaowenNews:
            yield Util._parse(yaowenNew, source)
        print('---------------要闻信息完毕----------------')

        wzphNews = response.css(".wzph_main a")
        for wzphNew in wzphNews:
            yield Util._parse(wzphNew, source)
        print('---------------排行信息完毕----------------')
