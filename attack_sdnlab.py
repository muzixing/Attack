import urllib2, urllib, re

i=100
url = "http://www.sdnlab.com"

while  i>0:
	page_data = urllib2.urlopen(url)
	print "the %s time to get sdnlab.com" %i
	i -= 1


