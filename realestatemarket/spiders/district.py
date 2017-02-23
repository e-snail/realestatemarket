# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

# 北京区域列表
districts = [u"东城",u"西城",u"朝阳",u"海淀",u"丰台",u"石景山","通州",
             u"昌平",u"大兴",u"亦庄开发区",u"顺义",u"房山",u"门头沟",u"平谷",u"怀柔",u"密云",u"延庆",u"燕郊"]


# 爬下北京每个区的小区个数
class BJDistrictSpiderPipeline(scrapy.Spider):

    # scrapy唯一定位实例的属性，必须唯一
    name = "bj_district_xiaoqu"

    # 允许爬取的域名列表，不设置表示允许爬取所有
    allowed_domains = ["bj.lianjia.com"]

    start_urls = []

    # 起始爬取列表
    for district in districts:
        url = "http://bj.lianjia.com/xiaoqu/rs" + district
        start_urls.append(url)

    # 回调函数，处理response并返回处理后的数据和需要跟进的url
    def parse(self, response):

        items = []

        soup = BeautifulSoup(response.body, "lxml")
        total_info = soup.find('div', {'class': 'page-box house-lst-page-box'}).get('page-data')
        pages = total_info.split(',')[0].split(':')[1]

        return items
