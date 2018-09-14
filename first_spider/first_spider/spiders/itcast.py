# -*- coding: utf-8 -*-
import scrapy
from first_spider.items import FirstSpiderItem


class ItcastSpider(scrapy.Spider):
    # 爬虫名，启动爬虫时必需的参数
    name = 'itcast'
    # 爬取域范围，允许爬虫在这个域名下进行爬取（可选参数）
    allowed_domains = ['http://www.itcast.cn']
    # 起始url列表，爬虫执行后第一批请求，将从这个列表里获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")
        # items = []
        for node in node_list:
            # 创建item对象，用来存储信息
            item = FirstSpiderItem()
            # extract()将xpath对象转换为Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # items.append(item)

            # 返回提取到的每个item数据，给管道文件处理，同时还会回来继续执行后面的代码
            yield item
