# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class LianjiaPipeline(object):
    def process_item(self, item, spider):
        # 规定保存数据的排列顺序
        args = [item['district'], item['region'], item['elevator'], item['floor'], item['id'], item['shi'],
                item['ting'], item['price'], item['renovation'], item['size']]
        # 去除带有空值的行
        arg = [x for x in args if x != '']
        # 保存为csv文件
        with open('cd_information.csv', 'a+', encoding='utf-8', newline='')as f:
            w = csv.writer(f)
            w.writerow(arg)
        return item

