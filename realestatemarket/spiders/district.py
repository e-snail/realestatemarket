# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import urllib.parse
from .global_model import GlobalModel


# 爬下北京每个区的小区个数
class BJDistrictSpiderPipeline(scrapy.Spider):

    # scrapy唯一定位实例的属性，必须唯一
    name = "bj_district_xiaoqu"

    # 允许爬取的域名列表，不设置表示允许爬取所有
    allowed_domains = ["bj.lianjia.com"]

    start_urls = []

    # 起始爬取列表
    for region in GlobalModel.regions:
        url = GlobalModel.url_regions_prefix + region
        start_urls.append(url)

    def start_requests(self):

        pages = []

        # 起始爬取列表
        for region in GlobalModel.regions:
            url = GlobalModel.url_regions_prefix + region
            page = scrapy.Request(url)
            pages.append(page)

            yield page

    # 回调函数，处理response并返回处理后的数据和需要跟进的url
    def parse(self, response):

        items = []

        # 解析出各区县的小区页数
        soup = BeautifulSoup(response.body, "lxml")
        total_info = soup.find('div', {'class': 'page-box house-lst-page-box'}).get('page-data')
        pages = total_info.split(',')[0].split(':')[1]

        # 从url中找到区县名称，再找到对应的index，最后对regions_pages[index]赋值
        region_name = response.url.replace(GlobalModel.url_regions_prefix, "").replace("/", "")
        region_name = urllib.parse.unquote(region_name)
        index = GlobalModel.regions.index(region_name)
        GlobalModel.regions_pages[index] = pages

        print('===========')
        print(GlobalModel.regions_pages)

        return items
