import scrapy
import json


class AlternativetoSpider(scrapy.Spider):
    name = 'alternativeto'
    allowed_domains = ['alternativeto.net']
    start_urls = ['https://alternativeto.net/software/android/']

    def parse(self, response):
        next_data = response.xpath('//script[@id="__NEXT_DATA__"]/text()')
        serialized = json.loads(next_data.get())
        totalPages = serialized['props']['pageProps']['pagingMeta']['totalPages']
        pageLinks = []
        for pageNumber in range(1, totalPages+1):
            pageLink = self.start_urls[0] + "?p=" + str(pageNumber)
            pageLinks.append(pageLink)
        yield from response.follow_all(pageLinks, callback=self.parseNextPages, dont_filter=True)

    def parseNextPages(self, response):
        next_data = response.xpath('//script[@id="__NEXT_DATA__"]/text()')
        serialized = json.loads(next_data.get())
        for item in serialized['props']['pageProps']['items']:
            yield {'name': item['name'], 'licenseModel': item['licenseModel']}
