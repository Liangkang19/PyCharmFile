# -*- coding: utf-8 -*-
# Scrapy使用css和xpath选择器来定位元素，它有四个基本方法：
# xpath():   返回选择器列表，每个选择器代表使用xpath语法选择的节点
# css():     返回选择器列表，每个选择器代表使用css语法选择的节点
# extract(): 返回被选择元素的unicode字符串
# re():      返回通过正则表达式提取的unicode字符串列表

import scrapy


class DomeSpider(scrapy.Spider):
    name = 'dome'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')       # 选择class="quote"的所有元素
        for quote in quotes:
            text1 = quote.css('.text::text')  # 选择class="text"中，text的内容部分
            text = text1.extract_first()      # 选择第一个元素中的字符串
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tags::text').ectract()
        pass
