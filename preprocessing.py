#!/usr/bin/python
# -*- coding: utf-8 -*-

from appartment import Appartment
import codecs
import sys

def preprocessData1(filename_input, filename_output="foo.txt"):
	f = codecs.open(filename_input, 'rU', 'utf-8')
	f_out = codecs.open(filename_output, 'w+', 'utf-8')
	new_data = []
	for line in f:
		appartment = parseLine(line)
		new_line = appartment.preprocessData1()
		if len(new_line) == 9:
			new_line = u'	'.join(new_line)
			f_out.write(new_line)
			f_out.write(u'\n')
	f.close()
	f_out.close()	



def parseLine(line):
	array = line.split("	")
	#print repr(array).decode("unicode-escape")
	address = array[0]
	metro = array[1]
	transportation = array[2]
	rooms = array[3]
	space = [array[4], array[5], array[6]]
	price = array[7]
	floor = array[8]
	addInfo = array[9]
	appartment = Appartment(address, metro, transportation, rooms, space, price, floor, addInfo)
	return appartment

if __name__ == "__main__":
	filename_input = str(sys.argv[1])
	filename_output = str(sys.argv[2])
	preprocessData1(filename_input, filename_output)
	print "Done"