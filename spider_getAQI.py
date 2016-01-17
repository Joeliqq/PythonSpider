# coding:UTF-8
__author__ = 'L'
#  -----------------
#
#
#
#
#  ------------------

import urllib2
import os
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )       #  防止写文件编码错误写出错。

def get_soup(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36')
    html = urllib2.urlopen(request).read()
    soup = BeautifulSoup(html.decode('gb2312','ignore'), "html.parser")  # 跨平台要加上解析的方式？！
    return soup

def get_AQI(filename):
    soup = get_soup(url)
    # lines = soup.find_all('table', class_ = 'b')
    lines = soup.find_all('td')
    # print lines[-1]

    file = open(filename, 'w')
    for i in lines:
        # print str(i.text).strip()  #  strip()去掉两端空格。 strip('\n') 去掉回车、
        file.write(str(i.text).strip() + '\n')
        # perline = i.find_all('td')
        # for j in perline:
        #     print j.text
    # file.close
    return

if __name__ == '__main__':
    filename = u'2013年10月北京PM2.5指数.txt'
     #  中文文件名或者目录。
    url = 'http://www.tianqihoubao.com/aqi/beijing-201511.html'  #  url ex
    get_AQI(filename)
