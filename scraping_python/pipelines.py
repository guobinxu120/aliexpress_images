# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import smtplib
import MySQLdb

class ScrapingPythonPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        if spider.name == 'aliexpress_images':
            return
        host = '127.0.0.1'
        user_name = 'root'
        password = ''
        db_name = 'xdata'

        self.connection = MySQLdb.connect(host=host, user=user_name, passwd=password, db=db_name, charset='utf8')
        # self.conn = MySQLdb.connect(host=settings.db_host, user=settings.db_username, passwd=settings.db_password, db=settings.db_name, charset='utf8')
        self.connection.ping(True)
        self.cursor = self.connection.cursor()

        spider.connection = self.connection
        spider.cursor = self.cursor


        sql_to_get_crawl_list = "SELECT * FROM crawl_list  WHERE store_type='{}';".format(spider.name)
        result = self.cursor.execute(sql_to_get_crawl_list)
        row = self.cursor.fetchone()
        existing_data_list = []
        last_crawl_url = {}
        last_page = {}
        is_success = {}

        store_ids = []
        while row is not None:
            existing_data_list.append(row)
            is_success[str(row[0])] = row[8]
            if row[8] == 'failed':
                last_crawl_url[str(row[0])] = row[6]
                last_page[str(row[0])] = row[7]

            store_ids.append(row[3])

            row = self.cursor.fetchone()
        spider.existing_data_list = existing_data_list

        item_ids_got_already = []
        for store_id in store_ids:
            sql_to_get_products = "SELECT * FROM products  WHERE store_id='{}';".format(store_id)
            result = self.cursor.execute(sql_to_get_products)
            row = self.cursor.fetchone()

            while row is not None:
                product_id = row[3].split('-')[0]
                if product_id not in item_ids_got_already:
                    item_ids_got_already.append(product_id)

                row = self.cursor.fetchone()
        spider.item_ids_got_already = item_ids_got_already

        pass


    def spider_closed(self, spider):
        pass
        # self.connection.close()

    def process_item(self, item, spider):
        query = "SELECT * FROM products WHERE product_number='{}'".format(item['product_number'])
        print(query)
        result = self.cursor.execute(query)
        if result == 0:
            key_txt = ','.join(item.keys())
            keys = key_txt.split(',')
            values = ""
            for i, val in enumerate(item.values()):
                if isinstance(val, float) or isinstance(val, int):
                    val = str(val)
                else:
                    if val == None:
                        # val = "''"
                        val = "''"
                    else:
                        val = val.replace("'", '"')
                        # val = "'" + val + "'"
                        val = "'" + val + "'"
                val = '{}'.format(val)
                values = values + ',' + val

            values = values[1:]
            query_str = "INSERT INTO products ({}) VALUES ({});".format(key_txt, values)
            # query = "UPDATE products SET {}".format(values)
            # print(query)
            try:
                result = self.cursor.execute(query_str)
            except Exception as e:
                print('Error')
            self.connection.commit()

            print('\n####################################################')
            print('Saved product ID: ' + str(item.get('product_number')))
            print('####################################################\n')
            return item
        else:
            print('\n####################################################')
            print('Exists product ID: ' + str(item.get('product_number')))
            print('Detail URL: ' + str(item.get('detail_url')))
            print('####################################################\n')

            # return {}
