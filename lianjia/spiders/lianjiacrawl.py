# -*- coding: utf-8 -*-
import scrapy

from lianjia.items import LianjiaItem


class LianjiacrawlSpider(scrapy.Spider):
    name = 'lianjiacrawl'

    start_urls = ['https://cd.lianjia.com/ershoufang/']

    def parse(self, response):
        urls = response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_one)

            for i in range(2, 101):
                link = 'https://cd.lianjia.com/ershoufang/pg{}/'.format(str(i))
                yield scrapy.Request(link, callback=self.parse)

    def parse_one(self, response):

        item = LianjiaItem()

        district = response.xpath('//div[@class="aroundInfo"]/div[@class="areaName"]/span[@class="info"]/a[1]/text()').extract_first()
        region = response.xpath('//div[@class="houseInfo"]/div[@class="type"]/div[@class="mainInfo"]/text()').extract_first()
        elevator = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[11]/text()').extract_first()
        floor = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[2]/text()').extract_first()
        id = response.xpath('//div[@class="houseRecord"]/span[@class="info"]/text()').extract_first()
        layout = response.xpath('//div[@class="houseInfo"]/div[@class="room"]/div[@class="mainInfo"]/text()').extract_first()
        price = response.xpath('//div[@class="content"]/div[@class="price "]/span[@class="total"]/text()').extract_first()
        renovation = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[9]/text()').extract_first()
        size = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[3]/text()').extract_first()
        year = response.xpath('//div[@class="houseInfo"]/div[@class="area"]/div[@class="subInfo"]/text()').extract_first().split('/')[0]

        # 区
        item['district'] = district
        # 房屋朝向
        item['region'] = region
        # 是否配备电梯
        item['elevator'] = elevator
        # 所在楼层
        item['floor'] = floor
        # 链家编号
        item['id'] = id
        # 房屋户型
        item['layout'] = layout
        # 房屋价格（单位：万）
        item['price'] = price
        # 装修类型
        item['renovation'] = renovation
        # 建筑面积
        item['size'] = size
        # 修建时间
        item['year'] =year

        yield item