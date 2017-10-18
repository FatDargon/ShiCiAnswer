# -*- coding:UTF-8 -*-
'''
Created on 2016-3-8

@author: Administrator
'''

import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from datetime import *
import gzip
from StringIO import StringIO
import time
class Soup():
    def __init__(self, url, encoding='utf-8'):
        self.url = url
        # self.sleep_download_time = 10
        self.soup = BeautifulSoup("", "html.parser")
        self.encoding = encoding
    def my_gzip(self,data):
        buf = StringIO(data)
        f = gzip.GzipFile(fileobj=buf)
        return f.read()
    def get_soup(self):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        #    'Host': "pinghot.qq.com",
            'Host': 'stock.caijing.com.cn',
            'Accept-Encoding':'gzip, deflate',
            'Referer': "http://stock.caijing.com.cn/20170605/4280521.shtml",
            'X-Requested-With': "XMLHttpRequest",
            'Cookie': 'bdshare_firstime=1506503322793; afpCT=1; _ga=GA1.3.385891441.1506503323; _gid=GA1.3.1841637955.1506688812; _gat=1; Hm_lvt_b0bfb2d8ed2ed295c7354d304ad369f1=1506503323,1506688812; Hm_lpvt_b0bfb2d8ed2ed295c7354d304ad369f1=1506690611'
        }
        try:
            # time.sleep(self.sleep_download_time)
            request = urllib2.Request(self.url, headers=headers)
            response = urllib2.urlopen(request)
            if_gzip = response.info().get('Content-Encoding')
            if self.encoding == '':
                contents = response.read()
            else:
                contents = response.read().decode(self.encoding)
            if if_gzip == 'gzip':
#                 print 'gzip'
                contents = self.my_gzip(contents)            
            self.soup = BeautifulSoup(contents, "html.parser")
            # request.close()
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
        return self.soup 

# soup = Soup('http://lufuli.net/chuchu/').get_soup()
# print soup
