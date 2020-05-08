# -*- coding: utf-8 -*-
import scrapy


class EbaySpider(scrapy.Spider):
    name = 'ebay'
    allowed_domains = ['ebay.com']
    start_urls = ['http://ebay.com/']

    def parse(self, response):
        pass
