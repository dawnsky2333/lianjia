# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class LianjiaPipeline(object):
    def process_item(self, item, spider):
        args = [item['district'],item['region'],item['elevator'],item['floor'],item['id'],item['layout'],
                item['price'],item['renovation'],item['size'],item['year']]
        with open('cd_information.csv','a+',encoding='utf-8', newline='')as f:
            # 保存为csv文件
            w = csv.writer(f)
            w.writerow(args)
        return item

