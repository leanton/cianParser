# -*- coding: utf-8 -*-
import urllib2
import re
from math import floor
import codecs
import sys
import lxml
import time
from socket import timeout
from bs4 import BeautifulSoup


def loadHelper(uri):
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	try:
		thing = opener.open(uri, None, 10)
		soup = BeautifulSoup(thing.read(), "lxml")
	except (timeout, urllib2.HTTPError, urllib2.URLError) as error:
		sys.stdout.write("{} encountered, hold on, bro".format(error))
		sys.stdout.flush()
		time.sleep(30)
		loadHelper(uri)
	return soup

def parsePage(pageNum):
	uri = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&type=4&room1=1&p={}'.format(pageNum)
	soup = loadHelper(uri)
	#print(soup.prettify())
	table = soup.find_all('tr', id=re.compile('tr_[0-9]'))
	sampleRow = table[0]

	data_table = []

	for sampleRow in table:
		fields = [u'metro', u'room', u'rooms', u'price', u'floor', u'dopsved']
		data_row = []
		for field in fields:	
			data = sampleRow.find_all('td', id=re.compile('(.)_' + field))[0]
			if (field == fields[0]):
				adress = data.get_text('|', strip = True).split('|')
				if len(adress) == 5:
					data_row.append(adress[0] + ", " + adress[1] + ", " + adress[2])
				elif len(adress) == 4:
					data_row.append(adress[0] + ", " + adress[1])
				elif len(adress) == 3:
					data_row.append(adress[0])
				elif len(adress) == 6:
					data_row.append(adress[0] + ", " + adress[1] + ", " + adress[2]  + ", " + adress[3])
				elif len(adress) == 7:
					data_row.append(adress[0] + ", " + adress[1] + ", " + adress[2]  + ", " + adress[3] + ", " + adress[4])
				data_row.append(adress[-1])
				data_row.append(adress[-2])
				#print adress.split('|')
				#print repr(adress).decode("unicode-escape")
		print repr(data_row).decode("unicode-escape")
		data_table.append(data_row)
	print repr(data_table).decode("unicode-escape")

	# returns an array of arrays with data cells
	return data_table


def export(data):
	f = codecs.open('foo.txt', 'w+', 'utf-8')
	for row in data:
		for cell in row:
			f.write(cell)
			f.write(u'	')
		f.write(u'\n')
	

if __name__ == "__main__":
	page = int(sys.argv[1])
	data = parsePage(page)
	export(data)