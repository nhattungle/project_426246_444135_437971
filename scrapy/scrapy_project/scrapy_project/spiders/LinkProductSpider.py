import scrapy

class LinkProduct(scrapy.Item):
    productLink = scrapy.Field()


class LinkProductSpider(scrapy.Spider):
    name = 'link_product'
    allowed_domains = ['https://e-roberto.eu/']
    try:
         with open("link_pages.csv", "rt") as f:
             start_urls = [url.strip() for url in f.readlines()][1:]
    except:
         start_urls = []

    def parse(self, response):
        # xpath: get all a tags
        xpath = '//div[contains(@class, "image-zoom")]/a/@href'
        for link in response.xpath(xpath):
            linkProduct = LinkProduct()
            linkProduct['productLink'] = link.get()
            print(linkProduct['productLink'])
            yield linkProduct

#scrapy crawl link_product -o link_products.csv