from scrapy.spider import Spider

class GuokrSpider(Spider):
    name = "guokr"
    allowed_domains = ["guokr.com"]
    start_urls = (
        'http://www.guokr.com/',
        )

    def parse(self, response):
        with open('test.html', 'w') as f:
            f.write(response.body)



