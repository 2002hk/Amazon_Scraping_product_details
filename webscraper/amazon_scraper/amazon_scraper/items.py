# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    brand=scrapy.Field()
    memory_storage_capacity=scrapy.Field()
    hardware_interface=scrapy.Field()
    features=scrapy.Field()
    write_speed=scrapy.Field()
    
