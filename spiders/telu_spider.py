from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from telu_sample.items import TeluSampleItem

class MySpider(BaseSpider):
    name = "telu"
    allowed_domains = ["telkomuniversity.ac.id"]
    start_urls = ["http://telkomuniversity.ac.id/academic/computational-science"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        content = hxs.xpath("//div[@class='entry-content']")
        items = []
        for content in content:
            item = TeluSampleItem()
            item["title"] = content.select("div/text()").extract()
            item["body"] = content.select("p/text()").extract()
            items.append(item)
        return items
