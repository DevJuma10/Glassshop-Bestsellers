import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['https://www.glassesshop.com']
    start_urls = ['https://https://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        pass
