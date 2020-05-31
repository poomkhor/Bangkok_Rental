# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request 

# this is to cleanup string from the scraping 
def cleanup(input_string):
    if input_string:
        return re.sub(r'[\n]','',input_string).strip()

# initializing spider
class HipflatSpider(scrapy.Spider):
    name = 'hipflat'
    start_urls = ['https://www.hipflat.co.th/en/market/condo-bangkok-skik']

    # analyst the text in html or css; an act of parsing
    def parse(self, response):    
        districts = response.css('.directories__lists-element-name::attr(href)').getall()
        for district in districts:
            district_url = response.urljoin(district)    
            yield Request(district_url, callback=self.parse_condo)

    # second page 
    def parse_condo(self, response):
        condos = response.css('.directories__lists-element-name::attr(href)').getall() 
        for condo in condos:
            url = response.urljoin(condo)
            yield Request(url, callback=self.parse_rental)
    
    # condo page
    def parse_rental(self, response):
        condo_name = response.css('.project-header-name a::text').get()
        district = response.css('.breadcrumb li:nth-child(2) span::text').get()
        # rooms = response.css("div[id=listings-for-rent] .listing-row__cell-area span[data-type=area] .number::text").getall()
        for room in response.css('div[id=listings-for-rent] .listings-table__body .listing-row'):
            rental_rate = room.css('td:nth-child(2) .money .number::text').get()
            if rental_rate is None:
                continue
            
            items = {
                'condo' : condo_name,
                'district' : cleanup(district),
                'room_area' : room.css('td:nth-child(6) .value .number::text').get(),
                'rental_rate' : rental_rate
             }
            
            yield items

    