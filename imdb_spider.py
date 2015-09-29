#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 entro <entropy1208@yahoo.co.in>
#
# Distributed under terms of the Psycho license.

import scrapy
import pymongo

try:
    client = pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
    print "Could not clientect to MongoDB: %s" % e
db = client.indexes
indexes1 = db.indexes1

class imdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["imdb.com"]
    start_urls = [
            "http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1/",
    ]
    def parse(self, response):
        next_pages = response.xpath('//td[@class = "overview-top"]/h4[@itemprop = "name"]/a/@href').extract()
        if next_pages:
            for elem in next_pages:
                url = response.urljoin(elem)
                yield scrapy.Request(url, self.parse_dir_contents)
    def parse_dir_contents(self, response):
        for sel in response.xpath('//td[@id = "overview-top"]'):
            item = {} 
            item['title'] = sel.xpath('h1/span[@class = "itemprop"]/text()').extract()
            item['year'] = sel.xpath('h1/span[@class = "nobr"]/a/text()').extract()
            item['rating'] = sel.xpath('div[@class = "infobar"]/meta/@content').extract()
            item['genres'] = sel.xpath('div[@class = "infobar"]/a/span[@class = "itemprop"]/text()').extract()
            item['runtime'] = sel.xpath('div[@class = "infobar"]/time/text()').extract()
            item['metascore'] = sel.xpath('div[@class = "star-box giga-star"]/div[@class = "star-box-details"]/strong/span/text()').extract()
            item['desc'] = sel.xpath('p[@itemprop = "description"]/text()').extract()
            item['director'] = sel.xpath('div[@itemprop = "director"]/a/span/text()').extract()
            item['stars'] = sel.xpath('div[@itemprop = "actors"]/a/span/text()').extract()
            indexes1.insert_one(item) 
        
        links = response.xpath('//div[@class = "rec_page"]/div[@class = "rec_item"]/a/@href').extract()
        if links:
            for link in links:
                url = response.urljoin(link)
                yield scrapy.Request(url, callback = self.parse_dir_contents)

    
