from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from scrapy.http import TextResponse
from scrapy.exceptions import CloseSpider
from scrapy import signals
from selenium.webdriver.chrome.options import Options
from datetime import date
import requests, random, time
import pickle

class SeleniumMiddleware(object):

    def __init__(self, s):
        # self.exec_path = 'chromedriver.exe'
        self.exec_path = 'phantomjs.exe'
        # self.exec_path = 'geckodriver.exe'
        self.first = False
###########################################################

    @classmethod
    def from_crawler(cls, crawler):
        obj = cls(crawler.settings)

        crawler.signals.connect(obj.spider_opened,
                                signal=signals.spider_opened)
        crawler.signals.connect(obj.spider_closed,
                                signal=signals.spider_closed)
        return obj

###########################################################

    def spider_opened(self, spider):
        if spider.use_selenium:
            self.d = self.init_driver()
            # try:
            #
            #     self.d = None
            # except TimeoutException:
            #     CloseSpider('PhantomJS Timeout Error!!!')

###########################################################

    def spider_closed(self, spider):
        if spider.use_selenium and self.d:
            pickle.dump( self.d.get_cookies() , open("cookies.pkl","wb"))
            self.d.quit()
###########################################################
    
    def process_request(self, request, spider):
        if spider.use_selenium:
            # while True:
            #     if self.d and request.meta.get('again'):
            #         self.d.close()
            #         self.d = None
            #         self.d = self.init_driver(spider.proxy_type, spider.proxy_url)
            #     elif not self.d:
            #         self.d = self.init_driver(spider.proxy_type, spider.proxy_url)
            #     # print "############################ Received url request from scrapy #####"
            #
            #     try:
            #         self.d.get(request.url)
            #         # self.d.delete_all_cookies()
            #         # cookies = pickle.load(open("cookies.pkl", "rb"))
            #         # for cookie in cookies:
            #         #     self.d.add_cookie(cookie)
            #         # self.d.get(request.url)
            #         # pickle.dump( self.d.get_cookies() , open("cookies.pkl","wb"))
            #         break
            #     except TimeoutException as e:
            #         print('TIMEOUT ERROR')
            # time.sleep(2)
            
            # lastHeight = self.d.execute_script("return document.body.scrollHeight")
            self.d.get(request.url)
            time.sleep(2)

            lastHeight = self.d.execute_script("return document.body.scrollHeight")
            while True:
                resl = self.d.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(7)
                newHeight = self.d.execute_script("return document.body.scrollHeight")
                if newHeight == lastHeight:
                    break
                lastHeight = newHeight
                break

            resp1 = TextResponse(url=self.d.current_url,
                                body=self.d.page_source,
                                encoding='utf-8')

            resp1.request = request.copy()
            
            return resp1

###########################################################
###########################################################

    def init_driver(self):
        # chrome_options = Options()
        # if proxy_type:
        #     if proxy_type == '-p':
        #         proxy_text = requests.get(proxy_url)
        #         proxy_text = proxy_text.text
        #         list_proxy_temp = proxy_text.split('\n')
        #
        #         list_proxy = []
        #         for line in list_proxy_temp:
        #             if line.strip() !='' and (line.strip()[-1] == '+' or line.strip()[-1] == '-'):
        #                 if 'US-' in line:
        #                     ip = line.strip().split(':')[0].replace(' ', '')
        #                     port = line.split(':')[-1].split(' ')[0]
        #                     list_proxy.append('http://' + ip+':'+port)
        #
        #         # # chrome_options.add_argument("window-size=3000,3000")
        #         # # chrome_options.add_argument("window-position=-10000,0")
        #         proxy = random.choice(list_proxy)
        #         print('Proxy: ' + proxy)
        #         # # chrome_options = WebDriverWait.ChromeOptions()
        #         chrome_options.add_argument('--proxy-server=%s' % proxy)
        #     else:
        #         chrome_options.add_argument('--proxy-server=socks5://' + proxy_url)
        d = webdriver.Chrome('chromedriver.exe')
        # d = webdriver.Firefox(executable_path='geckodriver.exe')
        # d = webdriver.PhantomJS(path)
        d.set_page_load_timeout(60)


        return d


    # def init_driver(self, proxy_type, proxy_url):
    #     chrome_options = Options()
    #     if proxy_type:
    #         if proxy_type == '-p':
    #             proxy_text = requests.get(proxy_url)
    #             proxy_text = proxy_text.text
    #             list_proxy_temp = proxy_text.split('\n')
    #
    #             list_proxy = []
    #             for line in list_proxy_temp:
    #                 if line.strip() !='' and (line.strip()[-1] == '+' or line.strip()[-1] == '-'):
    #                     if 'US-' in line:
    #                         ip = line.strip().split(':')[0].replace(' ', '')
    #                         port = line.split(':')[-1].split(' ')[0]
    #                         list_proxy.append('http://' + ip+':'+port)
    #
    #             # # chrome_options.add_argument("window-size=3000,3000")
    #             # # chrome_options.add_argument("window-position=-10000,0")
    #             proxy = random.choice(list_proxy)
    #             print('Proxy: ' + proxy)
    #             # # chrome_options = WebDriverWait.ChromeOptions()
    #             chrome_options.add_argument('--proxy-server=%s' % proxy)
    #         else:
    #             chrome_options.add_argument('--proxy-server=socks5://' + proxy_url)
    #     d = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    #     # d = webdriver.Firefox(executable_path='geckodriver.exe')
    #     # d = webdriver.PhantomJS(path)
    #     d.set_page_load_timeout(60)
    #
    #
    #     return d