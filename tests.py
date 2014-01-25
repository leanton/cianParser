#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from appartment import Appartment

def testTransportation(transportation):
	if type(transportation) is str or unicode:
		time = re.search(u'\d+', transportation)
		auto = re.search(u'авто', transportation)
		foot = re.search(u'пешком', transportation)
		if time and auto:
			time = int(time.group())
			d = {}
			d['auto'] = time
			return d
		elif time and foot:
			time = int(time.group())
			d = {}
			d['foot'] = time
			return d
		else:
			return "error"
	else:
		return "error, no string"

def testRooms(rooms):
	if type(rooms) is str or unicode:
		room = re.search(u'\d', rooms)
		if room:
			room = int(room.group())
			return room
		else:
			print "error, no match"
			return None
	else:
		print "error, type is WAT? " + type(rooms)
		return None


def testAppartment():
	string = u"Москва, Новосибирская улица, д.6к1, 	м.Щелковская	15мин. пешком	1-комн. квартира	кухня: 6	жилая: 35	общая: 35	35,000р.	1/9	кух.мебель|жил.мебель|телефон|ТВ|стир.машина|холодильник|можно с животными|можно с детьми"
	array = string.split("	")
	print repr(array).decode("unicode-escape")
	address = array[0]
	metro = array[1]
	transportation = array[2]
	rooms = array[3]
	space = [array[4], array[5], array[6]]
	price = array[7]
	floor = array[8]
	addInfo = array[9]
	appartment = Appartment(address, metro, transportation, rooms, space, price, floor, addInfo)
	print appartment
	print appartment.getAddress()
	print appartment.getPrice()


#print testTransportation(u"32мин. пешком")
#print testRooms(u"1-комн. квартира")
testAppartment()