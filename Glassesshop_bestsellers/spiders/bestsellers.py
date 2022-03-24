import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath("//div[@id='product-lists']/div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']")
        
        
        for product in products:
            yield{
                "name" : product.xpath("normalize-space(.//div[@class='p-title']/a[1]/text())").get(),
                "price" : product.xpath(".//div[@class='p-price'//span/text()").get(),
                "image_link" : response.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@src").get(),
                "product_url" : product.xpath(".//div[@class='p-title']/a[1]/@href").get()


            }


            # next_page = response.xpath("")

            # product_name = product.xpath("normalize-space(.//div[@class='p-title']/a[1]/text())").get()
            # product_price = product.xpath(".//div[@class='p-price'//span/text()").get()
            # product_url = product.xpath(".//div[@class='p-title']/a[1]/@href").get()
            # product_image_link = response.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@src").get()
