import scrapy

class LinkPage(scrapy.Item):
    page = scrapy.Field()


class LinkPageSpider(scrapy.Spider):
    name = 'link_page'
    allowed_domains = ['https://e-roberto.eu/']
    try:
         with open("link_categories.csv", "rt") as f:
             start_urls = [url.strip() for url in f.readlines()][1:]
    except:
         start_urls = []

    def parse(self, response):
        # xpath: get all a tags
        max_page = 1
        xpath = '//a[contains(@class, "page-number")]/text()'
        for link in response.xpath(xpath):
            max_page = max(int(link.get()), max_page)
       
        for p in range(1, max_page + 1):
            linkPage = LinkPage()
            linkPage['page'] = response.request.url + "page/"+str(p)
            print(linkPage['page'])
            yield linkPage

#scrapy crawl link_page -o link_pages.csv