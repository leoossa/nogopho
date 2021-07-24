import scrapy


class LineageosSpider(scrapy.Spider):
    name = 'lineageos'
    allowed_domains = ['https://wiki.lineageos.org/devices/']
    start_urls = ['http://https://wiki.lineageos.org/devices//']

    def parse(self, response):
        pass
