# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DouyuSpiderSpider(scrapy.Spider):
    name = 'douyu_spider'
    allowed_domains = ['douyucdn.cn', 'douyu.com']

    base_url = 'http://www.douyu.com/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [base_url + str(offset)]


    def parse(self, response):
        data_list = json.loads(response.body)['data']
        if len(data_list) == 0:
            return

        for data in data_list:
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['img_src'] = data['vertical_src']
            yield item

        self.offset += 20
        url = self.base_url + str(self.offset)
        yield scrapy.Request(url, callback=self.parse)

