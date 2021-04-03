# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class LianjiaItem(Item):
    # define the fields for your item here like:
    district = Field()
    region = Field()
    id = Field()
    shi = Field()
    ting = Field()
    floor = Field()
    size = Field()
    elevator = Field()
    renovation = Field()
    price = Field()
