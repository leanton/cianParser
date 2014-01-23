#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

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





print testTransportation(u"32мин. пешком")
print testRooms(u"1-комн. квартира")