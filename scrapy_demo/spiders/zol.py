from scrapy.spider import Spider

class ZolSpider(Spider):
    name = "zol"
    allowed_domains = ["desk.zol.com.cn"]
    start_urls = (
        'http://www.desk.zol.com.cn/',
        )

    def parse(self, response):
        pass 
