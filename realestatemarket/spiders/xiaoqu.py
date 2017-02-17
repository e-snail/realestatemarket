# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from realestatemarket.items import CondoSoldItem
import re

class LianjiaChengjiaoSpider(scrapy.Spider):

    def start_requests(self):

    def parse(self, response):