# -*- coding: utf-8 -*-
import scrapy

class AppCrawlerItem(scrapy.Item):
    #Link = scrapy.Field()
    name = scrapy.Field()
    Price = scrapy.Field()
    Genre = scrapy.Field()
    Downloads = scrapy.Field()
    Rating = scrapy.Field()
    Review_number = scrapy.Field()
    Updated = scrapy.Field()
    Author = scrapy.Field()
    Version = scrapy.Field()
    
