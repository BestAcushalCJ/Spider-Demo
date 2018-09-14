# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 教师姓名
    name = scrapy.Field()
    # 教师职称
    title = scrapy.Field()
    # 教师信息
    info = scrapy.Field()
    # pass
