#!/usr/bin/python
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

'''Global variables of the links'''

'''For rent URLs'''
HREF1 = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&type=4&room1=1&p={}'
HREF2 = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&type=4&room2=1&p={}'
HREF3 = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&type=4&room3=1&p={}'
HREF4 = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&type=4&room4=1&p={}'
HREF5 = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&type=4&room4=1&p={}'
HREF6 = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&type=4&room4=1&p={}'

'''For sell URLs'''
S_HREF1 = 'http://www.cian.ru/cat.php?deal_type=2&obl_id=1&room1=1&p={}'
S_HREF2 = 'http://www.cian.ru/cat.php?deal_type=2&obl_id=1&room2=1&p={}'
S_HREF3 = 'http://www.cian.ru/cat.php?deal_type=2&obl_id=1&room3=1&p={}'
S_HREF4 = 'http://www.cian.ru/cat.php?deal_type=2&obl_id=1&room4=1&p={}'


def loadHelper(uri):
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	try:
		thing = opener.open(uri, None, 10)
		soup = BeautifulSoup(thing.read(), "lxml")
		if not (soup is None):
			return soup
		else:
			print "soup is None"
			loadHelper(uri)
	except (timeout, urllib2.HTTPError, urllib2.URLError) as error:
		sys.stdout.write("{} encountered, hold on, bro".format(error))
		sys.stdout.flush()
		time.sleep(30)
		loadHelper(uri)

def parsePage(pageNum):
	uri = HREF1.format(pageNum)
	soup = loadHelper(uri)
	#print(soup.prettify())
	table = soup.find_all('tr', id=re.compile('tr_(\d+)'))
	if (table == []):
		print "no table"
	data_table = []

	for sampleRow in table:
		fields = [u'metro', u'room', u'rooms', u'price', u'floor', u'dopsved']
		data_row = []
		for field in fields:	
			data = sampleRow.find_all('td', id=re.compile('(.)_' + field))[0]

			''' Parsing code is written with if statement, need to refactor, seems to be too stupid '''

			''' Parsing address <td>'''
			if (field == fields[0]):
				address = data.get_text('|', strip = True).split('|')
				line = ""
				for i in range(len(address)-2):
					if (i != len(address)-2):
						line += address[i] + ", "
					else:
						line += address[i]
				data_row.append(line)
				data_row.append(address[-1])
				data_row.append(address[-2])
				#print address.split('|')
				#print repr(address).decode("unicode-escape")

			if (field == fields[1]):
				room = data.get_text()
				#print repr(room).decode("unicode-escape")
				data_row.append(room)

			'''Room space'''
			if (field == fields[2]):
				rooms = data.get_text('|', strip = True)

				'''Kitchen space'''
				kitchen = re.search(u'кухня:(\W)\d+', rooms)
				if (kitchen != None):
					data_row.append(kitchen.group())
				else:
					data_row.append(u'NULL')

				'''Dwelling space'''
				dspace = re.search(u'жилая:(\W)\d+', rooms)
				if (dspace != None):
					data_row.append(dspace.group())
				else:
					data_row.append(u'NULL')

				'''Full space'''
				space = re.search(u'общая:(\W)\d+', rooms)
				if (space != None):
					data_row.append(space.group())
				else:
					data_row.append(u'NULL')
				
			'''Price of the appartments'''
			if (field == fields[3]):
				price_raw = data.get_text('|', strip = True).split('|')
				price = price_raw[0]
				if (price != None):
					data_row.append(price)
				else:
					data_row.append(u'NULL')

			'''# of the floor'''
			if (field == fields[4]):
				floor = data.get_text('|', strip = True)
				data_row.append(floor)

			'''Additional information'''
			if (field == fields[5]):
				addinfo = data.get_text('|', strip = True)
				data_row.append(addinfo)

		
		'''End of data to parse, appending row to a table'''		
		#print repr(data_row).decode("unicode-escape")
		data_table.append(data_row)
	#print repr(data_table).decode("unicode-escape")

	# returns an array of arrays with data cells
	return data_table


def export(data, filename="foo.txt"):
	f = codecs.open(filename, 'w+', 'utf-8')
	for row in data:
		for cell in row:
			f.write(cell)
			f.write(u'	')
		f.write(u'\n')

def getTable(pageNum, URL=HREF1):
	uri = URL.format(pageNum)
	try:
		soup = loadHelper(uri)
		#print(soup.prettify())
		table = soup.find_all('tr', id=re.compile('tr_(\d+)'))
		if not (table is None):
			return table
		else:
			print "table is None"
			getTable(pageNum, URL)
	except AttributeError:
		print "AttributeError raised exception"
		getTable(pageNum, URL)


def parseTable(table):
	data_table = []

	for sampleRow in table:
		fields = [u'metro', u'room', u'rooms', u'price', u'floor', u'dopsved']
		data_row = []
		for field in fields:	
			data = sampleRow.find_all('td', id=re.compile('(.)_' + field))[0]

			''' Parsing code is written with if statement, need to refactor, seems to be too stupid '''

			''' Parsing address <td>'''
			if (field == fields[0]):
				address = data.get_text('|', strip = True).split('|')
				line = ""
				for i in range(len(address)-2):
					if (i != len(address)-2):
						line += address[i] + ", "
					else:
						line += address[i]
				data_row.append(line)
				data_row.append(address[-1])
				data_row.append(address[-2])
				#print address.split('|')
				#print repr(address).decode("unicode-escape")

			if (field == fields[1]):
				room = data.get_text()
				#print repr(room).decode("unicode-escape")
				data_row.append(room)

			'''Room space'''
			if (field == fields[2]):
				rooms = data.get_text('|', strip = True)

				'''Kitchen space'''
				kitchen = re.search(u'кухня:(\W)\d+', rooms)
				if (kitchen != None):
					data_row.append(kitchen.group())
				else:
					data_row.append(u'NULL')

				'''Dwelling space'''
				dspace = re.search(u'жилая:(\W)\d+', rooms)
				if (dspace != None):
					data_row.append(dspace.group())
				else:
					data_row.append(u'NULL')

				'''Full space'''
				space = re.search(u'общая:(\W)\d+', rooms)
				if (space != None):
					data_row.append(space.group())
				else:
					data_row.append(u'NULL')
				
			'''Price of the appartments'''
			if (field == fields[3]):
				price_raw = data.get_text('|', strip = True).split('|')
				price = price_raw[0]
				if (price != None):
					data_row.append(price)
				else:
					data_row.append(u'NULL')

			'''# of the floor'''
			if (field == fields[4]):
				floor = data.get_text('|', strip = True)
				data_row.append(floor)

			'''Additional information'''
			if (field == fields[5]):
				addinfo = data.get_text('|', strip = True)
				data_row.append(addinfo)

		
		'''End of data to parse, appending row to a table'''		
		#print repr(data_row).decode("unicode-escape")
		data_table.append(data_row)
	#print repr(data_table).decode("unicode-escape")

	# returns an array of arrays with data cells
	return data_table

if __name__ == "__main__":
	url = S_HREF4
	page_start = int(sys.argv[1])
	page_end = int(sys.argv[2]) + 1
	for page_num in range(page_start,page_end):
		table = getTable(page_num, url)
		while (table == []):
			time.sleep(2)
			table = getTable(page_num, url)
		data = parseTable(table)
		export(data, str(page_num) + '_data.txt')
		sys.stdout.write(" #{} page is parsed".format(page_num))
		sys.stdout.flush()
		#time.sleep(2)
		sys.stdout.write("\r")
		sys.stdout.flush()