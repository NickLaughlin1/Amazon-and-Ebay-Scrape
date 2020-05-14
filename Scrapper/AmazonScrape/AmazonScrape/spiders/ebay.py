# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from ..items import EbayscrapeItem
from ..GetUrl import Find_URL



class EbaySpider(scrapy.Spider):
    name = 'ebay'
    page_num = 1
    url = " "
    start_urls = ["https://www.ebay.com/"]
    def __init__(self):
        self.output = " "
        self.dict = {
            'Product Name' : [],
            'Product Price' : [],
            'Product Authorized' : [],
            'Product Usage' : [],
            'Prodcut Rating' : [],
            'Product Link' : [],
            'Product Image' : []
        }

    def parse(self, response):
        self.output = input("\n\n" + "What do you want the CSV file to be called (do not include .csv after name)?" + "\n") + ".csv" 
        EbaySpider.url = Find_URL("ebay")
        open(self.output, 'w').close()
        df = pd.DataFrame(self.dict)
        df.to_csv(self.output, index=False)
        yield scrapy.Request(EbaySpider.url, callback=self.parse_link)

    def parse_link(self, response):
        product_name = []
        product_price = []
        product_link = []
        product_img = []
        product_usage = []
        product_authorized = []
        product_rating = []

        print("Crawling page " + str(EbaySpider.page_num))
        print("URL: " + EbaySpider.url + "\n" + '-'*40 + "\n\n")

        results = response.xpath('//div/div/ul/li[contains(@class, "s-item" )]')
        #loops through all the listings on the page
        for product in results:
            items = EbayscrapeItem()
            name = product.css('.s-item__title::text').get()
            # Sponsored titles have a different class and some titles are bolded so both have to be checked
            if name == None:
                name = product.css('.s-item__title--has-tags::text').extract_first()
                if name == None:
                    name = product.css('.s-item__title .BOLD::text').extract_first()

            if name == 'New Listing':
                name = product.css('.s-item__title::text').extract()[1]
            # Adds the product information to an array
            product_name.append(name)
            product_price.append(product.css('.s-item__price::text').get())
            product_link.append(product.xpath('.//a[@class="s-item__link"]/@href').get())
            product_img.append(product.css('.s-item__image-img::attr(src)').get())
            product_usage.append(product.css('.SECONDARY_INFO::text').get())
            product_rating.append(product.css('.b-starrating .clipped::text').get())
            authorized = product.css('.s-item__authorized-seller .BOLD::text').get()
            # Checks to see if the seller is a authorized seller
            if authorized is not None:
                product_authorized.append(authorized)
            else:
                product_authorized.append("Not seller authorized")
            yield {
                'Product Name' : product_name,
                'Product Price' : product_price,
                'Product Authorized' : product_authorized,
                'Product Link' : product_link,
                'Product Usage' : product_usage,
                'Product Image' : product_img,
                'Product Rating' : product_rating
            }

        dict = {
            'Product Name' : product_name,
            'Product Price' : product_price,
            'Product Authorized' : product_authorized,
            'Product Usage' : product_usage,
            'Product Rating' : product_rating,
            'Product Link' : product_link,
            'Product Image' : product_img
        }
        # Writes all the information scraped into a csv file using pandas
        df = pd.DataFrame(dict)
        df.to_csv(self.output, mode='a', header=False, index=False)
        next_page = response.css('.pagination__next::attr(href)').extract_first()
        if next_page == None or str(next_page).endswith("#"):
            print("eBay items scraped successfully!" + "\n\n")
        else:
            EbaySpider.page_num += 1
            # call the parse function
            yield response.follow(next_page, callback = self.parse_link)

            
