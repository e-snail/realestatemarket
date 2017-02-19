# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from hashlib import md5

import pymysql
import pymysql.cursors


# class RealestatemarketPipeline(object):
#     def process_item(self, item, spider):
#         return item


def db_handle():
    conn = pymysql.connect(
        host='localhost',
        db='lianjia_sold',
        user='root',
        passwd='root123',
        charset='utf8',
        use_unicode=False
    )
    return conn


class LianjiaSoldPipeline(object):

    def __init__(self):
        return

    # pipeline默认调用
    @classmethod
    def process_item(cls, item, spider):
        db_object = db_handle()
        cursor = db_object.cursor()
        sql = '''
            insert into condo_sold(lj_id, square, expense, price, date, condo_framework, subdistrict_name)
            values (%s, %s, %s, %s, %s, %s, %s)
        '''

        try:
            cursor.execute(sql, ( item['lj_id'], item['square'], item['expense'], item['price'], item['date'], item['condo_framework'], item['subdistrict_name']))
            db_object.commit()
        except Exception as e:
            print(e)
            db_object.rollback()

        return item


class LianjiaChengjiaoPipeline(object):

    def __init__(self):
        return

    # # pipeline默认调用
    # @classmethod
    # def process_item(cls, item, spider):
    #     db_object = db_handle()
    #     cursor = db_object.cursor()
    #     sql = '''
    #         insert into condo_sold(lj_id, square, expense, price, date, condo_framework, subdistrict_name)
    #         values (%s, %s, %s, %s, %s, %s, %s)
    #     '''
    #
    #     try:
    #         cursor.execute(sql, ( item['lj_id'], item['square'], item['expense'], item['price'], item['date'], item['condo_framework'], item['subdistrict_name']))
    #         db_object.commit()
    #     except Exception as e:
    #         print(e)
    #         db_object.rollback()
    #
    #     return item

