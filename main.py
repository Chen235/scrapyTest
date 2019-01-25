from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapyProject.spiders.sina import SinaSpider
from scrapyProject.spiders.caixin import CaiXinSpider
from scrapyProject.spiders.caijing import CaiJingSpider

process = CrawlerProcess(get_project_settings())
process.crawl(SinaSpider)
process.crawl(CaiXinSpider)
process.crawl(CaiJingSpider)
process.start()
# cmdline.execute('scrapy crawl sina'.split())