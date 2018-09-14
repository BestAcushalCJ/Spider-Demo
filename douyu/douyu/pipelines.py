# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from douyu.settings import IMAGES_STORE as imgs_store

class DouyuPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        img_src = item['img_src']
        yield scrapy.Request(img_src)

    def item_completed(self, results, item, info):
        img_path = [x['path'] for ok, x in results if ok]
        print(img_path)

        os.renames(imgs_store + img_path[0], imgs_store + 'full/' + item['nickname'] + '.jpg')

        return item