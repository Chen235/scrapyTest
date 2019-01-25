from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapyProject.spiders.toutiao import ToutiaoSpider

process = CrawlerProcess(get_project_settings())
process.crawl(ToutiaoSpider)
process.start()
# cmdline.execute('scrapy crawl sina'.split())