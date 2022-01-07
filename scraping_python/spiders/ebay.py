# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from collections import OrderedDict
from scrapy.http import TextResponse
import requests, random, re

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class ebaySpider(Spider):
    name = "ebay"
    start_url = 'https://www.ebay.com/'
    domain1 = 'ebay.com'

    total_page_count = 1
    total_count = 0
    existing_data_list = []

    use_selenium = True

    last_crawl_url = {}
    last_page = {}
    is_success = {}

    crawl_status = ''
    connection = None
    cursor = None

    list_proxy = []
    item_ids_got_already = []

    # driver = webdriver.PhantomJS('phantomjs.exe')
    # driver.set_page_load_timeout(300)
    field_names = ['store_id', 'product_number', 'parent_product_number', 'is_variation',
                   'variation_theme', 'variation_value', 'upc',
                   'brand', 'mpn', 'model', 'detail_url', 'full_category_path',
                   'item_location_city', 'item_location_country', 'item_title',
                   'unit_price', 'shipping_cost', 'currency_code',
                   'description_text', 'description_html', 'specifics_html']

    headers = {
        'Cookie': 'aam_uuid=57987744947528180730353878592377435564; _ga=GA1.2.1757181732.1572027267; AMCVS_A71B5B5B54F607AB0A4C98A2%40AdobeOrg=1; AMCV_A71B5B5B54F607AB0A4C98A2%40AdobeOrg=-1303530583%7CMCIDTS%7C18199%7CMCMID%7C57977471168163333480352939188929301521%7CMCAAMLH-1572921002%7C9%7CMCAAMB-1572921002%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCCIDH%7C-1911210502%7CMCOPTOUT-1572323402s%7CNONE%7CvVersion%7C3.3.0; DG_ZID=8978D90C-3F60-3B3F-B945-52DB9FC3436F; ak_bmsc=E89987474A52A74D9979B7BE1BCF4C0DA5FE9C5E222000001FA4B75D3CCDF924~plnTZGuCafBSOwZAmD/FJ16blv7QkeJD/soPVFjb1Z/2fLXW8svWhgFUTRfJdcTh2RzAXRW1U+jc1TDoMWV7R9Ky7TNOq+M6X+/8d9U/ueC4OQ0E8qVLAX9PuqHkJBjoCyPu/oBR4OBsL5wzjp7VAL/sD67rayXyCvBPhaHLki3bGp8YArDs9DT80fkf63U2DSlIQJB/vxE5wya/g2ZXOE3vBHHDZje6ftgaLXfCdwGpg; cssg=02a3138216e0a489a07ca553ff90202f; DG_ZUID=153D9D17-1508-340C-AB14-EC508BB36147; DG_HID=1B9C2996-D7E4-3599-B86E-72A5A3794B71; bm_sv=2A7D6AD1AB6E389CE7AC44C5D7E6254B~3TxK8epjCmooJOG8WhmID095v/QpwM6ej7zYusqpxQJ7QJNwIICzLm5CnPt5/wKrK7ntNQSSbeDC7+X5HsZmO/5kIXlh9NVchDEt4oEAEeiAv2GVy6cuLJeZuMGKY1aLU6FLA86PpnhP1j36xcXSzA; __gads=ID=2cba914e7afdca11:T=1572316897:S=ALNI_MbPpJF60XxD8BHotZgJijnsbQzW2g; DG_IID=0976C962-8B26-3FC2-BA66-AD38DA573419; DG_UID=A91ED65D-59E1-3337-A08B-F00EA374EE3C; DG_SID=58.245.111.48:3TqyDqyvY55n/aretixtwy2TPrgYm+0uKL2zWVz09TM; JSESSIONID=4BF2D5DBE683BE9E47244394197CEC33; npii=btguid/02a3138216e0a489a07ca553ff90202f617a10e9^cguid/02a3136316e0a4cc4f84235afaf2b54f617a10e9^; dp1=bpbf/%23e000c000008100020000005f98dd6a^u1p/QEBfX0BAX19AQA**617a10ea^bl/US617a10ea^; ns1=BAQAAAW3rnQDlAAaAANgATF+Y3WpjNzJ8NjAxXjE1NzIwMDIyNzIxODZeXjFeM3wyfDV8NHw3fDExXjFeMl40XjNeMTJeMTJeMl4xXjFeMF4xXjBeMV42NDQyNDU5MDc1I5J9qKs+mziVjBsSS6b3QHuf1Ew*; s=CgAD4ACBduPtqMDJhMzEzODIxNmUwYTQ4OWEwN2NhNTUzZmY5MDIwMmbvIo21; nonsession=BAQAAAW3rnQDlAAaAAAgAHF3fNuoxNTcyMzE3NjcxeDM2MjIxMjM5NjEyOHgweDJOAMoAIGF6EOowMmEzMTM4MjE2ZTBhNDg5YTA3Y2E1NTNmZjkwMjAyZgAzAAlfmN1qOTAwMjIsVVNBAMsAAl23sPIzNI9PxqnhAG1vTJUKm+yM58qkW3dN; ds2=ssts/1572317694451^; ebay=%5Ecv%3D15555%5Ejs%3D1%5Esbf%3D%2310000100000%5E'
    }

    proxy_url = ''
    proxy_type = ''

    def __init__(self, proxy_type=None, proxy_url=None, *args, **kwargs):
        super(ebaySpider, self).__init__(*args, **kwargs)

        self.proxy_type = proxy_type
        self.proxy_url = proxy_url
        print(proxy_type)
        print(proxy_url)

    def start_requests(self):
        # proxy_text = requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt').text
        # list_proxy_temp = proxy_text.split('\n')
        #
        # for line in list_proxy_temp:
        #     if line.strip() !='' and (line.strip()[-1] == '+' or line.strip()[-1] == '-'):
        #         ip = line.strip().split(':')[0].replace(' ', '')
        #         port = line.split(':')[-1].split(' ')[0]
        #         self.list_proxy.append('http://'+ip+':'+port)

        for i in range(12):
            self.field_names.append('img' + str(i + 1))

        # yield Request(self.start_url, self.parse)

        for data_list in self.existing_data_list:
            # if data_list[8] == 'success':
            #     continue
            url = data_list[5]
            next_count = 1
            # if data_list[8] != 'success' and data_list[6]:
            if data_list[6]:
                url = data_list[6]
                next_count = data_list[7]

            # proxy = random.choice(self.list_proxy)
            yield Request(url, self.parse, meta={"next_count": next_count, 'url': data_list[5], 'data_list': data_list})

    def parse(self, response):
        try:
            if response.body == '<html><head></head><body></body></html>' or (not response.xpath('//div[@id="ConstraintCaptionContainer"]')):
                response.meta['again'] = True
                yield Request(response.url, self.parse, meta=response.meta, dont_filter=True )
                return
        except:
            response.meta['again'] = True
            yield Request(response.url, self.parse, meta=response.meta, dont_filter=True )
            return

        item_tags = response.xpath('//ul[@id="ListViewInner"]/li')

        data_list = response.meta.get('data_list')

        if (not data_list[7]) or (data_list[7] <= response.meta.get('next_count')):
            bad_resp = False

            for item_tag in item_tags:
                item_url = item_tag.xpath('./h3/a/@href').extract_first()
                listingid = item_tag.xpath('./@listingid').extract_first()
                lvprice = item_tag.xpath('.//li[@class="lvprice prc"]//text()').re(r'[\d.,]+')
                currency_unit = '$'
                if lvprice:
                    lvprice = lvprice[0]
                else:
                    lvprice = ''

                # item_url = 'https://www.ebay.com/itm/External-Portable-DVD-Combo-Player-CD-RW-Burner-Drive-USB-2-for-Windows-XP-7-8/362187069507?hash=item5454081843:g:-yUAAOSw4gZdcaT0'
                id_got = item_url.split('?')[0].split('/')[-1]
                if id_got in self.item_ids_got_already:
                    print('\n####################################################')
                    print('Exists product ID: ' + id_got)
                    print('Detail URL: ' + item_url)
                    print('####################################################\n')
                    continue

                resp_1 = requests.get(item_url, headers= self.headers)
                if resp_1.status_code == 200:
                    resp = TextResponse(url=item_url,
                                        body=resp_1.text,
                                        encoding='utf-8')

                    title = resp.xpath('//h1[@id="itemTitle"]/text()').extract_first()

                    item = OrderedDict()
                    for field_name in self.field_names:
                        item[field_name] = ''
                    item['store_id'] = data_list[3]

                    item['specifics_html'] = resp.xpath('//div[@id="viTabs_0_is"]').extract_first()
                    itemAttr_tds = resp.xpath('//div[@id="viTabs_0_is"]/div/table//td')
                    for i, itemAttr_td in enumerate(itemAttr_tds):
                        td_label = itemAttr_td.xpath('./text()').extract_first()
                        if not td_label:
                            continue
                        vals = []
                        if i + 1 <= len(itemAttr_tds) - 1:
                            temps = itemAttr_tds[i + 1].xpath('.//text()').extract()
                            for v in temps:
                                v = v.strip()
                                if v:
                                    vals.append(v)

                        item['item_location_country'] = 'USA'

                        if 'Country/Region of Manufacture' in td_label:
                            if vals:
                                item['item_location_country'] = ' '.join(vals)
                        elif 'UPC:' in td_label.strip()[:4]:
                            if vals:
                                item['upc'] = ' '.join(vals)
                        elif 'Brand:' == td_label.strip()[:6]:
                            if vals:
                                item['brand'] = ' '.join(vals)
                        elif 'MPN:' in td_label.strip()[:4]:
                            if vals:
                                item['mpn'] = ' '.join(vals)
                        elif 'Model' in td_label.strip()[:5]:
                            if vals:
                                item['model'] = ' '.join(vals)

                    item['product_number'] = listingid
                    item['is_variation'] = 0
                    item['variation_theme'] = ''
                    item['variation_value'] = ''

                    item['detail_url'] = item_url
                    item['full_category_path'] = data_list[4]

                    item['item_location_city'] = ''

                    item['item_title'] = title

                    item['unit_price'] = lvprice
                    item['shipping_cost'] = 0
                    item['currency_code'] = currency_unit

                    variation_themes = []
                    variation_values_dict = {}

                    tv_brands = resp.xpath('//select[@name="TV Brand:"]/option[contains(@id,"msku-opt-")]/text()').extract()
                    if tv_brands:
                        variation_themes.append('TV Brand')
                        variation_values_dict['TV Brand'] = tv_brands

                    imageModule = resp.xpath('//div[@id="vi_main_img_fs"]/ul/li//img/@src').extract()
                    for i, imagePath in enumerate(imageModule):
                        if i > 11:
                            break
                        img_title = 'img' + str(i + 1)
                        item[img_title] = imagePath.replace('s-l64.jpg', 's-l500.jpg')

                    desc_ifr_url = resp.xpath('//iframe[@id="desc_ifr"]/@src').extract_first()

                    resp_2 = requests.get(desc_ifr_url)
                    if resp_2.status_code == 200:
                        respDesc = TextResponse(url=desc_ifr_url,
                                            body=resp_2.text,
                                            encoding='utf-8')
                        specsModule_props = respDesc.xpath('//div[@id="patemplate_itemspecifics"]/table/tr')

                        for specsModule_prop in specsModule_props:
                            variation_values = []
                            attrName = specsModule_prop.xpath('./th/text()').extract_first()
                            attrValue = specsModule_prop.xpath('./td/text()').extract_first()
                            if 'Size' in attrName:
                                variation_themes.append('Size')
                                variation_values.append(attrValue)
                                variation_values_dict['Size'] = variation_values
                            # elif 'Type' in attrName:
                            #     variation_theme.append('Type')
                            #     variation_values.append(attrValue)
                            elif 'Color' in attrName:
                                variation_themes.append('Color')
                                variation_values.append(attrValue)
                                variation_values_dict['Color'] = variation_values
                        # if variation_theme:
                        #     item['is_variation'] = 1
                        #     item['variation_theme'] = variation_theme[0]
                        #     item['variation_value'] = variation_values[0]

                        if item['variation_value']:
                            item['parent_product_number'] = '{}-{}'.format(listingid, item['variation_value'].replace('.', '-').replace(' ', '-').replace('/', '-'))
                        else:
                            item['parent_product_number'] = item['product_number']

                        # main_txts = respDesc.xpath('//div[@id="patemplate_description"]//div[@class="patemplatebox_bodyin"]/div/text()').extract()
                        main_txt = respDesc.xpath('//div[@id="patemplate_description"]//div[@class="patemplatebox_bodyin"]/div').extract_first()
                        if main_txt:
                            main_txt = main_txt.replace('\n', '').replace('<div id="patemplate_itemspecifics">', '').replace('<div id="pastingspan1">', '').replace('<div>', '').replace('</div>', '').strip()
                            table_txts = re.findall('<table(.*)<\/table>', main_txt)
                            for table_txt in table_txts:
                                main_txt = main_txt.replace('<table' + table_txt + '</table>', '')

                            style_txts = re.findall(' style="(.*?)"', main_txt)
                            style_txts = list(dict.fromkeys(style_txts))
                            for style_txt in style_txts:
                                main_txt = main_txt.replace(' style="{}"'.format(style_txt), '')
                            main_txt = main_txt.replace('<span>', '').replace('</span>', '')

                            main_txt = main_txt.replace('<!--PA4_ItemSpecifics_Begin-->', '').replace('<!--PA4_ItemSpecifics_End-->', '').replace('<!--PA4_Description_Begin-->', '').replace('<!--PA4_Description_End-->', '')

                            strong3_txts = re.findall('<strong><strong><strong>(.*?)<\/strong>(.*?)<\/strong>(.*?)<\/strong>', main_txt)
                            strong3_txts = list(dict.fromkeys(strong3_txts))
                            for style_txt in strong3_txts:
                                main_txt = main_txt.replace('<strong><strong><strong>{}</strong>{}</strong>{}</strong>'.format(style_txt[0], style_txt[1], style_txt[2]),
                                                            '<strong>{}</strong>'.format(''.join(style_txt)))
                            strong2_txts = re.findall('<strong><strong>(.*?)<\/strong>(.*?)<\/strong>', main_txt)
                            strong2_txts = list(dict.fromkeys(strong2_txts))
                            for style_txt in strong2_txts:
                                main_txt = main_txt.replace('<strong><strong>{}</strong>{}</strong>'.format(style_txt[0], style_txt[1]),
                                                            '<strong>{}</strong>'.format(''.join(style_txt)))

                        item['description_text'] = main_txt
                        item['description_html'] = respDesc.xpath('//div[@id="patemplate_description"]').extract_first()

                        if not variation_themes:
                            item['is_variation'] = 0
                        else:
                            item['is_variation'] = 1
                            item['variation_theme'] = ','.join(variation_themes)
                            variation_values = []
                            for variation_theme in variation_themes:
                                variation_values.extend(variation_values_dict[variation_theme])
                            item['variation_value'] = ','.join(variation_values)

                        item['parent_product_number'] = '0'

                        yield item

                        product_number = item['product_number']

                        if variation_themes:
                            item['is_variation'] = 1
                            for variation_theme in variation_themes:
                                item['variation_theme'] = variation_theme
                                item['parent_product_number'] = product_number

                                for variation_value in variation_values_dict[variation_theme]:
                                    if variation_value[len(variation_value) - 3: len(variation_value)] == '...':
                                        variation_value = variation_value.split('(')[0]
                                    item['variation_value'] = variation_value
                                    if variation_value[len(variation_value) - 1: len(variation_value)] == ')':
                                        variation_value = variation_value[: len(variation_value) - 1]
                                    if '(' in variation_value:
                                        temps_txt = variation_value.split('(')
                                        variation_value = '{}({}'.format(temps_txt[0], temps_txt[1].lower())

                                    variation_value = variation_value.replace('(', '-').replace(')', '-').replace('.', '-').replace('*', '-').replace(' ', '-').replace('/', '-')\
                                        .replace('&', '').replace('"', '').replace('--', '-').replace('---', '-').replace('----', '-')

                                    item['product_number'] = '{}-{}'.format(product_number, variation_value)
                                    yield item

                    # yield Request(desc_ifr_url, self.parseDescription, meta={'item': item})

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
            # break

        next_url = response.xpath('//a[@class="gspr next"]/@href').extract_first()
        if next_url:
            next_count = response.meta.get('next_count')
            # update query ##########################
            update_query = 'UPDATE crawl_list SET last_crawl_url = "{}", last_page = {} WHERE uid={};'.format(next_url, str(next_count + 1), str(data_list[0]))
            result = self.cursor.execute(update_query)
            self.connection.commit()
            ###################################

            print('next page: ' + str(next_count + 1))

            yield Request(next_url, self.parse, meta={"next_count": next_count + 1, 'url': next_url,
                                                      'data_list': response.meta.get('data_list')})

    def err_parse(self, response):
        ban_proxy = response.request.meta.get('proxy')
        if ban_proxy:
            ban_proxy = response.request.meta['proxy'].replace('http://', '')
        # if '154.16.' in ban_proxy:
        #     ban_proxy = ban_proxy.replace('http://', 'http://eolivr4:bntlyy3@')
        if ban_proxy in self.list_proxy:
            self.list_proxy.remove(ban_proxy)
        if len(self.list_proxy) < 1:
            proxy_text = requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt').text
            list_proxy_temp = proxy_text.split('\n')
            self.list_proxy = []
            for line in list_proxy_temp:
                if line.strip() !='' and (line.strip()[-1] == '+' or line.strip()[-1] == '-'):
                    ip = line.strip().split(':')[0].replace(' ', '')
                    port = line.split(':')[-1].split(' ')[0]
                    self.list_proxy.append('http://'+ip+':'+port)

        proxy = random.choice(self.list_proxy)
        # response.request.meta['proxy'] = proxy
        print ('err proxy: ' + proxy)
        response.request.meta['proxy'] = proxy
        if not 'errpg' in response.request.url :
            yield Request(response.request.meta['url'],
                          callback=self.parse,
                          meta=response.request.meta,
                          dont_filter=True,
                          errback=self.err_parse)