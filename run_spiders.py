# -*- coding: utf-8 -*-
#!/usr/bin/python
from multiprocessing import Pool
import os, sys


if __name__ == '__main__':
	spider_params = sys.argv
	print(spider_params)
	# print ">>>>> Starting {} spider".format(spider_name_params)
	if len(spider_params) > 2:
		command = 'scrapy crawl {} -a proxy_type={} -a proxy_url={}'.format(spider_params[1], spider_params[2], spider_params[3])
	else:
		command = 'scrapy crawl {}'.format(spider_params[1])

	os.system(command)
	# run_crawler(spider_params)
