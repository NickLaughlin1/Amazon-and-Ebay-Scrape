# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# Used code found from https://stackoverflow.com/questions/14390945/suppress-scrapy-item-printed-in-logs-after-pipeline
import logging

logging.getLogger('scrapy.core.scraper').addFilter(
    lambda x: not x.getMessage().startswith('Scraped from'))