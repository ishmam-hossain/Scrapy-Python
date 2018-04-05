# -*- coding: utf-8 -*-
import scrapy
from ..items import JobItem


class QuotesSpider(scrapy.Spider):
    name = 'bdjobs'
    allowed_domains = ['bdjobs.com/']
    start_urls = ['http://jobs.bdjobs.com/jobsearch.asp?fcatId=8']
    
    

    def parse(self, response):
        job_list = response.css('.norm-jobs-wrapper')

        print('---------------')
        for item in job_list:
            comp_name = item.css('.comp-name-text::text').extract_first()
            #job_name = item.css('.job-title-text::text').extract_first()
            exp_rqr = item.css('.exp-text-d::text').extract_first()
            #dead_line = item.css('.dead-text::text').extract_first() 
            #print(comp_name , exp_rqr)
            print(comp_name.strip() + '  ---  ' + exp_rqr.strip())
            
            itemClass = JobItem()
            
            itemClass['comp_name'] = comp_name.strip()
            itemClass['exp_rqr'] = exp_rqr.strip()

            
            yield itemClass

   