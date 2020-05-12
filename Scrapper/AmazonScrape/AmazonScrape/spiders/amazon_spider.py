# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from ..items import AmazonscrapeItem
from ..GetUrl import Find_URL

class AmazonSpiderSpider(scrapy.Spider):
    
    name = 'amazon'
    page_number = 2
    start_urls = ["https://www.amazon.com/"]
    def __init__(self):
        self.output = " "
        self.dict = {
            'Poduct Name' : [],
            'Product Price' : [],
            'Product Rating' : [],
            'Product Link' : [],
            'Product Image' : []
        }

    def parse(self, response):
        self.output = input("What do you want the CSV file to be called (do not include .csv after name)?" + "\n") + ".csv"
        url = Find_URL("amazon")
        open(self.output, 'w').close()
        df = pd.DataFrame(self.dict)
        df.to_csv(self.output, index=False)
        yield scrapy.Request(url, callback=self.parse_link)

    def parse_link(self, response):
        product_name = []
        product_image = []
        product_price = []
        product_rating = []
        product_link = []

        # Loops through all the listings on the page
        for product in response.css('.s-result-item'):
            items = AmazonscrapeItem()
            product_name.append(product.css('.a-color-base.a-text-normal::text').get())
            product_price.append(product.css('.a-offscreen::text').get())
            product_image.append(product.css('.s-image::attr(src)').get())
            if product.css('.a-text-normal::attr(href)').get() is not None:
                product_link.append("https://www.amazon.com" + product.css('.a-text-normal::attr(href)').get())
            else:
                product_link.append("No link")
            product_rating.append(product.css('.aok-align-bottom').css('::text').extract())
            yield {
                'product_name' : product_name,
                'product_price' : product_price,
                'product_rating' : product_rating,
                'product_link' : product_link,
                'product_image' : product_image
            }
        # Dictionary that has all the information from each listing that will be used in the csv file
        dict = {
            'Product Name' : product_name, 
            'Product Price' : product_price,
            'Product Rating' : product_rating,
            'Product Link' : product_link,
            'Product Image Links' : product_image
            }
        df = pd.DataFrame(dict)
        df.to_csv(self.output, mode='a', header=False, index=False)  # write to the csv file without overwriting the data each time

        # Gets the available page numbers
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
        # call the parse function
        yield response.follow(next_page, callback = self.parse_link)

    