# coding:utf-8
__author__ = 'L'
#---------------------------------------
#   程序：百度贴吧图片爬虫
#   版本：0.1
#   作者：l
#   日期：2015-12-28
#   语言：Python 2.7
#   操作：输入网址后自动保存贴吧内图片到本地
#   功能：贴吧内网页所有图片存储到本地。
#---------------------------------------

import re
import urllib

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)" pic_ext='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.gif' % x)
        print '第', x , '张下载完成、'
        x += 1

# 参数 如： http://tieba.baidu.com/p/3191208081
# 可使用参数输入 参见BaiduTieba.py
html = gethtml('')
# print html
getImg(html)