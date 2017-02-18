# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from realestatemarket.items import CondoSoldItem
import re


class LianjiaChengjiaoSpider(scrapy.Spider):

    # scrapy唯一定位实例的属性，必须唯一
    name = "lianjia_chengjiao"

    # 允许爬取的域名列表，不设置表示允许爬取所有
    allowed_domains = ["bj.lianjia.com"]

    # 起始爬取列表
    start_urls = ["http://bj.lianjia.com/chengjiao/pg1"]

    # 根据我们自己的需求拼接要访问的url，有了这个函数定义后start_urls实际上就没用了
    def start_requests(self):

        pages = []

        for i in range(1,100):
            url = 'http://bj.lianjia.com/chengjiao/pg%s' % i
            page = scrapy.Request(url)
            pages.append(page)

        return pages

    # 回调函数，处理response并返回处理后的数据和需要跟进的url
    def parse(self, response):
        # response  <200 http://bj.lianjia.com/chengjiao/>  请求返回成功
        # response.body 返回的网页内容
        sel = Selector(response)
        sites = response.xpath(
            '//div[@class="content"]/div[@class="leftContent"]/ul[@class="listContent"]/li/div[@class="info"]')
        items = []

        for site in sites:
            item = CondoSoldItem()
            # http://bj.lianjia.com/chengjiao/101101076131.html
            link = site.xpath('div[@class="title"]/a/@href').extract()
            item['lj_id'] = re.findall('[\d]{12}', link[0])

            title = site.xpath('div[@class="title"]/a/text()').extract()
            titles = title[0].split(' ')

            item['subdistrict_name'] = titles[0]
            item['condo_framework'] = titles[1]
            item['square'] = str(titles[2]).replace('\u5e73\u7c73', '')

            item['date'] = site.xpath('div[@class="address"]/div[@class="dealDate"]/text()').extract()
            item['expense'] = site.xpath('div[@class="address"]/div[@class="totalPrice"]/span/text()').extract()
            item['price'] = site.xpath('div[@class="flood"]/div[@class="unitPrice"]/span/text()').extract()

            items.append(item)

        return items

