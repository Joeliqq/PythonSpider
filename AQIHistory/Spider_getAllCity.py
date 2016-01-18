# coding:UTF-8
__author__ = 'L'

import urllib2
import os
from bs4 import BeautifulSoup
import re
import sys
reload(sys)

sys.setdefaultencoding( "UTF-8" )       #  防止写文件编码错误写出错。
def get_soup(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36')
    html = urllib2.urlopen(request).read()
    soup = BeautifulSoup(html.decode('gb2312','ignore'), "html.parser")
    return soup

def get_cityurl(url):
    soup = get_soup(url)
    city_list = soup.find_all('dl')  # 是l不是1


    for i in city_list:
        province = i.find_all('b')
        print province[0].text  # 加【0】编码改变，加text去掉两端的标识。
        file = open(province[0].text, 'w')

        allcities = i.find_all('a')  # dd ?
        for j in allcities:
            # print j.text
            # print j['href']
            file.write(j.text + " " + j['href'] + "\n" )

        file.close()


if __name__ == '__main__':
    url = 'http://www.tianqihoubao.com/aqi/'
    get_cityurl(url)
