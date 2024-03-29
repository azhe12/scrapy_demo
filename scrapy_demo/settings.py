# Scrapy settings for scrapy_demo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['scrapy_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_demo.spiders'
DNSCACHE_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_demo (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0'
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_demo.random_user_agent.RandomUserAgentMiddleware': 400,
      'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',)
