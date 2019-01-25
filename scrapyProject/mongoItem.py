from scrapy.item import Item, Field


class mongoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    title = Field()
    url = Field()
    date = Field()
    source = Field()

