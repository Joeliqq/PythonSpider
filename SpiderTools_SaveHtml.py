# coding:UTF-8

import urllib2
import string

url = str(raw_input(u'URL input \n'))

header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
file = open('Download/page.html', 'w+')
req = urllib2.Request(url, None, headers=header)

file.write(urllib2.urlopen(req).read())

# 这个跟在浏览器上解析的不太一样，还是看浏览器的既方便又丰富