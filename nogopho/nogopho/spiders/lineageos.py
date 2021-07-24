import scrapy


class LineageosSpider(scrapy.Spider):
    name = 'lineageos'
    allowed_domains = ['wiki.lineageos.org']
    start_urls = ['https://wiki.lineageos.org/devices/']

    def parse(self, response):
        devices_links = response.css('th[scope="row"] a')
        yield from response.follow_all(devices_links, self.parse_device)

    def parse_device(self, response):
        # First table row (<tr>) is name of the device
        name = response.css('table.deviceinfo tr th::text').get()
        released = response.xpath(
            '//tr[th[contains(text(), "Released")]]//td/text()').getall()
        released = [release.strip()
                    for release in released]  # Strip newlines and spaces
        supported_versions = response.xpath(
            '//tr[th[contains(text(), "versions")]]//li/text()').getall()
        # Last table row <tr> is <ul><li>...</ul> for supported versions if there are supported versions
        # if it is not maintained - last table row is 'Battery' and there's no <ul> and no <li>
        if len(supported_versions) == 0:
            supported_versions = 'unmaintained'

        yield{'name': name, 'supported_versions': supported_versions, 'released': released}
