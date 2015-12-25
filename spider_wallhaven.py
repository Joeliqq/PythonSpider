__author__ = 'L'

import urllib
import urllib2

url = 'http://alpha.wallhaven.cc/random'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0' # 注释注意中英文

request = urllib2.Request(url)

request.add_header('User-Agent', user_agent)

response = urllib2.urlopen(request)
the_page = response.read()
print the_page