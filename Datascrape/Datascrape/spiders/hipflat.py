# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

# things to get rental price, sqm, type
# 
class HipflatSpider(scrapy.Spider):
    name = 'hipflat'
    start_urls = ['https://www.hipflat.co.th/en/market/condo-bangkok-skik']

    
    def parse(self, response):
        districts = response.css('.directories__lists-element-name::attr(href)').getall()
        # district_names = response.css('.directories__lists-element-name::text').getall()
        for district in districts:
            district_url = response.urljoin(district)    
        yield Request(district_url, callback=self.parse_condo)
    
    def parse_condo(self, response):
        condos = response.css('.directories__lists-element-name::attr(href)').getall() 
        for condo in condos:
            url = response.urljoin(condo)
        yield Request(url, callback=self.parse_rental)

    def parse_rental(self, response):
        yield {
            'condo' : response.css('.project-header-name a::text').getall(),
            'address' : response.css('span[itemprop=streetAddress]::text').get(),
            'rental_rate' : response.css("div[id=listings-for-rent] .listing-row__primary .money .number::text").getall(),
            'condo_area': response.css("div[id=listings-for-rent] .listing-row__cell-area span[data-type=area] .number::text").getall() 
        }
        print('Done')
    