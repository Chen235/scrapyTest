import datetime

from scrapyProject.mongoItem import mongoItem

class Util(object):

    def _item(mainTitle, url, source):
        item = mongoItem()
        item['title'] = mainTitle.strip()
        item['url'] = url
        item['source'] = source
        item['date'] = datetime.datetime.now()
        return item

    def _parse(aTag,source):
        text = aTag.xpath("text()").extract_first()
        href = aTag.xpath("@href").extract_first()
        if (not href.endswith("/")) and (text!=None)  and (len(text) > 4):
            return Util._item(text,href,source)