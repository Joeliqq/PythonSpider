# coding:UTF-8
__author__ = 'L'

# ----------------------------
#
#
#
#
# --------------------------------

import urllib2
import os
from  bs4 import BeautifulSoup
import re

def getSoup(URL):
    'URL为每个地区一页'
    request = urllib2.Request(URL)
    request.add_header('User-Agent', 'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50')
    html = urllib2.urlopen(request).read()
    soup = BeautifulSoup(html.decode('gb2312','ignore'))   # 增加编码方式防止乱码
    return soup

def getPerMonthURL(URL):
    '得到该地区每月空气质量的URL地址'
    soup = getSoup(URL)
    AllURL = []

    file = open('perMonth.txt', 'w')
    urllist = soup.find_all('a', title = re.compile("201.+"))  # 这个位置也可以使用正则表达式。
    for i in urllist:
        
        print i['title']
        print "http://www.tianqihoubao.com" + i['href']
    return

if __name__ == '__main__':
    url = 'http://www.tianqihoubao.com/aqi/beijing.html'
    getPerMonthURL(url)
