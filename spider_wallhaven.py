# coding:utf-8

import urllib2
import re
import urllib
import os

# 参考 http://lyeec.me/blog/crawler/#%E6%9C%80%E7%BB%88%E7%89%88%E6%9C%AC
'''
url = 'http://alpha.wallhaven.cc/random'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
request = urllib2.Request(url)
request.add_header('User-Agent', user_agent)
html = urllib2.urlopen(request).read()
'''
def getHtml(url):
    'get-content-of-html'
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36')
    return urllib2.urlopen(request).read()

def getImgList(html):
    'get the id list of the pictures'
    reg = r'data-wallpaper-id="(\d*?)"' #  ?
    pattern = re.compile(reg)
    img_list = re.findall(pattern, html)
    return  img_list

def getImgURL(imgid):
    'get url of the pic by id'
    return 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + imgid + '.jpg' #   这个才是真正的图片的地址，不是每个图片打开网页后的地址、

def run():
    results = []
    url = "http://alpha.wallhaven.cc/random"
    pageNum = int(raw_input('how many pages would you want (25 pictures in one page) : '))

    #  get the id of the pictures
    while pageNum > 0:
        pageNum -= 1
        print 'Writing Random Page...'
        results += getImgList(getHtml(url))

    results = list(set(results))

    #  write the pictures url into text
    file = open('url.txt', 'w')
    for imgid in results:
        file.write(getImgURL(imgid) + '\n')
        saveImg(getImgURL(getHtml(url)), str(imgid))
    file.close()


if __name__ == '__main__':
    run()