#  coding:utf-8

import urllib2
import random
import os
from bs4 import BeautifulSoup


def getSoup(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36')
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")       #  "html.parser" 是指定beautifulsoup的解析器
    return soup

def saveImaURL(url):
    soup = getSoup(url)
    filterURL = soup.find_all('a',class_="view_img_link")
    # imageURL = filterURL[0]['href']     #  nice第一个代表数组，总共只有一个，第二个代表其中的哪个元素、
    # print imageURL
    imglist = []
    # print filterURL[1]

    file = open('url.txt', 'w')
    for i in filterURL:
        # print i         #       i 是 BeautifulSoup得到的所有的匹配元素遍历时的之一，是tag类型，相当于是filterURL这个数组中的一个。
        # print i['href']     #   这个相当于一个字典，对应关系，即映射、 （字典通常一对一，也能够实现一对多）
        imageURL = i['href']
        imglist.append(imageURL)
        file.write(imageURL + '\n')
        # imageURL = filterURL[0]['href']
        # print imageURL
        # imglist.append(imageURL)
        # file.write(imageURL + '\n')
    file.close()
    return imglist

# def saveURL2Text():
#     file = open('url.txt', 'w')
#     for imgid in saveImaURL():
#         file.write(getImaURLList + '\n')
#     file.close()

def wgetImage():
    command = 'wget -P ./jiandanmeizitu -c -i url.txt'
    os.system(command)
    return

if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    saveImaURL(url)
    wgetImage()
