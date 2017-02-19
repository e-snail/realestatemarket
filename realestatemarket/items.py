# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class RealestatemarketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 北京区县信息
class BJCityDistrict(Item):
    id = Field()                # 区县id
    district_no = Field()       # 区县号
    district_name = Field()     # 区县名


# 房子格局信息
class CondoFrameworkItem(Item):
    id = Field()        # 格局id
    des = Field()       # 格局描述


# 房子所在小区信息
class CondoPosition(Item):
    id = Field()                    # 位置信息id
    province = Field()              # 省、市
    city = Field()                  # 市
    district = BJCityDistrict()     # 区县
    longitude = Field()             # 经度
    latitude = Field()              # 纬度
    subdistrict_name = Field()      # 小区名


# 已成交房子的信息
class CondoSoldItem(Item):
    id = Field()                        # 已成交房子id
    lj_id = Field()                     # 已成交房子的链家编号
    square = Field()                    # 面积
    expense = Field()                   # 总价
    price = Field()                     # 单价
    date = Field()                      # 成交日期

    subdistrict_name = Field()          # 小区名
    condo_framework = Field()           # 房子格局

    # framework = CondoFrameworkItem()    # 房子格局
    # position = CondoPosition()          # 位置信息


# 小区信息
class XiaoquItem(Item):
    href = Field()
    name = Field()
    district = Field()
    biz_circle = Field()
    style = Field()
    build_year = Field()


# 成交房屋信息
class ChengjiaoItem(Item):
    # 链接
    href = Field()
    # 小区名
    name = Field()
    # 户型
    frame = Field()
    # 面积
    area = Field()
    # 成交日期
    deal_date = Field()
    # 单价
    unit_price = Field()
    # 总价
    total_price = Field()
    # 中介
    agent = Field()