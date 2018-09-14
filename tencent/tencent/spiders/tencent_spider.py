# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentSpiderSpider(scrapy.Spider):
    name = 'tencent_spider'
    allowed_domains = ['tencent.com']
    # 1.需要拼接的url
    base_url = 'https://hr.tencent.com/position.php?&start='
    # 1.需要拼接的url地址的偏移量
    offset = 0
    # 爬虫启动时，读取的url地址
    start_urls = [base_url + str(offset)]

    # 用来出来response
    def parse(self, response):
        # 提取每个response的数据
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = TencentItem()
            # 提取每个职位的信息
            item['position_name'] = node.xpath("./td[1]/a/text()").extract()[0]
            item['position_link'] = node.xpath("./td[1]/a/@href").extract()[0]

            if len(node.xpath("./td[2]/text()")):
                item['position_type'] = node.xpath("./td[2]/text()").extract()[0]
            else:
                item['position_type'] = '不定'

            item['people_num'] = node.xpath("./td[3]/text()").extract()[0]
            item['work_location'] = node.xpath("./td[4]/text()").extract()[0]
            item['publish_time'] = node.xpath("./td[5]/text()").extract()[0]

            # yield的重要性，是返回数据后还能回来接着执行代码
            yield item
            
        # 第一种写法，拼接url，适用场景：也没没有可以点击的请求链接，必须通过拼接url才能获取响应
        # if self.offset < 3330:
        #     self.offset += 10
        #     url = self.base_url + str(self.offset)
        #     yield scrapy.Request(url, callback=self.parse)

        # 第二种写法，直接从response获取需要爬取的下一页链接，并发送请求处理，直到请求全部提取完
        if not len(response.xpath("//a[@class='noactive' and @id='next']")):
            url = response.xpath("//a[@id='next']/@href")[0].extract()
            yield scrapy.Request("http://hr.tencent.com/" + url, callback=self.parse)