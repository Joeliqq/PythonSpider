__author__ = 'L'

import urllib
import urllib2

url = 'http://ip.chinaz.com/'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' # 模拟（伪装）

values = {'name' : 'XXX',
          'location' : 'neu',
          'language' : 'python'}

headers = {'user-agent' : user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page