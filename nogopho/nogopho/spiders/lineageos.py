import scrapy


class LineageosSpider(scrapy.Spider):
    name = 'lineageos'
    allowed_domains = ['wiki.lineageos.org']
    start_urls = ['https://wiki.lineageos.org/devices/']

    def parse(self, response):
        print("HTTP Status Code:", response.status)
        devices = response.css('th[scope="row"]')
        for device in devices:
            smartphone = device.css('a')
            name = smartphone.css('a::text').get()
            link = smartphone.css('a::attr(href)').get()
            print("Device:", name, "link", link)
        pass
