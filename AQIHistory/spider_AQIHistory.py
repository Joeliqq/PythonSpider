# coding:UTF-8
__author__ = 'L'

# ----------------------------
#
# 得到该地区每月空气质量的月份和对应的URL地址，
# 存入列表
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
    soup = BeautifulSoup(html.decode('gb2312','ignore'), "html.parser")   # 增加编码方式防止乱码
    return soup
'''
存入文件防止出错后重新开始，可以继续执行。
保存到文件，分开执行，加强容错。单独执行利于调试与记录。
模块化。
'''
def getPerMonthURL(URL):
    '得到该地区每月空气质量的月份和对应的URL地址， 存入列表。'
    soup = getSoup(URL)
    monthlist = []

    urllist = soup.find_all('a', title = re.compile("201.+"))  # 这个位置也可以使用正则表达式。
    for i in urllist:
        # print i['title']
        # print "http://www.tianqihoubao.com" + i['href']
        monthname = i['title']
        monthurl = "http://www.tianqihoubao.com" + i['href']
        monthlist.append([monthname, monthurl])
    return monthlist

if __name__ == '__main__':
    url = 'http://www.tianqihoubao.com/aqi/beijing.html'
    getPerMonthURL(url)
