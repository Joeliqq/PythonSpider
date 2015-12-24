__author__ = 'L'

import urllib
import urllib2


# 字典的另一形式
data = {}
data['name'] = 'xx'
data['location'] = 'neu'
data['language'] = 'python'

url_values = urllib.urlencode(data)
print url_values

url = 'http://www.baidu.com/example'
full_url = url + '?' + url_values;
data = urllib2._open(full_url)