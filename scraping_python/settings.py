# -*- coding: utf-8 -*-

# Scrapy settings for scraping_python project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scraping_python'

SPIDER_MODULES = ['scraping_python.spiders']
NEWSPIDER_MODULE = 'scraping_python.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scraping_python (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scraping_python.middlewares.ScrapingPythonSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scraping_python.middlewares.ScrapingPythonDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scraping_python.pipelines.ScrapingPythonPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DOWNLOADER_MIDDLEWARES = {
   'scraping_python.middlewares.selenium_middleware.SeleniumMiddleware': 1,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350
}

RETRY_TIMES = 10
RETRY_HTTP_CODES = [502, 503, 504, 522, 524, 408, 429, 400, 403]

DATABASE = {
    'drivername': 'mysql',
    'host': 'localhost',
    'port': '3306',
    'username': 'root',
    'password': '',
    'database': 'xdata'
}

proxies = ['gcm:Money102!@138.94.217.121:80', 'gcm:Money102!@107.172.49.125:80', 'gcm:Money102!@138.94.217.88:80', 'gcm:Money102!@155.94.138.50:80', 'gcm:Money102!@154.16.53.104:80', 'gcm:Money102!@173.254.225.183:80', 'gcm:Money102!@206.41.174.205:80', 'gcm:Money102!@206.41.173.29:80', 'gcm:Money102!@104.223.127.170:80', 'gcm:Money102!@138.94.217.60:80', 'gcm:Money102!@185.198.223.43:80', 'gcm:Money102!@206.41.173.218:80', 'gcm:Money102!@191.96.243.220:80', 'gcm:Money102!@104.223.127.165:80', 'gcm:Money102!@198.12.82.181:80', 'gcm:Money102!@162.253.64.59:80', 'gcm:Money102!@209.99.164.57:80', 'gcm:Money102!@45.61.164.250:80', 'gcm:Money102!@179.61.144.224:80', 'gcm:Money102!@154.16.55.58:80', 'gcm:Money102!@209.99.164.194:80', 'gcm:Money102!@107.150.89.53:80', 'gcm:Money102!@179.61.140.224:80', 'gcm:Money102!@185.198.223.213:80', 'gcm:Money102!@138.94.217.15:80', 'gcm:Money102!@179.61.180.187:80', 'gcm:Money102!@23.105.159.59:80', 'gcm:Money102!@104.223.82.161:80', 'gcm:Money102!@104.223.42.126:80', 'gcm:Money102!@179.61.140.218:80', 'gcm:Money102!@154.16.69.121:80', 'gcm:Money102!@206.41.173.251:80', 'gcm:Money102!@154.16.55.92:80', 'gcm:Money102!@179.61.179.180:80', 'gcm:Money102!@198.46.201.252:80', 'gcm:Money102!@179.61.179.176:80', 'gcm:Money102!@172.245.194.42:80', 'gcm:Money102!@96.8.120.219:80', 'gcm:Money102!@155.94.138.214:80', 'gcm:Money102!@138.94.217.137:80', 'gcm:Money102!@96.8.122.56:80', 'gcm:Money102!@107.150.89.202:80', 'gcm:Money102!@138.94.217.28:80', 'gcm:Money102!@107.161.85.32:80', 'gcm:Money102!@107.161.85.17:80', 'gcm:Money102!@184.175.219.204:80', 'gcm:Money102!@107.172.52.131:80', 'gcm:Money102!@185.161.71.125:80', 'gcm:Money102!@196.247.18.222:80', 'gcm:Money102!@23.105.159.106:80', 'gcm:Money102!@206.41.174.119:80', 'gcm:Money102!@23.105.159.158:80', 'gcm:Money102!@172.245.250.160:80', 'gcm:Money102!@209.99.164.44:80', 'gcm:Money102!@192.210.188.147:80', 'gcm:Money102!@154.16.55.71:80', 'gcm:Money102!@179.61.180.166:80', 'gcm:Money102!@104.223.42.68:80', 'gcm:Money102!@162.253.64.136:80', 'gcm:Money102!@45.61.166.76:80', 'gcm:Money102!@155.94.138.20:80', 'gcm:Money102!@104.223.127.163:80', 'gcm:Money102!@23.94.184.207:80', 'gcm:Money102!@162.253.64.36:80', 'gcm:Money102!@162.212.172.141:80', 'gcm:Money102!@172.245.250.136:80', 'gcm:Money102!@23.105.159.218:80', 'gcm:Money102!@208.91.109.190:80', 'gcm:Money102!@104.223.69.230:80', 'gcm:Money102!@107.172.52.185:80', 'gcm:Money102!@184.175.219.44:80', 'gcm:Money102!@184.175.219.13:80', 'gcm:Money102!@154.16.69.10:80', 'gcm:Money102!@209.99.164.7:80', 'gcm:Money102!@206.41.174.160:80', 'gcm:Money102!@23.105.159.230:80', 'gcm:Money102!@107.172.52.119:80', 'gcm:Money102!@192.210.188.164:80', 'gcm:Money102!@192.161.59.208:80', 'gcm:Money102!@104.223.127.134:80', 'gcm:Money102!@23.94.184.212:80', 'gcm:Money102!@209.99.164.207:80', 'gcm:Money102!@179.61.140.233:80', 'gcm:Money102!@23.105.159.232:80', 'gcm:Money102!@154.16.69.109:80', 'gcm:Money102!@155.94.138.41:80', 'gcm:Money102!@185.198.223.45:80', 'gcm:Money102!@96.8.120.215:80', 'gcm:Money102!@107.172.49.123:80', 'gcm:Money102!@23.95.128.143:80', 'gcm:Money102!@155.94.194.111:80', 'gcm:Money102!@138.94.217.119:80', 'gcm:Money102!@179.61.180.180:80', 'gcm:Money102!@107.161.85.254:80', 'gcm:Money102!@206.41.173.152:80', 'gcm:Money102!@107.172.49.109:80', 'gcm:Money102!@192.161.59.223:80', 'gcm:Money102!@104.129.40.68:80', 'gcm:Money102!@107.161.85.202:80', 'gcm:Money102!@107.172.49.94:80', 'gcm:Money102!@45.61.168.208:80', 'gcm:Money102!@23.105.183.94:80', 'gcm:Money102!@23.229.36.112:80', 'gcm:Money102!@23.108.86.31:80', 'gcm:Money102!@45.61.173.152:80', 'gcm:Money102!@209.99.169.252:80', 'gcm:Money102!@45.61.170.120:80', 'gcm:Money102!@45.61.168.145:80', 'gcm:Money102!@209.242.217.72:80', 'gcm:Money102!@45.61.168.220:80', 'gcm:Money102!@45.61.172.123:80', 'gcm:Money102!@209.242.221.151:80', 'gcm:Money102!@45.61.174.232:80', 'gcm:Money102!@107.175.13.102:80', 'gcm:Money102!@45.61.185.57:80', 'gcm:Money102!@23.108.86.20:80', 'gcm:Money102!@209.242.223.104:80', 'gcm:Money102!@107.172.225.29:80', 'gcm:Money102!@45.61.184.135:80', 'gcm:Money102!@23.105.159.6:80', 'gcm:Money102!@45.61.173.130:80', 'gcm:Money102!@45.61.170.82:80', 'gcm:Money102!@209.242.222.10:80', 'gcm:Money102!@209.99.168.151:80', 'gcm:Money102!@23.229.27.85:80', 'gcm:Money102!@75.75.235.248:80', 'gcm:Money102!@45.61.170.25:80', 'gcm:Money102!@23.108.233.159:80', 'gcm:Money102!@209.242.222.59:80', 'gcm:Money102!@209.99.171.135:80', 'gcm:Money102!@209.99.171.170:80', 'gcm:Money102!@23.229.56.74:80', 'gcm:Money102!@23.105.183.238:80', 'gcm:Money102!@23.105.183.135:80', 'gcm:Money102!@45.61.185.58:80', 'gcm:Money102!@45.61.187.212:80', 'gcm:Money102!@45.61.169.34:80', 'gcm:Money102!@209.242.223.81:80', 'gcm:Money102!@23.231.32.107:80', 'gcm:Money102!@45.61.184.48:80', 'gcm:Money102!@45.61.186.71:80', 'gcm:Money102!@209.242.223.131:80', 'gcm:Money102!@107.172.225.16:80', 'gcm:Money102!@45.61.186.113:80', 'gcm:Money102!@23.108.86.79:80', 'gcm:Money102!@23.229.52.39:80', 'gcm:Money102!@209.242.221.66:80', 'gcm:Money102!@23.231.32.210:80', 'gcm:Money102!@209.99.171.226:80', 'gcm:Money102!@23.94.75.156:80', 'gcm:Money102!@209.99.168.178:80', 'gcm:Money102!@23.105.183.241:80', 'gcm:Money102!@209.99.169.200:80', 'gcm:Money102!@209.99.173.71:80', 'gcm:Money102!@23.105.159.47:80', 'gcm:Money102!@209.99.170.149:80', 'gcm:Money102!@64.44.50.160:80', 'gcm:Money102!@209.99.170.228:80', 'gcm:Money102!@209.242.217.110:80', 'gcm:Money102!@209.242.222.138:80', 'gcm:Money102!@23.231.32.145:80', 'gcm:Money102!@23.105.159.70:80', 'gcm:Money102!@64.44.50.237:80', 'gcm:Money102!@45.61.171.188:80', 'gcm:Money102!@45.61.184.160:80', 'gcm:Money102!@23.231.15.167:80', 'gcm:Money102!@209.242.223.169:80', 'gcm:Money102!@45.61.169.35:80', 'gcm:Money102!@209.99.168.223:80', 'gcm:Money102!@23.94.75.223:80', 'gcm:Money102!@209.242.217.176:80', 'gcm:Money102!@209.99.168.228:80', 'gcm:Money102!@23.229.52.50:80', 'gcm:Money102!@209.242.222.27:80', 'gcm:Money102!@107.175.13.78:80', 'gcm:Money102!@209.242.217.173:80', 'gcm:Money102!@23.231.32.18:80', 'gcm:Money102!@209.99.171.178:80', 'gcm:Money102!@45.61.171.27:80', 'gcm:Money102!@209.99.169.27:80', 'gcm:Money102!@23.229.58.59:80', 'gcm:Money102!@45.61.174.50:80', 'gcm:Money102!@209.242.221.189:80', 'gcm:Money102!@23.108.233.89:80', 'gcm:Money102!@209.242.221.198:80', 'gcm:Money102!@209.99.173.236:80', 'gcm:Money102!@209.99.169.242:80', 'gcm:Money102!@23.231.15.209:80', 'gcm:Money102!@23.94.10.9:80', 'gcm:Money102!@209.99.173.33:80', 'gcm:Money102!@107.172.225.46:80', 'gcm:Money102!@23.231.15.130:80', 'gcm:Money102!@45.61.174.197:80', 'gcm:Money102!@23.105.159.28:80', 'gcm:Money102!@209.99.170.104:80', 'gcm:Money102!@209.99.170.41:80', 'gcm:Money102!@23.108.233.18:80', 'gcm:Money102!@23.108.86.84:80', 'gcm:Money102!@23.231.15.117:80', 'gcm:Money102!@45.61.172.80:80','gcm:Money102!@138.94.218.91:80','gcm:Money102!@108.170.11.244:80','gcm:Money102!@181.214.89.97:80','gcm:Money102!@198.144.178.210:80','gcm:Money102!@184.175.219.79:80','gcm:Money102!@185.161.71.124:80','gcm:Money102!@200.10.37.47:80','gcm:Money102!@209.242.219.91:80','gcm:Money102!@196.196.86.145:80','gcm:Money102!@138.122.192.57:80','gcm:Money102!@107.172.225.50:80','gcm:Money102!@155.94.139.85:80','gcm:Money102!@184.95.48.157:80','gcm:Money102!@199.119.225.29:80','gcm:Money102!@154.16.24.136:80','gcm:Money102!@171.22.121.60:80','gcm:Money102!@165.231.54.160:80','gcm:Money102!@181.214.89.115:80','gcm:Money102!@155.94.139.122:80','gcm:Money102!@50.115.166.239:80','gcm:Money102!@179.61.160.183:80','gcm:Money102!@154.16.55.152:80','gcm:Money102!@171.22.121.231:80','gcm:Money102!@107.172.238.188:80','gcm:Money102!@179.61.160.174:80','gcm:Money102!@131.153.31.221:80','gcm:Money102!@171.22.121.91:80','gcm:Money102!@155.94.139.11:80','gcm:Money102!@138.94.218.204:80','gcm:Money102!@167.88.113.251:80','gcm:Money102!@181.214.89.85:80','gcm:Money102!@104.129.13.116:80','gcm:Money102!@108.170.11.250:80','gcm:Money102!@200.10.37.146:80','gcm:Money102!@131.153.31.218:80','gcm:Money102!@192.210.140.29:80','gcm:Money102!@185.161.71.85:80','gcm:Money102!@107.172.225.12:80','gcm:Money102!@45.61.160.84:80','gcm:Money102!@198.144.178.224:80','gcm:Money102!@181.214.89.87:80','gcm:Money102!@138.122.192.62:80','gcm:Money102!@104.129.15.160:80','gcm:Money102!@104.129.13.82:80','gcm:Money102!@154.16.24.150:80','gcm:Money102!@45.61.161.37:80','gcm:Money102!@200.10.37.251:80','gcm:Money102!@158.222.14.251:80','gcm:Money102!@200.10.37.58:80','gcm:Money102!@179.61.160.203:80','gcm:Money102!@138.94.218.84:80','gcm:Money102!@158.222.14.52:80','gcm:Money102!@154.16.24.138:80','gcm:Money102!@45.61.160.77:80','gcm:Money102!@138.122.192.2:80','gcm:Money102!@200.10.37.35:80','gcm:Money102!@23.231.110.194:80','gcm:Money102!@131.153.31.220:80','gcm:Money102!@107.172.238.180:80','gcm:Money102!@104.129.9.57:80','gcm:Money102!@158.222.14.31:80','gcm:Money102!@108.170.11.226:80','gcm:Money102!@172.245.10.15:80','gcm:Money102!@104.129.15.187:80','gcm:Money102!@191.101.199.84:80','gcm:Money102!@179.61.160.199:80','gcm:Money102!@154.16.24.176:80','gcm:Money102!@209.242.219.138:80','gcm:Money102!@165.231.54.157:80','gcm:Money102!@171.22.121.113:80','gcm:Money102!@179.61.160.205:80','gcm:Money102!@181.214.89.98:80','gcm:Money102!@171.22.121.88:80','gcm:Money102!@204.45.182.22:80','gcm:Money102!@172.245.10.60:80','gcm:Money102!@64.38.250.190:80','gcm:Money102!@179.61.160.197:80','gcm:Money102!@209.242.219.244:80','gcm:Money102!@181.214.89.105:80','gcm:Money102!@173.0.52.249:80','gcm:Money102!@185.161.71.159:80','gcm:Money102!@155.94.139.235:80','gcm:Money102!@185.161.71.10:80','gcm:Money102!@104.160.31.231:80','gcm:Money102!@179.61.160.194:80','gcm:Money102!@158.222.14.173:80','gcm:Money102!@154.16.91.243:80','gcm:Money102!@198.144.180.105:80','gcm:Money102!@23.231.110.188:80','gcm:Money102!@172.245.10.58:80','gcm:Money102!@168.235.70.179:80','gcm:Money102!@192.210.140.28:80','gcm:Money102!@198.144.180.86:80','gcm:Money102!@104.129.15.162:80','gcm:Money102!@23.231.110.225:80','gcm:Money102!@23.231.110.221:80','gcm:Money102!@138.122.192.58:80','gcm:Money102!@198.144.178.234:80','gcm:Money102!@138.94.218.248:80','gcm:Money102!@138.122.192.61:80','gcm:Money102!@107.172.225.30:80','gcm:Money102!@107.172.238.167:80','gcm:Money102!@104.160.29.110:80','gcm:Money102!@104.160.29.118:80','gcm:Money102!@158.222.1.90:80','gcm:Money102!@192.210.140.27:80','gcm:Money102!@158.222.14.169:80','gcm:Money102!@104.160.9.59:80','gcm:Money102!@64.38.250.181:80','gcm:Money102!@107.172.225.55:80','gcm:Money102!@181.214.89.90:80','gcm:Money102!@185.161.71.171:80','gcm:Money102!@191.101.199.22:80','gcm:Money102!@196.196.86.236:80','gcm:Money102!@107.172.238.182:80','gcm:Money102!@107.172.225.58:80','gcm:Money102!@154.16.24.139:80','gcm:Money102!@196.196.86.132:80','gcm:Money102!@198.144.178.254:80','gcm:Money102!@209.242.219.160:80','gcm:Money102!@196.196.86.189:80','gcm:Money102!@154.16.24.188:80','gcm:Money102!@191.101.199.72:80','gcm:Money102!@104.129.13.103:80','gcm:Money102!@198.144.178.247:80','gcm:Money102!@191.101.199.114:80','gcm:Money102!@155.94.139.70:80','gcm:Money102!@171.22.121.29:80','gcm:Money102!@179.61.160.209:80','gcm:Money102!@107.172.238.155:80','gcm:Money102!@107.172.225.62:80','gcm:Money102!@184.95.48.156:80','gcm:Money102!@23.231.110.245:80','gcm:Money102!@209.242.219.208:80','gcm:Money102!@108.170.11.239:80','gcm:Money102!@154.16.24.151:80','gcm:Money102!@23.231.110.243:80','gcm:Money102!@104.160.31.241:80','gcm:Money102!@200.10.37.78:80','gcm:Money102!@200.10.37.88:80','gcm:Money102!@209.242.219.158:80','gcm:Money102!@64.38.250.188:80','gcm:Money102!@155.94.139.203:80','gcm:Money102!@191.101.199.101:80','gcm:Money102!@185.161.71.240:80','gcm:Money102!@209.242.219.171:80','gcm:Money102!@154.16.91.246:80','gcm:Money102!@158.222.14.189:80','gcm:Money102!@191.101.199.80:80','gcm:Money102!@192.210.140.30:80','gcm:Money102!@138.94.218.28:80','gcm:Money102!@179.61.160.216:80','gcm:Money102!@184.175.219.178:80','gcm:Money102!@45.61.161.9:80','gcm:Money102!@181.214.89.121:80','gcm:Money102!@23.231.110.160:80','gcm:Money102!@155.94.139.171:80','gcm:Money102!@181.214.89.67:80','gcm:Money102!@138.94.218.21:80','gcm:Money102!@196.196.86.184:80','gcm:Money102!@75.127.5.119:80','gcm:Money102!@23.231.110.163:80','gcm:Money102!@199.119.225.19:80','gcm:Money102!@107.172.238.174:80','gcm:Money102!@138.94.218.192:80','gcm:Money102!@45.61.163.134:80','gcm:Money102!@45.61.161.19:80','gcm:Money102!@191.101.199.73:80','gcm:Money102!@192.210.140.25:80','gcm:Money102!@185.161.71.19:80','gcm:Money102!@154.16.55.145:80','gcm:Money102!@196.196.86.195:80','gcm:Money102!@165.231.54.185:80','gcm:Money102!@45.61.162.196:80','gcm:Money102!@165.231.54.178:80','gcm:Money102!@64.38.250.172:80','gcm:Money102!@45.61.161.23:80','gcm:Money102!@108.170.11.254:80','gcm:Money102!@200.10.37.179:80','gcm:Money102!@209.242.219.249:80','gcm:Money102!@191.101.199.14:80','gcm:Money102!@158.222.14.116:80','gcm:Money102!@171.22.121.66:80','gcm:Money102!@138.122.192.3:80','gcm:Money102!@138.122.192.7:80','gcm:Money102!@154.16.91.236:80','gcm:Money102!@104.129.13.80:80','gcm:Money102!@165.231.54.162:80','gcm:Money102!@107.172.238.187:80','gcm:Money102!@196.196.82.100:80','gcm:Money102!@171.22.121.11:80','gcm:Money102!@198.144.178.236:80','gcm:Money102!@196.196.86.34:80','gcm:Money102!@165.231.54.252:80','gcm:Money102!@155.94.147.236:80','gcm:Money102!@165.231.54.68:80','gcm:Money102!@131.153.31.219:80','gcm:Money102!@154.16.24.156:80','gcm:Money102!@138.94.218.182:80','gcm:Money102!@155.94.139.118:80']
