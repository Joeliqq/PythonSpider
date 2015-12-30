# coding:utf-8

# ---------------------------------
#
# 抓取豆瓣美女图片
#
# ---------------------------------

from bs4 import BeautifulSoup
import os
import sys
import urllib2

# 创建文件夹
path = os.getcwd()
new_path = os.path.join(path, u'豆瓣美女')
if not os.path.isdir((new_path)):
    os.mkdir(new_path)

def page_loop(page = 0):
    url = 'http://www.dbmeinv.com/?pager_offset=%s' % page
    content = urllib2.urlopen(url)   # 不用read() ?

    soup = BeautifulSoup(content)

    mg_girl = soup.find_all('img')

    # 加入检测
    if mg_girl == []:
        print u'抓取完成'
        sys.exit(0)

    print u'开始抓取'
    for girl in mg_girl:
        link = girl.get('src')
        flink = 'http://www.dbmeinv.com/' +link
        print flink

        content2 = urllib2.urlopen(flink).read()
        with open(u'豆瓣美女' + '/' + flink[-11:], 'wb') as code:
            code.write(content2)

    page = int(page) + 1
    print u'开始抓取下一页'
    print 'the %s page' % page
    page_loop(page)


page_loop()
