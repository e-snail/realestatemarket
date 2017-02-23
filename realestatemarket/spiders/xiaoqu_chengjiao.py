# -*- coding: utf-8 -*-
import scrapy
from realestatemarket.items import ChengjiaoItem
from bs4 import BeautifulSoup


# 爬下小区信息的所有成交信息
class XiaoquChengjiaoSpiderPipeline(scrapy.Spider):

    # scrapy唯一定位实例的属性，必须唯一
    name = "xiaoqu_chengjiao_all"

    start_urls = ["http://bj.lianjia.com/chengjiao/pg1rs%E5%86%A0%E5%BA%AD%E5%9B%AD"]

    # 根据我们自己的需求拼接要访问的url，有了这个函数定义后start_urls实际上就没用了
    def start_requests(self):

        pages = []
        counts = [1]

        xiaoqu = u"冠庭园"

        for count in counts:
            url = u"http://bj.lianjia.com/chengjiao/pg" + str(count) + "rs" + xiaoqu + "/"
            page = scrapy.Request(url)
            pages.append(page)

        return pages

    # 回调函数，处理response并返回处理后的数据和需要跟进的url
    def parse(self, response):
        # response  <200 http://bj.lianjia.com/chengjiao/pg1rs%E5%86%A0%E5%BA%AD%E5%9B%AD/>  请求返回成功
        # response.body 返回的网页内容
        items = []

        # FIXME 取的当前小区的所有成交记录页数 pages
        # soup = BeautifulSoup(response.body, "lxml")
        # total_info = soup.find('div', {'class': 'page-box house-lst-page-box'}).get('page-data')
        # pages = total_info.split(',')[0].split(':')[1]

        # 抓取小区当前页所有成交记录
        soup = BeautifulSoup(response.body, "lxml")
        chengjiao_list = soup.find('div', {'class': 'content'}).findAll('ul', {'class': 'listContent'})

        print("count=" + str(len(chengjiao_list)))

        for chengjiao in chengjiao_list:

            chengjiao_item = ChengjiaoItem()

            # 链接
            chengjiao_item['href'] = chengjiao.find('a', {'class': 'img'}).get('href')

            info = chengjiao.find('div', {'class': 'info'})

            # 冠庭园 2室1厅 74.24平米
            title = info.find('div', {'class': 'title'}).find('a').text
            titles = title.split(" ")
            # 小区名
            chengjiao_item['name'] = titles[0]
            # 户型
            chengjiao_item['frame'] = titles[1]
            # 面积
            chengjiao_item['area'] = titles[2]

            address = info.find('div', {'class': 'address'})

            # 2016.06.06 or 2016.06 or ...
            # 成交日期
            deal_date = address.find('div', {'class': 'dealDate'}).text
            chengjiao_item['deal_date'] = deal_date
            # 总价
            total_price = address.find('div', {'class': 'totalPrice'}).text
            chengjiao_item['total_price'] = total_price

            floor = info.find('div', {'class': 'flood'})
            # 中介
            agent = floor.find('div', {'class': 'source'}).text     # 其它公司成交 or 链家成交
            chengjiao_item['agent'] = agent
            # 单价
            unit_price = floor.find('div', {'class': 'unitPrice'}).text
            chengjiao_item['unit_price'] = unit_price

            # print(chengjiao_item)

            items.append(chengjiao_item)

        return items
