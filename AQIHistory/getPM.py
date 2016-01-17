#  coding=UTF-8

#  -------------------------
#
#
#
#  -------------------------

import urllib2
import os
from bs4 import BeautifulSoup
import time

'''
    写文本编码
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_soup(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36')
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def save_text(url):
    soup = get_soup(url)
    filterURL = soup.find_all('tr', class_ = "zb_k_box_tr1")

    # print filterURL[0]

    file = open('PMTest.md', 'w+')     #  w  w+  文件要从循环外，否则只保存了最后一行、

    datafilter = soup.find_all('div', class_ = "zb_k_box_top")
    # print datafilter
    data = datafilter[0].find_all('p')
    print data[0].text

    # for i in filterURL:
    #     # print i
    #     city = i.find_all('td', width = "65")
    #     # print city[0].text          #           text 方法 取值
    #     polutants = i.find_all('td', width = "50")
    #     rank = i.find_all('td', width = "115", align = "center")
    #     value = i.find_all('td', width = "40")
    #     file.write(city[0].text + ';' + polutants[0].text + ';' + rank[0].text + ';' + value[0].text + '\n')
    # file.close()

if __name__ == '__main__':
    url = 'http://www.cnemc.cn/'
    save_text(url)
    print '日期：'+ time.strftime('%Y-%m-%d',time.localtime(time.time()))
