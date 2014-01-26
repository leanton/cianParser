#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

COST_AUTO = 5

class Appartment(object):
	"""Appartment class consists of features that have all appartments"""
	def __init__(self, address, metro, transportation, rooms, space, price, floor, addInfo):
		super(Appartment, self).__init__()

		self.address = self.setAddress(address)
		self.metro = self.setMetro(metro)
		self.transportation = self.setTransportation(transportation)
		self.rooms = self.setRooms(rooms)
		self.space = self.setSpace(space)
		self.price = self.setPrice(price)
		self.floor = self.setFloor(floor)
		self.addInfo = self.setAddInfo(addInfo)

	# Getter methods

	def getAddress(self):
		return self.address

	def getMetro(self):
		return self.metro

	def getTransportation(self):
		return self.transportation

	def getRooms(self):
		return self.rooms

	def getSpace(self):
		return self.space

	def getPrice(self):
		return self.price

	def getFloor(self):
		return self.floor

	def getAddInfo(self):
		return self.addInfo

	# Setter methods

	def setAddress(self, address):
		if (type(address) is str) or (type(address) is unicode):
			self.address = address
		else:
			print "Can't set proper address, type is not string"
			self.address = None
		return self.address

	def setMetro(self, metro):
		if (type(metro) is str) or (type(metro) is unicode):
			self.metro = metro
		else:
			print "Can't set metro, type is not string"
			self.metro = None
		return self.metro

	def setTransportation(self, transportation):
		if type(transportation) is dict:
			self.transportation = transportation
		elif (type(transportation) is str) or (type(transportation) is unicode):
			time = re.search(u'\d+', transportation)
			auto = re.search(u'авто', transportation)
			foot = re.search(u'пешком', transportation)
			if time and auto:
				time = int(time.group())
				d = {}
				d['auto'] = time
				self.transportation = d
			elif time and foot:
				time = int(time.group())
				d = {}
				d['foot'] = time
				self.transportation = d
			else:
				self.transportation = None
			return self.transportation

	def setRooms(self, rooms):
		if type(rooms) is int:
			self.rooms = rooms
		elif (type(rooms) is str) or (type(rooms) is unicode):
			room = re.search(u'\d', rooms)
			if room:
				room = int(room.group())
				self.rooms = room
			else:
				print "error, no match"
				self.rooms = None
		else:
			print "type error, current type is " + type(rooms)
			self.rooms = None
		return self.rooms

	def setSpace(self, space):
		if type(space) is dict:
			self.space = space
		elif type(space) is list:
			d = {}
			for typo in space:
				if re.search(u'кухня', typo):
					area = re.search(u'\d+', typo)
					area = int(area.group())
					d['kitchen'] = area
				elif re.search(u'жилая', typo):
					area = re.search(u'\d+', typo)
					area = int(area.group())
					d['dwelling'] = area
				elif re.search(u'общая', typo):
					area = re.search(u'\d+', typo)
					area = int(area.group())
					d['full'] = area
				elif typo == "NULL":
					pass
				else:
					print "Error, no matching typo's. Current typo is " + typo
			self.space = d
		else:
			print "Error with setting space"
			self.space = None
		return self.space

	def setPrice(self, price):
		if (type(price) is int) or (type(price) is float):
			print "type is " + str(type(price))
			self.price = int(price)
		elif (type(price) is str) or (type(price) is unicode):
			price = price.replace(u',', '')
			price = re.search(u'^\d+', price)
			if price:
				self.price = int(price.group())
			else:
				print "No match of price in string"
				self.price = None
		else:
			print "Type error, current type is " + str(type(price))
			self.price = None
		return self.price

	def setFloor(self, floor):
		if type(floor) is tuple:
			self.floor = floor
		elif (type(floor) is str) or (type(floor) is unicode):
			floor = floor.split("/")
			if len(floor) == 2:	
				floor = (int(floor[0]), int(floor[1]))
				self.floor = floor
			else:
				print "length of floor array is not 2, len = " + len(floor)
				self.floor = None
		else:
			print "Type error, current type is " + type(floor)
			self.floor = None
		return self.floor

	def setAddInfo(self, addInfo):
		if type(addInfo) is list:
			self.addInfo = addInfo
		elif (type(addInfo) is str) or (type(addInfo) is unicode):
			addInfo = addInfo.split('|')
			self.addInfo = addInfo
		else:
			print "Type error, current type is " + type(addInfo)
			self.addInfo = None
		return self.addInfo

	# Helper methods to preprocess data
	def preprocessData1(self):
		line = []
		address = self.address
		if address:
			line.append(address)
		metro = self.metro
		if metro:
			line.append(metro)
		transportation = self.transportation
		if transportation:
			if 'auto' in transportation:
				line.append(str(COST_AUTO*transportation['auto']))
			elif 'foot' in transportation:
				line.append(str(transportation['foot']))
			else:
				print "no line about transportation"
		rooms = self.rooms
		if rooms:
			line.append(str(rooms))
		space = self.space
		if space:
			if 'kitchen' in space:
				line.append(str(space['kitchen']))
			if 'dwelling' in space:
				line.append(str(space['dwelling']))
			if 'full' in space:
				line.append(str(space['full']))
		price = self.price
		if price:
			line.append(str(price))
		floor = self.floor
		if floor and floor[1]!=0:
			num = round(float(floor[0])/float(floor[1]), 2)
			line.append(str(num))
		return line




