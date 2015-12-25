# coding:utf-8
# 下载百度贴吧内对应页码的所有页面存储为html文件
import string, urllib2

def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page + 1):
        sname = string.zfill(i, 5) + '.html' # 自动填充6位作为文件名
        print 'Downloading ' + str(i) + 'page and saving as ' + sname + '......' # str() 类型转换
        f = open(sname, 'w+')   # 文件流？
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()

#----------在这里输入参数--------------
bdurl = str(raw_input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))
begin_page = int(raw_input(u'请输入开始的页数：\n'))
end_page = int(raw_input(u'请输入终点的页数：\n'))
#----------在这里输入参数--------------

baidu_tieba(bdurl,begin_page,end_page)