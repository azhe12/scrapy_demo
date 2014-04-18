#encoding=utf-8
"""
user-agent中间件
使用setting.py中随机user-agent代替默认的user-agent
"""

from scrapy_demo.settings import USER_AGENTS
import random

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENTS)
        print "azhe: %s" % ua
        if ua:
            request.headers.setdefault('User-Agent', ua)

