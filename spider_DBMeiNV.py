# coding:utf-8

# ----------------------------
# python 爬虫抓取豆瓣美女图片
#
# 使用 BeautifulSoup4工具
#
# ----------------------------

import urllib2
from bs4 import BeautifulSoup
import socket

baseurl = 'http://www.dbmeinv.com/dbgroup/show.htm'

def user_agent(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req_timeout = 20
    try:
        req = urllib2.Request(url, None, req_header)
        html = urllib2.urlopen(req, None, req_timeout)
    except urllib2.URLError as e:
        print e.message
    except socket.timeout as e:
        user_agent(url)
    return  html

def page_loop(pageid):
    url = baseurl + '?pager_offset=%s'%pageid
    print url
    page = user_agent(url)
    print page
    soup = BeautifulSoup(page)
    total_img = 0
    img = soup.find_all(['img'])
    for myimg in img:
        link = myimg.get('src')
        total_img += 1
        print link
        #content2 = urllib2.urlopen(link).read() # 从这里可以看出是函数式编程
        content2 = user_agent(link).read()
        with open(u'Download' + '/' + link[-11:], 'wb') as code :
            code.write(content2) # 函数式写法
        print total_img
        return total_img

page_start = 1
page_stop = 4
total = 0
for i in range(page_start, page_stop):
    total += page_loop(i)

print total