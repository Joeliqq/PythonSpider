__author__ = 'L'

import urllib
import urllib2

url = "http://www.someserver.com/register.cgi"

# python 字典
values = {'name' : 'xxx',
          'location' : 'neu',
          'language' : 'python'}

data = urllib.urlencode(values)  # 编码
req = urllib2.Request(url, data)  # 发送请求同时传data表单
response = urllib2.urlopen(req)  # 接受反馈信息
the_page = response.read()  # 读取

