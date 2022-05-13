# set limit number of products to be scraped
limit = True
number_of_limit = 100
#############################################

# https://www.zyte.com/blog/handling-javascript-in-scrapy-with-splash/

# Install Docker Desktop: https://docs.docker.com/desktop/windows/install/
# Linux-kernel: https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package
# Install linux: user: wne, password: 123456
# Rundocker: & "C:\Program Files\Docker\Docker\DockerCli.exe" -SwitchDaemon

# https://github.com/scrapy-plugins/scrapy-splash
# pip install scrapy-splash
# docker pull scrapinghub/splash
# docker run -p 8050:8050 scrapinghub/splash
# docker pull scrapinghub/splash
# docker run -p 8050:8050 scrapinghub/splash

# $ pip install scrapy scrapy-splash
# https://stackoverflow.com/questions/39684974/docker-for-windows-error-hardware-assisted-virtualization-and-data-execution-p

import scrapy
from scrapy_splash import SplashRequest 

class Product(scrapy.Item):
    product_title = scrapy.Field()
    price_net = scrapy.Field()
    price_gross = scrapy.Field()
    quantity_in_stock = scrapy.Field()
    number_of_product_in_a_package = scrapy.Field()
    size = scrapy.Field()
    status = scrapy.Field()
    category = scrapy.Field()
    product_url = scrapy.Field()
    image_url = scrapy.Field()

class ProductDetailSpider(scrapy.Spider):
    name = 'product_detail'
    allowed_domains = ['https://e-roberto.eu/']
    try:
         with open("link_products.csv", "rt") as f:
            if(limit):
                # get limit number of products to be scraped
                start_urls = [url.strip() for url in f.readlines()][1:number_of_limit]
            else:
                start_urls = [url.strip() for url in f.readlines()][1:]
    except:
         start_urls = []

    def start_requests(self): 
        for url in self.start_urls: 
            yield SplashRequest(url, self.parse, 
                endpoint='render.html', 
                args={'wait': 0.5}, 
        ) 

    def parse(self, response):
        product = Product()
       
        # xpath: get all h1 tags
        try:
            xpath = '//h1[contains(@class, "product-title")]/text()'
            product_title = response.xpath(xpath).get()
            product_title = (product_title.rstrip()).lstrip()
            product['product_title'] = product_title
        except:
            product['product_title'] = ''

        # xpath: get price net
        try:
            xpath = '//span[contains(@id, "gianet")]/text()'
            product['price_net'] = response.xpath(xpath).get()
        except:
            product['price_net'] = 0

        # xpath: get price gross
        try:         
            xpath = '//span[contains(@id, "giabrut")]/text()'
            product['price_gross'] = response.xpath(xpath).get()
        except:
            product['price_gross'] = 0

        # xpath: get quantity in stock
        try:
            xpath = '//p[contains(@class, "stock in-stock")]/text()'
            array_quantity_in_stock = (response.xpath(xpath).get()).split(" ", 1)
            product['quantity_in_stock'] = array_quantity_in_stock[0]
        except:
            product['quantity_in_stock'] = 0

        # xpath: get number of product in a package
        try:
            xpath = '//span[contains(@id, "paczka")]/text()'
            product['number_of_product_in_a_package'] = response.xpath(xpath).get()
        except:
            product['number_of_product_in_a_package'] = 0

        # xpath: get size
        try:
            xpath = xpath = '//span[contains(@id, "gianet")]/following-sibling::*[3]/text()'
            product['size'] = response.xpath(xpath).get()
        except:
            product['size'] = ''

        # xpath: get status
        try:
            xpath = '//span[@id="XXC"]/following-sibling::*[2]/text()'
            product['status'] = response.xpath(xpath).get()
        except:
            product['status'] = ''

        # xpath: get category
        try:
            xpath = '//nav[@class="woocommerce-breadcrumb breadcrumbs uppercase"]/a[last()]/text()'
            product['category'] = response.xpath(xpath).get()
        except:
            product['category'] = ''

        # xpath: get product url
        try:
            # product['product_url'] = response.request.url
            product['product_url'] = "https://e-roberto.eu/sklep/{0}/".format((product_title.replace(" ", "-")).lower())
        except:
            product['product_url'] = ''

        # xpath: get image url
        try:
            xpath = '//img[contains(@class, "wp-post-image")]/@src'
            product['image_url'] = response.xpath(xpath).get()
        except:
            product['image_url'] = ''

        yield product

#scrapy crawl product_detail -o product_details.csv