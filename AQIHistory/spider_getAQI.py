# coding:UTF-8
__author__ = 'L'
#  -----------------
#
#
#
#
#  ------------------

import urllib2
import random
from bs4 import BeautifulSoup
import spider_AQIHistory

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )       #  防止写文件编码错误写出错。

def get_soup(url):
    headers = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]


    header={"User-Agent":random.choice(headers)}
    request=urllib2.Request(url, headers = header)
    # 增加

    # 防止http 500 错误， 自动等待。
    try:
        resp = urllib2.urlopen(request)
        contents = resp.read()
    except urllib2.HTTPError, error:
        contents = error.read()
    soup = BeautifulSoup(contents.decode('gb2312','ignore'), "html.parser")  # 跨平台要加上解析的方式？！
    return soup


def save_AQI(filename, url):
    '输入具体地点的具体月份，保存该月份数据到指定文件名'
    soup = get_soup(url)
    # lines = soup.find_all('table', class_ = 'b')
    lines = soup.find_all('td')
    # print lines[-1]

    file = open(filename, 'w')
    for i in lines:
        # print str(i.text).strip()  #  strip()去掉两端空格。 strip('\n') 去掉回车、
        file.write(str(i.text).strip() + '\n')
        # perline = i.find_all('td')
        # for j in perline:
        #     print j.text
    file.close
    return

def save_FomartAQI(filename, url):
    '输入具体地点的具体月份，保存该月份数据到指定文件名'
    soup = get_soup(url)
    # lines = soup.find_all('table', class_ = 'b')
    lines = soup.find_all('tr')
    # print lines[-1]

    file = open(filename, 'w')
    for i in lines:
        # print str(i.text).strip()  #  strip()去掉两端空格。 strip('\n') 去掉回车、
        # file.write(str(i.text).strip() + '\n')
        perline = i.find_all('td')
        for j in perline:
            # print j.text
            file.write(str(j.text).strip() + '   ')
        file.write('\n')
    file.close
    return

if __name__ == '__main__':


    # 单独测试
    filename = u'2015年11月北京PM2.5指数.txt'
    #  中文文件名或者目录。
    url = 'http://www.tianqihoubao.com/aqi/beijing-201511.html'  #  url ex
    # get_AQI(filename, url)
    save_FomartAQI(filename, url)

    # for i in fileurls:
    #     print i
    #     city = i[0]
    #     city_url = "http://www.tianqihoubao.com" + i[1]
    #     print city + city_url

    # webURL = []
    # from itertools import islice
    # for line in islice(file, 1|2|3|4, None):
    #     print line[0]
    #     print line[1]
    #     webURL.append([line[0],line[1]])
    # print str(webURL[0])
    # print webURL[1]


        # for j in city_urllist:
        #     monthlist = spider_AQIHistory.getPerMonthURL(j)
        #     print monthlist


    # 测试  循环

    # city_url = 'http://www.tianqihoubao.com/aqi/beijing.html'
    #
    # monthlist = spider_AQIHistory.getPerMonthURL(city_url)  #  输入 城市分页面的，得到该城市每个月份的文件名与URL
    # for i in monthlist:
    #     filename = i[0] + '.txt'
    #     historyurl = i[1]
    #     print 'Download ' + filename + '...'
    #     get_AQI(filename, historyurl)


