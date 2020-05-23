# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request 

def cleanup(input_string):
    if input_string:
        return re.sub(r'[\n]','',input_string).strip()

class HipflatSpider(scrapy.Spider):
    name = 'hipflat'
    start_urls = ['https://www.hipflat.co.th/en/market/condo-bangkok-skik']

    def parse(self, response):
        # district = response.css('.directories__lists-element-name::attr(href)').get()
        # district_url = response.urljoin(district)    
        # yield Request(district_url, callback=self.parse_condo)
    
        districts = response.css('.directories__lists-element-name::attr(href)').getall()
        # district_names = response.css('.directories__lists-element-name::text').getall()
        for district in districts:
            district_url = response.urljoin(district)    
            yield Request(district_url, callback=self.parse_condo)
    
    def parse_condo(self, response):
        # condo = response.css('.directories__lists-element-name::attr(href)').get()
        # url = response.urljoin(condo)
        # yield Request(url, callback=self.parse_rental)

        condos = response.css('.directories__lists-element-name::attr(href)').getall() 
        for condo in condos:
            url = response.urljoin(condo)
            yield Request(url, callback=self.parse_rental)

    def parse_rental(self, response):
        condo_name = response.css('.project-header-name a::text').get()
        district = response.css('.breadcrumb li:nth-child(2) span::text').get()
        # rooms = response.css("div[id=listings-for-rent] .listing-row__cell-area span[data-type=area] .number::text").getall()
        for room in response.css('tbody > tr'):
            rental_rate = response.css("div[id=listings-for-rent] .listing-row__primary .money .number::text").get()
            if rental_rate is None:
                continue

            items = {
                'condo' : condo_name,
                'district' : cleanup(district),
                'room_area' : response.css('td:nth-child(6) > span > span::text').get(),
                'rental_rate' : response.css('td:nth-child(2) > div:nth-child(2) > div > span > span:nth-child(3)::text').get()
                # 'room_area' : response.css("div[id=listings-for-rent] .listing-row__cell-area span[data-type=area] .number::text").get(),
                # 'rental_rate' : response.css("div[id=listings-for-rent] .listing-row__primary .money .number::text").get()
            }
            
            yield items
        # item = {
        #     'condo' : response.css('.project-header-name a::text').get(),
        #     'district' : response.css('.breadcrumb li:nth-child(2) span::text').get(),
        #     'room_area': response.css("div[id=listings-for-rent] .listing-row__cell-area span[data-type=area] .number::text").getall(),
        #     'rental_rate' : response.css("div[id=listings-for-rent] .listing-row__primary .money .number::text").getall()
        # }   


    