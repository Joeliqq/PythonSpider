#coding:utf-8

import urllib
import urllib2

url = 'http://ip.chinaz.com/'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' # 模拟（伪装）
header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

values = {'name' : 'XXX',
          'location' : 'neu',
          'language' : 'python'}

headers = {'user-agent' : header}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page