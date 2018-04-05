# -*- coding: utf-8 -*-
import scrapy
from ..items import ProdItem

class QuotesSpider(scrapy.Spider):
    name = 'sports'
    allowed_domains = ['sportsdirect.com/']
    start_urls = ['https://www.sportsdirect.com/running/running-clothes/mens-running-clothes/mens-running-jackets']
    
    

    def parse(self, response):
        prod = response.css('.s-productthumbbox')
        
        for item in prod:
            brand = item.css('.productdescriptionbrand::text').extract_first()
            pName = item.css('.productdescriptionname::text').extract_first()
            price = item.css('.curprice::text').extract_first()
            size = item.css('.sizeDetail::text').extract_first()
            
            itemClass = ProdItem()
            
            itemClass['brand'] = brand
            itemClass['pName'] = pName
            itemClass['price'] = price
            itemClass['size'] = size
            
            
            yield itemClass


