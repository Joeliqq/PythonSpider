# coding:UTF-8

# ---------------------
#
#   拽百度图片到本地
#
# ---------------------

import urllib2

url = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1450430011617_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&itg=0&ie=utf-8&word=%E5%B0%8F%E6%B8%85%E6%96%B0%E5%9B%BE%E7%89%87'

header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

req = urllib2.Request(url,headers=header)
try:
    content = urllib2.urlopen(req).read()
except urllib2.URLError,e:
    print e
f = open('a.txt','w+')
f.write(content)
f.close()