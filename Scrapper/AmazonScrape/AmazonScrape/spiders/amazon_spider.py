# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from selenium import webdriver
from ..items import AmazonscrapeItem
from ..GetUrl import Find_URL

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    # The user gets to name the file
    output = input("What do you want the CSV file to be called (do not include .csv after name)?" + "\n") + ".csv"
    url = Find_URL()
    start_urls = [url]

    def __init__(self):
        open(self.output, 'w').close()


    def parse(self, response):
        product_name = []
        product_image = []
        product_price = []
        product_rating = []
        for product in response.css('.s-result-item'):
            items = AmazonscrapeItem()
            product_name.append(product.css('.a-color-base.a-text-normal::text').get())
            product_price.append(product.css('.a-offscreen::text').get())
            product_image.append(product.css('.s-image::attr(src)').get())
            product_rating.append(product.css('.aok-align-bottom').css('::text').extract())
            yield {
                'product_name' : product_name,
                'product_price' : product_price,
                'product_rating' : product_rating,
                'product_image' : product_image
            }
        dict = {
            'Product Name' : product_name, 
            'Product Price' : product_price,
            'Product Rating' : product_rating,
            'Product Image Links' : product_image
            }
        df = pd.DataFrame(dict)
        df.to_csv(self.output, mode='a', header=False)

        # Iterates through each Amazon Page
        amazon_num = response.css('.a-normal a::text').extract()
        next_page = ""
        # Gets the next pages url
        for num in amazon_num:
            if AmazonSpiderSpider.page_number == int(num):
                # Makes sure a previous page isn't selected
                if AmazonSpiderSpider.page_number == 2:
                    next_page = response.css('.a-normal a::attr(href)')[0].extract()
                else:
                    next_page = response.css('.a-normal a::attr(href)')[len(amazon_num) - 1].extract()
                    if next_page is None:
                        AmazonSpiderSpider.last_page = True
        AmazonSpiderSpider.page_number += 1
        yield response.follow(next_page, callback = self.parse)
    