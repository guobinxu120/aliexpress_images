# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from collections import OrderedDict
from datetime import datetime, timedelta
from scrapy.http import TextResponse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import requests, random, json
from scrapy.utils.project import get_project_settings

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class aliexpressSpider(Spider):
    name = "tmall_images"
    start_url = 'https://list.tmall.com/search_product.htm?q=%C4%D0%CA%BF%B3%C4%C9%C0%B3%A4%D0%E4%C9%CC%CE%F1&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton'
    domain1 = 'aliexpress.com'

    total_count = 0
    use_selenium = True

    # settings = get_project_settings()
    # # list_proxy = settings.get('PROXIES')
    # proxy = random.choice(list_proxy)

    def __init__(self, proxy_type=None, proxy_url=None, *args, **kwargs):
        super(aliexpressSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        # url = 'https://www.aliexpress.com/category/200001648/blouses-shirts.html'
        yield Request(self.start_url, self.parse,
                      meta={"next_count": 1,
                            'url': self.start_url})

    def parse(self, response):
        urls = response.xpath('//div[@id="J_ItemList"]/div/div/div/a/@href').extract()
        for url in urls:
            if 'https:' not in url:
                url = 'https:' + url

            yield Request(url, self.parse_detail)

            break

    def parse_detail(self, response):
        urls = response.xpath('//div[@id="J_ItemList"]/div/div/div/a/@href').extract()
        for url in urls:
            yield Request(url, self.parse)

            break