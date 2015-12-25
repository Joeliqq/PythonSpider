__author__ = 'L'

from urllib2 import Request, urlopen, URLError, HTTPError

req = Request('http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1450430011617_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&itg=0&ie=utf-8&word=%E5%B0%8F%E6%B8%85%E6%96%B0%E5%9B%BE%E7%89%87')

try:
    response = urlopen(req)
except HTTPError, e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code : ' , e.code
except URLError, e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
else:
    print 'No exception was raised.'