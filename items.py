from scrapy.item import Item, Field

class TeluSampleItem(Item):
    title = Field()
    body = Field()
