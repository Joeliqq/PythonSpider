# coding:utf-8

import urllib2
import re
import os


url = 'http://alpha.wallhaven.cc/random'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'

request = urllib2.Request(url)
request.add_header('User-Agent', user_agent)

html = urllib2.urlopen(request).read()

reg = r'wallpaper'