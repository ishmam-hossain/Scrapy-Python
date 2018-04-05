# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['sportsdirect.com/']
    start_urls = ['https://www.sportsdirect.com/football/football-boots/Puma-Football-Boots?promo_name=ftb-lp2018']
    
    

    def parse(self, response):
        print(response)
