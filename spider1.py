__author__ = 'L'

import urllib2

request = urllib2.Request("http://wallbase.fr/abstract-bokeh-digital-art-minimalistic")
response = urllib2.urlopen(request)
the_page = response.read()
print the_page