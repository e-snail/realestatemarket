# -*- coding: utf-8 -*-
import scrapy
from realestatemarket.items import XiaoquItem
from bs4 import BeautifulSoup
import re


regions = [u"东城"]


# 爬下每个区所有的小区信息
class BJXiaoquSpiderPipeline(scrapy.Spider):

    # scrapy唯一定位实例的属性，必须唯一
    name = "bj_xiaoqu_single"

    # 允许爬取的域名列表，不设置表示允许爬取所有
    allowed_domains = ["bj.lianjia.com"]

    # 起始爬取列表
    start_urls = ["http://bj.lianjia.com/xiaoqu/rs"]

    # 根据我们自己的需求拼接要访问的url，有了这个函数定义后start_urls实际上就没用了
    def start_requests(self):

        pages = []
        counts = [1]

        region = u"朝阳"

        for count in counts:
            url = u"http://bj.lianjia.com/xiaoqu/pg" + str(count) + "rs" + region + "/"
            page = scrapy.Request(url)
            pages.append(page)

        return pages

    # 回调函数，处理response并返回处理后的数据和需要跟进的url
    def parse(self, response):
        # response  <200 http://bj.lianjia.com/xiaoqu/rs朝阳/>  请求返回成功
        # response.body 返回的网页内容

        items = []

        # plain_text = unicode(response)  # ,errors='ignore')
        soup = BeautifulSoup(response.body, "lxml")
        xiaoqu_list = soup.find('div', {'class': 'content'}).findAll('li', {'class': 'clear xiaoquListItem'})

        for xq in xiaoqu_list:

            xiaoqu_item = XiaoquItem()

            xiaoqu_item['href'] = xq.find('a', {'class': 'img'}).get('href')

            xiaoqu_item['name'] = xq.find('div', {'class': 'title'}).find('a', {'target': '_blank'}).text

            content = xq.find('div', {'class': 'positionInfo'}).text.strip()
            contents = content.split('\n')

            xiaoqu_item['district'] = contents[0].strip()
            xiaoqu_item['biz_circle'] = contents[1].strip()
            xiaoqu_item['style'] = contents[2].strip()
            xiaoqu_item['build_year'] = re.findall('[\d]{4}', contents[3].strip())[0]

            items.append(xiaoqu_item)

        return items