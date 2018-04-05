# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand = scrapy.Field()
    pName = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()

class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comp_name = scrapy.Field()
    exp_rqr = scrapy.Field()
    #price = scrapy.Field()
    #size = scrapy.Field()
    
    '''
    
    class ProdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand = scrapy.Field()
    pName = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    
    
    
    brand = item.css('.productdescriptionbrand::text').extract_first()
            pName = item.css('.productdescriptionname::text').extract_first()
            price = item.css('.curprice::text').extract_first()
            size = item.css('.sizeDetail::text').extract_first()
    '''


