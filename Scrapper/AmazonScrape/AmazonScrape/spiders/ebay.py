# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from ..items import EbayscrapeItem
from ..GetUrl import Find_URL



class EbaySpider(scrapy.Spider):
    name = 'ebay'
    page_num = 2
    output = input("What do you want the CSV file to be called (do not include .csv after name)?" + "\n") + ".csv" 
    url = Find_URL("ebay")
    start_urls = [url]
    def __init__(self):
        open(self.output, 'w').close()
        dict = {
            'Product Name' : [],
            'Product Price' : [],
            'Product Link' : [],
            'Product Image' : []
        }
        df = pd.DataFrame(dict)
        df.to_csv(self.output, index=False)

    def parse(self, response):
        product_name = []
        product_price = []
        product_link = []
        product_img = []

        results = response.xpath('//div/div/ul/li[contains(@class, "s-item" )]')
        #loops through all the listings on the page
        for product in results:
            items = EbayscrapeItem()
            product_name.append(product.css('s-item_title::text').get())
            print(product_name)
