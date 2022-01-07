# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from collections import OrderedDict
from datetime import datetime, timedelta
from scrapy.http import TextResponse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import requests, random, json
from scrapy.utils.project import get_project_settings

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class aliexpressSpider(Spider):
    name = "aliexpress_images"
    start_url = 'https://www.aliexpress.com'
    domain1 = 'aliexpress.com'

    total_count = 0
    use_selenium = True

    # settings = get_project_settings()
    # # list_proxy = settings.get('PROXIES')
    # proxy = random.choice(list_proxy)

    def __init__(self, proxy_type=None, proxy_url=None, *args, **kwargs):
        super(aliexpressSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        url = 'https://www.aliexpress.com/category/200001648/blouses-shirts.html'
        yield Request(url, self.parse,
                      meta={"next_count": 1,
                            'url': url},
                      errback=self.err_parse)

    def parse(self, response):
        if 'https://login.' in response.url:
            self.err_parse(response)
            return

        script_datas = response.xpath('//script/text()').extract()
        json_data = {}
        for script_data in script_datas:
            if 'window.runParams = {' in script_data:
                script_data = script_data.replace('window.runParams = {', '')
                # script_data = script_data.replace('data: {"actionModule":', '')
                script_data = script_data.strip()
                script_data = script_data[6:len(script_data) - 3]
                script_data = script_data.split('csrfToken:')[0].strip()
                script_data = script_data[:len(script_data) - 1]
                json_data = json.loads(script_data)

        item_urls = response.xpath('//div[@class="ui-box-body"]/ul[@class="items-list util-clearfix"]/li/div[@class="detail"]/h3/a/@href').extract()

        data_list = response.meta.get('data_list')

        if (not data_list[7]) or (data_list[7] <= response.meta.get('next_count')):
            bad_resp = False
            is_continue = False

            for item_url in item_urls:
                if 'https:' not in item_url:
                    item_url = 'https:' + item_url
                # item_url = 'https://www.aliexpress.com/store/product/2-3-4G-Mobile-Phone-Signal-Booster-Signal-Amplifier-Set-Cell-Phone-Signal-Repeater-900-1800/3106020_4000207196617.html'

                id_got = item_url.split('/')[-1].split('_')[-1].replace('.html', '')
                if id_got in self.item_ids_got_already:
                    print('\n####################################################')
                    print('Exists product ID: ' + id_got)
                    print('Detail URL: ' + item_url)
                    print('####################################################\n')
                    continue

                resp_1 = requests.get(item_url)
                if resp_1.status_code == 200:
                    resp = TextResponse(url=item_url,
                                        body=resp_1.text,
                                        encoding='utf-8')

                    script_datas = resp.xpath('//script/text()').extract()
                    json_data = {}
                    for script_data in script_datas:
                        if 'window.runParams = {' in script_data:
                            script_data = script_data.replace('window.runParams = {', '')
                            # script_data = script_data.replace('data: {"actionModule":', '')
                            script_data = script_data.strip()
                            script_data = script_data[6:len(script_data) - 3]
                            script_data = script_data.split('csrfToken:')[0].strip()
                            script_data = script_data[:len(script_data) - 1]
                            json_data = json.loads(script_data)

                    if json_data:
                        item = OrderedDict()
                        for field_name in self.field_names:
                            item[field_name] = ''
                        item['store_id'] = data_list[3]

                        commonModule = json_data.get('commonModule')
                        item['product_number'] = str(commonModule.get('productId'))
                        item['is_variation'] = 0
                        item['variation_theme'] = ''
                        item['variation_value'] = ''

                        specsModule = json_data.get('specsModule')
                        item['upc'] = ''
                        item['brand'] = ''
                        item['mpn'] = ''
                        item['model'] = ''

                        variation_themes = []
                        variation_values_dict = {}

                        specsModule_props = specsModule.get('props')
                        for specsModule_prop in specsModule_props:
                            variation_values = []
                            attrName = specsModule_prop.get('attrName')
                            attrValue = specsModule_prop.get('attrValue')
                            if 'Brand' in attrName:
                                item['brand'] = attrValue
                            elif 'Model' in attrName:
                                item['model'] = attrValue
                            elif 'UPC' in attrName:
                                item['upc'] = attrValue
                            elif 'MPN' in attrName:
                                item['mpn'] = attrValue
                            elif 'Size' in attrName:
                                variation_themes.append('Size')
                                variation_values.append(attrValue.strip())
                                variation_values_dict['Size'] = variation_values
                                # item['is_variation'] = 1
                                # item['variation_theme'] = 'Size'
                                # item['variation_value'] = attrValue
                            # elif 'Type' in attrName:
                            #     variation_themes.append('Type')
                            #     variation_values.append(attrValue.strip())
                            #     variation_values_dict['Type'] = variation_values
                                # item['is_variation'] = 1
                                # item['variation_theme'] = 'Type'
                                # item['variation_value'] = attrValue
                            elif 'Color' in attrName:
                                variation_themes.append('Color')
                                variation_values.append(attrValue.strip())
                                variation_values_dict['Color'] = variation_values
                                # item['is_variation'] = 1
                                # item['variation_theme'] = 'Color'
                                # item['variation_value'] = attrValue

                        # if item['variation_value']:
                        #
                        # else:
                        #     item['parent_product_number'] = item['product_number']

                        item['detail_url'] = item_url
                        item['full_category_path'] = data_list[4]

                        # storeModule = json_data.get('storeModule')
                        # item['item_location_city'] = storeModule.get('province')
                        # item['item_location_country'] = storeModule.get('countryCompleteName')
                        skuModule = json_data.get('skuModule')
                        item['item_location_city'] = ''
                        if skuModule.get('productSKUPropertyList'):
                            location_countries = []
                            for productSKUPropertyList in skuModule.get('productSKUPropertyList'):
                                if productSKUPropertyList.get('skuPropertyValues'):
                                    skuPropertyValues = productSKUPropertyList.get('skuPropertyValues')

                                    if productSKUPropertyList['skuPropertyName'] == 'Ships From':
                                        # get country
                                        for skuPropertyValue in skuPropertyValues:
                                            location_countries.append(skuPropertyValue.get('propertyValueDisplayName'))
                                    else:
                                        variation_themes.append(productSKUPropertyList['skuPropertyName'])
                                        variation_values = []
                                        for skuPropertyValue in skuPropertyValues:
                                            variation_values.append(skuPropertyValue.get('propertyValueDisplayName').strip())
                                        variation_values_dict[productSKUPropertyList['skuPropertyName']] = variation_values
                            item['item_location_country'] = ', '.join(location_countries)

                        titleModule = json_data.get('titleModule')
                        item['item_title'] = titleModule.get('subject')

                        priceModule = json_data.get('priceModule')
                        item['unit_price'] = priceModule.get('maxActivityAmount').get('value')
                        item['shipping_cost'] = 0
                        item['currency_code'] = priceModule.get('maxActivityAmount').get('currency')


                        item['description_text'] = ''
                        item['description_html'] = ''
                        item['specifics_html'] = ''

                        imageModule = json_data.get('imageModule')
                        for i, imagePath in enumerate(imageModule.get('imagePathList')):
                            if i > 11:
                                break
                            img_title = 'img' + str(i + 1)
                            item[img_title] = imagePath

                        descriptionModule = json_data.get('descriptionModule')
                        descriptionUrl = descriptionModule.get('descriptionUrl')
                        if descriptionUrl:
                            yield Request(descriptionUrl, self.parseDescription, meta={'item': item, 'variation_themes': variation_themes, 'variation_values_dict': variation_values_dict})

                        # update query ##########################
                        update_query = 'UPDATE crawl_list SET last_crawl_url = "{}", last_page = {} WHERE uid={};'.format(response.meta.get('url'), str(response.meta.get('next_count')), str(data_list[0]))
                        result = self.cursor.execute(update_query)
                        self.connection.commit()
                        ###################################

                        # yield Request(item_url, self.parseDetail, meta={'url': response.meta.get('url'), 'data_list': response.meta.get('data_list')})
                else:
                    bad_resp = True

                # break

            if bad_resp:
                # update query ##########################
                update_query = 'UPDATE crawl_list SET crawl_status = "failed" WHERE uid={};'.format(str(data_list[0]))
                result = self.cursor.execute(update_query)
                self.connection.commit()
                ###################################
                return
            else:
                # update query ##########################
                update_query = 'UPDATE crawl_list SET crawl_status = "success" WHERE uid={};'.format(str(data_list[0]))
                result = self.cursor.execute(update_query)
                self.connection.commit()
                ###################################


        next_url = response.xpath('//a[text()="Next"]/@href').extract_first()
        if next_url:
            if 'https:' not in next_url:
                next_url = 'https:' + next_url
            next_count = response.meta.get('next_count')
            if self.proxy_type:
                yield Request(next_url, self.parse, meta={"next_count": next_count + 1, 'url': next_url, 'proxy': response.meta.get('proxy'),
                                                          'data_list': response.meta.get('data_list')}, errback=self.err_parse)
            else:
                yield Request(next_url, self.parse, meta={"next_count": next_count + 1, 'url': next_url,
                                                          'data_list': response.meta.get('data_list')})



    def err_parse(self, response):
        self.proxy = random.choice(self.list_proxy)
        # response.request.meta['proxy'] = proxy
        print ('err proxy: ' + self.proxy)
        response.request.meta['proxy'] = self.proxy
        if not 'errpg' in response.request.url :
            yield Request(response.request.meta['url'],
                          callback=self.parse,
                          meta=response.request.meta,
                          dont_filter=True,
                          errback=self.err_parse)