# -*- coding: utf-8 -*-
import scrapy


class EbaySpider(scrapy.Spider):
    name = 'ebay'
    output = input("What do you want the CSV file to be called (do not include .csv after name)?" + "\n") + ".csv"
    url = Find_URL("ebay")
    start_urls = [url]
    allowed_domains = ['ebay.com']
    start_urls = ['http://ebay.com/']

    def parse(self, response):
        pass
